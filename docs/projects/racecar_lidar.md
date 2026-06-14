# Racecar LiDAR Benchmarking

**Years:** 2024-2026  
**Role:** Research engineer  
**Tech:** Python, NumPy, SciPy, OpenCV, LiDAR parsing, AprilTags, OptiTrack, ESP32, MuJoCo

## Overview

This project started as a racecar localization problem and turned into a benchmark suite.

I built an RC Ackermann-drive platform and compared several 2D LiDAR odometry approaches against real ground truth from AprilTags and motion capture. Instead of treating one algorithm as the answer, I set up a workflow where multiple pipelines could be evaluated on the same sessions with the same logs, metrics, and plots.

The result is closer to an experimental framework than a single script.

## Why It Matters

- Small autonomous vehicles do not have the sensing budget of full-size platforms.
- Sparse 2D LiDAR is attractive, but it becomes fragile when the platform turns hard, slides, or leaves nice indoor assumptions.
- Controller evaluation is only meaningful if the localization story is honest.

## What I Built

- A logging and benchmarking pipeline around LiDAR, dual IMUs, AprilTags, and OptiTrack exports.
- Multiple odometry methods, including curvature-based ICP, Shi-Tomasi feature extraction on rasterized scans, and polynomial or segment-matching approaches.
- Session-level comparison tooling to score drift, trajectory quality, and failure modes across runs.
- Visualization outputs for trajectory overlays, summary plots, and per-session diagnostics.

## Technical Notes

From the thesis repository:

- 130 motion-capture telemetry files were recorded.
- 108 had matching LiDAR logs.
- 33 sessions had enough real vehicle motion to be useful for the benchmark.

The strongest idea in this work is not just feature extraction. It is the insistence on comparing methods under the same experimental conditions:

- identical session matching,
- explicit ground-truth alignment,
- consistent SE(2) accumulation,
- outlier rejection at the step level,
- and generated summary plots instead of anecdotal claims.

## Representative Methods

### Shi-Tomasi ICP

Rasterize each scan to an image, detect corners, back-project them to LiDAR points, and estimate motion from those matched features. This turned out to be robust on long sessions where sparse structure still gave consistent corners.

### Poly-RANSAC

Cluster the scan, fit local geometry, match segments, and estimate SE(2) transforms from higher-level structure rather than raw points. This produced strong short and medium run accuracy but can accumulate mismatch over long runs.

### Fused Method

Use segment structure where it helps most and image-derived corners where translation estimation is more stable. This is the kind of hybrid approach I find most realistic in messy robotics work.

## What This Project Says About Me

- I care about the pipeline around an algorithm, not just the algorithm.
- I like experiments with enough structure that the results can survive scrutiny.
- I am comfortable moving between sensors, code, data cleaning, simulation, and physical platform constraints.
