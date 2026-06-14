# Webcam Streaming Stack

**Years:** 2026  
**Role:** Systems builder  
**Tech:** Raspberry Pi, mediamtx, Tailscale, WebRTC, RTSP, Python deployment helpers

## Overview

This project solves a very specific but very common problem: how to get a camera feed from a lightweight remote device onto a phone or laptop with low latency and without turning the setup into a networking project.

The stack uses a Raspberry Pi camera source, `mediamtx` as the relay and recorder, and Tailscale for access over the internet without manual port forwarding.

## Why It Matters

Remote experiments fail for boring reasons:

- camera setup is annoying,
- the stream is not easy to access from outside the local network,
- recordings are not captured reliably,
- and the solution is often too heavy for the device at the edge.

This design keeps the edge device simple and pushes the relay and recording work to a spare laptop.

## Architecture

Pi Camera -> RTSP publisher -> laptop relay -> WebRTC in browser

That split gives a clean balance:

- the Pi handles hardware H.264 encoding,
- the laptop handles relay and recording,
- the viewer uses a browser instead of a custom client.

## What I Like About This Project

- It is small but useful.
- It is the kind of infrastructure project that makes other robotics or field-testing work easier.
- It shows a bias toward real deployment constraints instead of perfect-lab assumptions.

## Expansion Path

- Add one-click mode switching for local-only, VPN, and public-demo modes.
- Fold it into a broader remote-observation toolkit for experiments, test rigs, or workshop cameras.
- Pair it with the main portfolio site using short demo clips and setup diagrams.
