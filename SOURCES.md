# Primary sources and verification record

Edition 1.1, revised 27 October 2026. The bibliography records the inspected versions; links below point to primary papers, author project pages, or official documentation. Conference/journal years and preprint revision years have different meanings. Results are scoped to the cited protocol rather than treated as universal capabilities.

## Foundation and graphics

- [Pharr, Jakob, and Humphreys (2023), *Physically Based Rendering*, fourth edition](https://www.pbr-book.org/4ed/Introduction): image formation and rendering from scene descriptions.
- [Mildenhall et al. (2020), NeRF](https://www.matthewtancik.com/nerf): scene representation and novel-view synthesis; not by itself an action-conditioned dynamics model.
- [Kerbl et al. (2023), 3D Gaussian Splatting](https://arxiv.org/abs/2308.04079): Gaussian scene primitives and rendering. The book makes no unmatched rendering-speed comparison.
- [Sutton and Barto (2018), *Reinforcement Learning*, second edition](http://incompleteideas.net/book/RLbook2020.pdf): state, return, value, and temporal-difference learning. The author-hosted PDF is a later file edition.

## Policies, context, and optimization

- [Physical Intelligence (2024), π0, v1](https://arxiv.org/abs/2410.24164v1), [Physical Intelligence (2025), π0.5, v1](https://arxiv.org/abs/2504.16054v1), and [Physical Intelligence (2025), π*0.6 / RECAP, v1](https://arxiv.org/abs/2511.14759v1): action generation, heterogeneous training, and learning from experience. Corporate author–year labels identify the originating group.
- [Chi et al. (2024), Diffusion Policy, inspected v5](https://arxiv.org/abs/2303.04137v5): the bibliography names the expanded journal edition, separately from the earlier 2023 RSS version.
- [Qian et al. (2026), SynthICL, v1](https://arxiv.org/abs/2606.08154v1) and [official project](https://synth-icl.github.io/): visual demonstration context, shared frozen backbone, action flow decoder, and auxiliary subgoal training. Cheng Qian and Yifei Ren are included in the complete author list. The reported 79% across 16 tasks is attributed to the authors' protocol.
- [Vosylius and Johns (2025), Instant Policy, inspected v2](https://arxiv.org/abs/2411.12633v2): point-cloud/graph context representation; ICLR publication year.
- [Vaswani et al. (2017), Attention Is All You Need](https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html): scaled dot-product attention. The later arXiv file date is not used as the conference year.
- [Lipman et al. (2023), Flow Matching](https://openreview.net/forum?id=PqvMRDCJT9t) and [Lipman et al. (2024), Flow Matching Guide, v1](https://arxiv.org/abs/2412.06264v1): reference paths, conditional velocity regression, and sampling.
- [Schulman et al. (2017), PPO, v2](https://arxiv.org/abs/1707.06347v2) and [Schulman et al. (2016), GAE, inspected v6](https://arxiv.org/abs/1506.02438v6): likelihood ratios, clipping, and advantage estimation. GAE's ICLR year is distinguished from its 2018 file revision.
- [McAllister et al. (2025), Flow Matching Policy Gradients, v2](https://arxiv.org/abs/2507.21053v2) and [authors' explanation](https://flowreinforce.github.io/): FPO uses an exponentiated flow-loss difference as a surrogate. The book does not identify it with an exact action-density ratio.
- [Kingma and Gao (2023), v7](https://arxiv.org/abs/2303.00848v7): weighted diffusion objectives and likelihood bounds. Appendix A states the assumptions and retains the non-canceling bound gap.
- [Abdolmaleki et al. (2024), Preference Optimization as Probabilistic Inference, v1](https://arxiv.org/abs/2410.04166v1): PMPO terminology; it is not treated as FPO or PPO.
- [Ross et al. (2011), dataset aggregation](https://proceedings.mlr.press/v15/ross11a.html): the distribution of observations depends on learned behavior.
- Official OpenAI Spinning Up references supplement the derivations: [key concepts](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html), [policy optimization](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html), and [PPO](https://spinningup.openai.com/en/latest/algorithms/ppo.html).

## Prediction and evidence

- [Guo et al. (2026), Ctrl-World, v3](https://arxiv.org/abs/2510.10125v3): multiview prediction, pose conditioning, and memory. The bibliography records the revised preprint edition.
- [Jain et al. (2026), WEAVER, v2](https://arxiv.org/abs/2606.13672v2): latent prediction, memory, reward/value heads, and the specifically attributed timing comparison. Hardware, horizon, NFE, and cache conditions accompany the comparison.
- [Janner et al. (2019), Model-Based Policy Optimization](https://papers.neurips.cc/paper/9416-when-to-trust-your-model-model-based-policy-optimization.pdf): short imagined branches as a response to model error.
- [Yang et al. (2026), RISE, v2](https://arxiv.org/abs/2602.11075v2): frozen learned environment and advantage-conditioned policy learning. Its operational progress score is distinguished from textbook advantage estimators.
- [Guo et al. (2026), VLAW, v2](https://arxiv.org/abs/2602.12063v2): model refresh from real experience and success-filtered policy training, not an FPO update.
- [Lv et al. (2026), SkeLAM, v1](https://arxiv.org/abs/2610.31474v1): training/deployment information availability. Recorded-action replay is distinguished from closed-loop improvement.
- [Wang et al. (2026), Interactive World Simulator, v1](https://arxiv.org/abs/2603.08546v1): compact latent dynamics, task-specific setup, and the distinction between interactive demonstrations and quantitative prediction evaluation.
- [Wang et al. (2026), WorldContact, v1](https://arxiv.org/abs/2609.19600v1): explicit deformable-object states and contact-related structure. Its experiments are not presented as connector-insertion evidence; state-rollout timing excludes rendering.
- [Hafner, Yan, and Lillicrap (2025), Dreamer 4, v1](https://arxiv.org/abs/2509.24527v1): staged training and imagined policy improvement. Minecraft evidence is not presented as physical manipulation evidence.
- [Chen et al. (2026), HaWMPO, v1](https://arxiv.org/abs/2609.09941v1): learned hallucination assessment and reward softening. Proxy labels and limited evaluation size remain visible.
- [Duan et al. (2026), WorldOracle, v4](https://arxiv.org/abs/2610.18826v4): paired predicted/recorded outcomes under fixed actions. This does not establish new-policy improvement.
- [MuJoCo official computation documentation](https://mujoco.readthedocs.io/en/stable/computation/index.html), accessed 27 October 2026: contact formulations and their assumptions. The book's schematic mechanical balance is not a complete solver.

## Teaching constructions and reproduction

The cup and connector examples, original teaching diagrams, arithmetic, proposed research questions, and one-dimensional deadband experiment are teaching constructions. The code and equation define the toy result; no paper is cited as having performed that experiment. Proposed combinations of components are not attributed to a published implementation.

The public edition combines original teaching diagrams with seven paper figures whose inspected versions publish a CC BY 4.0 license. Their individual credits and license checks appear in [FIGURES.md](FIGURES.md); the other research figures are linked. No complete research PDF is redistributed. See [NOTICE.md](NOTICE.md). The official [CC BY-NC 4.0 legal code](https://creativecommons.org/licenses/by-nc/4.0/legalcode) and [MIT License](https://opensource.org/license/mit) determine the reuse terms; educational intent alone is not permission to copy external content.
