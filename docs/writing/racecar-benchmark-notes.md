# Racecar Benchmark Notes

Most robotics demos do not fail because the math is impossible. They fail because the pipeline around the math is weak.

My racecar work forced that lesson early. It was not enough to get one LiDAR odometry method to look good on one run. I needed to know which method held up across different sessions, different trajectories, and different kinds of drift. That meant building a benchmark, not just an algorithm.

The useful shift was moving from "can I estimate motion from this scan?" to "how do I compare methods under the same conditions?" Once that became the goal, the work naturally expanded: log matching, AprilTag alignment, motion-capture imports, trajectory plots, outlier rejection, and summary metrics all mattered as much as the feature extraction itself.

## What honest comparison actually required

The hard part was not writing a second odometry method. It was making sure two methods were being judged on exactly the same evidence.

- **Session matching.** I recorded 130 motion-capture telemetry files; 108 had matching LiDAR logs, and only 33 had enough real vehicle motion to be worth scoring. A benchmark that quietly includes near-stationary runs flatters every method equally and tells you nothing.
- **Ground-truth alignment.** AprilTags and OptiTrack live in their own frames. Until those are aligned into a common SE(2) reference, a "good" trajectory is just a good-looking shape pointed the wrong way.
- **Consistent accumulation.** Every method had to integrate motion the same way, with the same outlier rejection at the step level, so that one pipeline was not silently getting a smoothing advantage.

## What surprised me

The method that looked best on a single clean run was rarely the most robust one across all 33 sessions. Shi-Tomasi corner tracking on rasterized scans held up on long runs where sparse structure still produced stable corners, while segment-fitting approaches were sharper on short runs but accumulated mismatch over distance. You only see that tradeoff if you refuse to cherry-pick the session.

That is the part of robotics I enjoy most. Good experiments create a fair fight between ideas, and the result is something you can actually defend instead of a screenshot that happened to go well.
