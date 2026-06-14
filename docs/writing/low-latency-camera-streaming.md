# Low-Latency Camera Streaming For Experiments

Getting a camera online sounds easy until the camera is remote, the network is annoying, and the viewer is on a phone.

The webcam streaming project came out of that exact situation. I wanted a setup that was simple at the edge, viewable from anywhere I had access, and low-latency enough to be useful for live monitoring. The answer was not a giant custom stack. It was a clean split of responsibilities: Pi for capture, laptop for relay and recording, browser for viewing, and Tailscale for access.

## Why the split matters

The instinct is to make the camera device do everything. That is also how you end up with a Raspberry Pi struggling to encode, serve, record, and survive a flaky network all at once. Separating the roles keeps each piece doing the thing it is actually good at:

- the **Pi** handles hardware H.264 encoding and publishes over RTSP, which is light enough that the edge device stays reliable,
- a **spare laptop** runs `mediamtx` as the relay and recorder, where CPU and disk are cheap,
- the **browser** consumes a WebRTC stream, so the viewer needs no special client,
- **Tailscale** provides access across networks without manual port forwarding or exposing anything to the public internet.

## Latency is mostly an architecture decision

Most of the latency people complain about does not come from the codec. It comes from buffering, protocol hops, and re-encoding. By keeping hardware encoding on the Pi and letting the relay pass the stream through rather than transcode it, the end-to-end delay stays low enough to actually react to what you are watching.

I like projects like this because they remove friction for everything else. A camera you can trust to be up, accessible, and recording turns "set up the stream again" into a non-event, and good infrastructure makes every future experiment cheaper.
