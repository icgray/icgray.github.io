# Crack Detection Pipeline

**Years:** 2026  
**Role:** ML engineer and tooling developer  
**Tech:** Python, PyTorch, transfer learning, evaluation tooling, Kaggle datasets

## Overview

This project is a practical computer-vision pipeline for identifying cracks and surface defects in concrete and metal imagery.

The interesting part is not just model training. It is the full path from data acquisition to reproducible evaluation:

- dataset download scripts,
- configurable training,
- scratch and transfer-learning baselines,
- saved checkpoints,
- confusion-matrix reporting,
- and lightweight inference for new images.

## Why I Built It

Defect detection is a useful bridge between research code and industrial engineering. It forces good habits:

- you need a reliable dataset story,
- you need metrics that mean something,
- and you need a workflow that can be rerun without guessing what changed.

## System Design

- `config.yaml` holds dataset, model, and training settings.
- `dataset.py` defines transforms and train/validation/test splits.
- `model.py` supports both a custom CNN and ResNet-based transfer learning.
- `train.py`, `evaluate.py`, and `predict.py` make the repository usable as a pipeline rather than a notebook-only experiment.

## What Makes It Portfolio-Worthy

- It shows I can structure ML work as software, not just analysis.
- It keeps the code approachable for someone who wants to swap datasets or architectures.
- It includes both from-scratch and pre-trained model paths, which is the kind of tradeoff real teams actually make.

## Next Improvements

- Add sample results and confusion-matrix images directly to the public project page.
- Publish benchmark numbers for the concrete and metal tasks.
- Extend the same pattern to other inspection problems where a fast baseline is more useful than an overbuilt stack.
