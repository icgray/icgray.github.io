# Designing Sensor-Rich Robots

State estimation gets presented as a software problem, but a lot of the real difficulty lives in hardware layout.

Where the IMU sits, how the LiDAR is mounted, whether cables shift, how vibration enters the frame, and whether the optical path stays clean all change the quality of the data before a single filter runs. I learned this in swarm robotics and later in racecar experiments: mechanical design decisions quietly shape algorithm performance.

## The data is born before the filter sees it

A Kalman filter can only do so much with a signal that was already compromised at the connector. A few examples from my own builds:

- **Mounting and vibration.** An IMU rigidly coupled to a motor mount picks up structural resonance that looks like real acceleration. Moving it, isolating it, or even just choosing a stiffer plate can do more for the estimate than retuning the process noise.
- **Cable strain.** On the collaborative load-transport sensor, early prototypes damaged wires during assembly, which meant intermittent channels that no calibration could rescue. The fix was a better housing, not better code.
- **Sensor placement geometry.** Two of the same load cell placed symmetrically gave a second independent contribution per axis and a path toward torque estimation. The information came from the layout, not from a cleverer equation.

## The tradeoff I keep coming back to

The fastest way to improve a robot is often not a more complicated estimator. It is a better physical system feeding that estimator cleaner information. A noisier sensor in the right place usually beats a better sensor in the wrong one.

That is one reason I like interdisciplinary work. If you can move freely between the CAD model, the wiring, and the estimator, you can spend your effort wherever the real bottleneck is, instead of forcing every problem to be a software problem because software is the only layer you are allowed to touch.
