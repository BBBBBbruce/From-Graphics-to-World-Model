# SPDX-License-Identifier: MIT
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("world", Path(__file__).resolve().parents[1] / "examples/one_dimensional_world.py")
world = importlib.util.module_from_spec(spec)
spec.loader.exec_module(world)


class WorldTests(unittest.TestCase):
    def test_deadband_and_symmetry(self):
        for a in (-0.02, -0.01, 0.0, 0.01, 0.02):
            self.assertEqual(world.transition(0.5, a, 0.02), 0.5)
        self.assertAlmostEqual(world.transition(0.5, 0.05, 0.02), 0.53)
        self.assertAlmostEqual(world.transition(0.5, -0.05, 0.02), 0.47)
        with self.assertRaises(ValueError):
            world.transition(0.5, 0.01, -0.02)

    def test_noiseless_recovery(self):
        fitted = world.fit(world.sample(10, 200, 0.035))
        self.assertEqual(fitted["deadband"]["width"], 0.035)

    def test_reference_model_has_zero_regret(self):
        report = world.evaluate("deadband", {"width": 0.02}, world.sample(42, 200, 0.02), 0.02)
        self.assertAlmostEqual(report["prediction_mae_m"], 0.0)
        self.assertAlmostEqual(report["decision_regret_m"], 0.0)

    def test_reproducibility_and_nonnegative_regret(self):
        self.assertEqual(world.run(4), world.run(4))
        for result in world.run(4)["results"]:
            self.assertGreaterEqual(result["decision_regret_m"], -1e-14)
            self.assertLessEqual(result["successes"], result["count"])

    def test_training_is_independent_of_evaluation(self):
        data = world.sample(7, 100, 0.02, 0.003)
        fitted = world.fit(data)
        before = repr(fitted)
        world.evaluate("deadband", fitted["deadband"], world.sample(8, 100, 0.04), 0.04)
        self.assertEqual(repr(fitted), before)
        self.assertNotEqual(data, world.sample(8, 100, 0.02, 0.003))

    def test_tie_rule_prefers_no_motion(self):
        self.assertEqual(world.choose("persistence", {}, 0.5, 0.55), 0.0)


if __name__ == "__main__":
    unittest.main()
