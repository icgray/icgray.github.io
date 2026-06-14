# Shot Peening ML

**Years:** 2024-2025  
**Role:** ML engineer and software developer  
**Tech:** Python, PyTorch, Tkinter, NumPy, Matplotlib, test automation, CI

## Overview

Shot peening is a good example of a workflow where simulation is valuable but iteration speed is painful.

This project uses machine learning to predict deformation from shot peening parameters and geometry so engineers can explore outcomes quickly instead of waiting on full finite-element runs every time. The public-facing strength of the project is not just the model. It is the whole toolchain around it:

- dataset generation,
- model training,
- visualization,
- a GUI for non-ML users,
- and tests that make the project feel like software instead of a one-off notebook.

## Core Idea

Replace repeated high-cost simulation passes with a fast approximation layer that is useful for screening, comparison, and early process tuning.

That matters because many engineering teams do not need the final answer first. They need a fast way to narrow the design space before spending expensive simulation time.

## What The Repository Shows

- A structured Python project with `pyproject.toml`, tests, and CI.
- A GUI entry point for loading models, running predictions, and visualizing results.
- A PyTorch model intended to learn deformation behavior from simulated examples.
- Visualization utilities that make the results understandable for engineering users.

## Why It Is A Strong Portfolio Piece

- It connects mechanical engineering directly to ML.
- It focuses on workflow acceleration, which is a real engineering value.
- It treats usability as part of the technical solution.
- It shows comfort with both research-style experimentation and software packaging discipline.

## Next Step For The Public Version

The strongest upgrade for this page will be screenshots and one concrete case study:

1. input recipe,
2. model prediction,
3. comparison against simulation,
4. decision made faster because of the model.

That would turn an already solid technical project into a very convincing portfolio story.
