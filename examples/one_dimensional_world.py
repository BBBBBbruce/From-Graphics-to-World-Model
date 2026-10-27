#!/usr/bin/env python3
"""A one-step response model and decision experiment. Python stdlib only.

SPDX-License-Identifier: MIT
The deadband law is a teaching construction, not a physical contact simulator.
"""
from __future__ import annotations
import argparse
import csv
import json
import math
from pathlib import Path
import random

ACTIONS = tuple(i / 200 for i in range(-20, 21))
WIDTHS = tuple(i / 1000 for i in range(61))


def transition(state: float, action: float, width: float) -> float:
    if width < 0:
        raise ValueError("deadband width must be nonnegative")
    return state + math.copysign(max(abs(action) - width, 0.0), action)


def sample(seed: int, count: int, width: float, noise: float = 0.0) -> list[dict]:
    rng = random.Random(seed)
    data = []
    for _ in range(count):
        state, action = rng.uniform(0.1, 0.9), rng.uniform(-0.1, 0.1)
        target = state + rng.uniform(-0.06, 0.06)
        next_state = transition(state, action, width)
        observation = next_state + rng.uniform(-noise, noise)
        data.append(dict(state=state, action=action, next_state=next_state,
                         next_observation=observation, target=target))
    return data


def fit(data: list[dict]) -> dict:
    if not data:
        raise ValueError("training data cannot be empty")
    denom = sum(row["action"] ** 2 for row in data)
    gain = (sum(row["action"] * (row["next_observation"] - row["state"])
                for row in data) / denom) if denom else 0.0
    width = min(WIDTHS, key=lambda k: sum(
        (transition(row["state"], row["action"], k) - row["next_observation"]) ** 2
        for row in data))
    return {"persistence": {}, "linear": {"gain": gain}, "deadband": {"width": width}}


def predict(model: str, params: dict, state: float, action: float) -> float:
    if model == "persistence":
        return state
    if model == "linear":
        return state + params["gain"] * action
    if model == "deadband":
        return transition(state, action, params["width"])
    raise ValueError(f"unknown model: {model}")


def choose(model: str, params: dict, state: float, target: float) -> float:
    # Primary key: target error. Ties: smaller magnitude, then smaller signed action.
    return min(ACTIONS, key=lambda a: (abs(predict(model, params, state, a) - target),
                                      abs(a), a))


def evaluate(model: str, params: dict, data: list[dict], true_width: float) -> dict:
    errors, regrets, successes = [], [], 0
    for row in data:
        s, a, g = row["state"], row["action"], row["target"]
        errors.append(abs(predict(model, params, s, a) - row["next_state"]))
        selected = choose(model, params, s, g)
        chosen_error = abs(transition(s, selected, true_width) - g)
        best_error = min(abs(transition(s, x, true_width) - g) for x in ACTIONS)
        regrets.append(chosen_error - best_error)
        successes += chosen_error <= 0.004
    return dict(count=len(data), prediction_mae_m=sum(errors) / len(data),
                decision_regret_m=sum(regrets) / len(data),
                successes=successes, success_rate=successes / len(data))


def run(seed: int = 2026) -> dict:
    training = sample(seed, 400, 0.02, noise=0.003)
    models = fit(training)
    settings = dict(seed=seed, training_count=400, test_count_per_condition=200,
                    training_width_m=0.02, training_noise_half_width_m=0.003,
                    candidate_count=len(ACTIONS), candidate_step_m=0.005,
                    success_tolerance_m=0.004,
                    test_seeds={"original": seed + 1, "shifted": seed + 2},
                    reference="known deterministic toy transition; no evaluation noise",
                    selection="target error, then command magnitude, then signed command")
    results = []
    for index, (condition, width) in enumerate((("original", 0.02), ("shifted", 0.04))):
        data = sample(seed + index + 1, 200, width)
        for model, params in models.items():
            results.append(dict(condition=condition, true_width_m=width, model=model,
                                **evaluate(model, params, data, width)))
    return dict(settings=settings, fitted_parameters=models, results=results)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--output", type=Path, default=Path("results/toy"))
    args = parser.parse_args()
    report = run(args.seed)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "results.json").write_text(json.dumps(report, indent=2) + "\n")
    with (args.output / "results.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(report["results"][0]))
        writer.writeheader()
        writer.writerows(report["results"])
    print("condition model      prediction MAE(m) regret(m) success/count")
    for r in report["results"]:
        print(f'{r["condition"]:9} {r["model"]:11} {r["prediction_mae_m"]:10.5f}'
              f' {r["decision_regret_m"]:10.5f} {r["successes"]}/{r["count"]}')
    print(f"Saved results to {args.output}")


if __name__ == "__main__":
    main()
