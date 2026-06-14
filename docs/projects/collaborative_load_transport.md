# Sensing for Collaborative Load Transport

**Years:** 2020-2021  
**Role:** Capstone team member, mechanical and controls contributor  
**Tech:** Strain-based load cells, Arduino, analog filtering, linear regression calibration, 3D printing, CAD

## Overview

This capstone project was about a practical sensing problem for collaborative robotics: how do you give a small robot enough force awareness to carry a large or delicate object with other robots, without using an expensive industrial force sensor?

Our answer was a low-cost multi-axis sensor built from four off-the-shelf 1D strain-based load cells mounted in a symmetric 3D-printed structure. By combining their readings, we could estimate in-plane force components and, in principle, torque as well.

The target application was collaborative transport of delicate parts, especially large uncured composite components where excessive local force or deformation would be unacceptable.

## The Problem

Multi-axis force sensors are useful, but they are expensive and often mismatched to small-robot research budgets. At the same time, collaborative transport needs more than simple obstacle avoidance:

- each robot has to react to the load,
- the group has to compensate for uneven forces,
- and the sensing has to be cheap enough to replicate across multiple robots.

That made cost a real design constraint, not a side note.

## Design Approach

The final concept used four single-axis load cells in a square arrangement instead of a purpose-built 2-axis commercial sensor.

That layout mattered for three reasons:

- it preserved rotational symmetry,
- it gave two sensing contributions per axis rather than one,
- and it created a path toward torque estimation by comparing the sensor responses around the structure.

The full sensing chain looked like this:

1. Force applied to the assembly.
2. Strain gauges in the 1D load cells produced small analog voltage changes.
3. Analog low-pass filtering reduced noise and aliasing risk.
4. Amplification raised the signals to usable levels.
5. An Arduino sampled and debounced the signals.
6. A linear calibration model mapped voltages to force components.

## What We Built

- A multi-load-cell mechanical assembly with a robot-mountable form factor.
- A 3D-printed housing and baseplate iterated to reduce wire damage and improve assembly.
- Analog filtering and amplification stages for each sensor channel.
- Arduino-based acquisition code for multi-channel sampling.
- A calibration workflow using linear regression rather than a full analytical closed-form model.

## Why The Calibration Strategy Was Reasonable

The mapping from four raw voltage channels to `Fx`, `Fy`, and torque was complicated enough that a purely analytical model would have taken too long for the capstone timeline and still needed empirical correction.

So the project used a numerical calibration approach:

- apply known loads,
- compute expected force components from geometry and orientation,
- record voltage outputs,
- fit a linear model from voltages to force components.

That was a pragmatic engineering decision. It kept the computation light enough for real-time use while still grounding the model in measured data.

## Validation

The project used several test modes:

- **1D static loading** for basic sanity checks and calibration confidence.
- **2D static loading** to verify decomposition of force into x and y components.
- **Dynamic pendulum loading** to compare measured forces against a simple analytical dynamic model.
- **Application-style tests** to connect the sensor back to the collaborative transport use case.

From the original report:

- static RMS error reached about **6.61% in x** and **9.63% in y** on the later prototype,
- an earlier version achieved errors as low as **0.42% in x** and **1.02% in y**,
- sensor resolution was reported at **0.01 N**,
- and the sensing pipeline produced a data point every **40 ms** in the demonstrated implementation.

Those numbers matter because they show the project was not just a concept model. It was measured, calibrated, and challenged against expected loads.

## What I Still Like About This Project

- It solved a real robotics problem under budget constraints.
- It combined mechanical design, signal conditioning, embedded code, and modeling in one system.
- It used theory where it helped and empirical calibration where that was the smarter choice.
- It was one of the early projects that pushed me toward cross-disciplinary engineering instead of staying inside a single lane.

## Media

- Original demo video: [YouTube demo](https://youtu.be/JSwahNZB86g)
- Original final report PDF: [Download the full report](../assets/collaborative-load-transport-final-report.pdf)
- Full report as a webpage: [Report archive page](collaborative_load_transport_report.md)

Two image URLs from the original post still resolve through Blogger hosting, but most of the inline report figures were linked to old local Office temp files and did not survive the Blogspot export cleanly. Once you find the original figures, this page should get:

- one hero image of the prototype,
- one CAD or assembly image,
- one block diagram of the sensing stack,
- and one results plot from the static or pendulum validation tests.

## Source Note

This page is a cleaned-up reconstruction of your December 2021 Blogspot capstone post, rewritten into portfolio form so the core engineering story is visible without the report appendix structure.

## Archive

The full original document is now preserved on this site as a PDF exactly so the project can stay true to its original 2021 form:

- [Collaborative Load Transport Final Report (PDF)](../assets/collaborative-load-transport-final-report.pdf)
- [Collaborative Load Transport Report Archive Page](collaborative_load_transport_report.md)

The archive page keeps the original report structure, extracted figures, appendices, code excerpts, and class-report formatting on the website itself. This project page is the shorter portfolio interpretation of the same work.
