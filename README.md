# Your task

This project was originally used for my thesis and abandoned halfway due to low priority. Therefore, I look forward to your suggestions for completing this implementation. The basic structure is ready. You just need to validate and test all components and reproduce the results of the original work. As a tip, I would definitely start with the MixtureOfExperts model and compare it to the original implementation. (My suggestion would be to leave out the batch normalization for the time being and only integrate it again when all other sources of error have been eliminated). Please read the appendix of the original paper, where most of the implementation details are hidden. Thank you very much for your help! I am already looking forward to your PRs :)).

Note: This project is still WIP. Benchmarks and further details will be added soon.
# PyTorch implementation Dynamics-Aware Discovery of Skills (DADS).
The ``dads-torch`` repository contains all modules needed for the implementation of [DADS](https://arxiv.org/abs/1907.01657).
In addition, all routines for off-policy training and zero-shot execution in MujoCo environments are supported.
The RL algorithm SAC used here is a modification of the implementation from [pranz24](https://github.com/pranz24/pytorch-soft-actor-critic).

### Installation
Just clone the repository and run ``pip`` with the needed requirements. Note that a valid MuJoCo 2.1.0 installation is required.

    git clone https://github.com/freiberg-roman/dads-torch.git
    pip install -e ".[dev]"

To test your installation, run

    python -m pytest tests/

### Run experiments
Change the required test point directory in the ``off_policy.yaml`` file and run

    python -m dads.main.main mode=dads_train

then change the directory in the ``zero_shot.yaml`` file to the required directory containing the trained networks and
execute

    python -m dads.main.main mode=dads_eval

to evaluate your networks in a concrete environment. If you are familiar with Hydra, you can also manipulate all entries from the command line :)
