# Lab: Inspect Local HTTP Traffic

> Category: Network Security  
> Difficulty: Beginner  
> Estimated Time: 20 minutes  
> Environment: Local workstation, Wireshark, Python 3

## Objective

Capture and inspect traffic generated between processes on the same machine. The service binds only to loopback and is not exposed to the network.

## Prerequisites

Wireshark with a loopback capture interface, Python 3, and `curl`. Capture only your own generated traffic.

## Procedure

1. In a terminal, start a local server:

   ```bash
   python -m http.server 8000 --bind 127.0.0.1
   ```

2. In Wireshark, select the loopback interface (`lo` on many Linux systems; interface naming varies) and start a capture. If loopback capture is unavailable, use another approved local capture method.
3. In a second terminal, request the local page:

   ```bash
   curl -i http://127.0.0.1:8000/
   ```

4. Stop the capture and filter with `tcp.port == 8000`.
5. Inspect the TCP handshake, HTTP request line, response status, and payload. Note that this plaintext HTTP is acceptable only for this local exercise.

## Expected Results

The capture should show a connection to `127.0.0.1:8000` and a successful HTTP response containing a directory listing. Do not expose this server beyond loopback.

## Cleanup

Stop the Python server with Ctrl+C, stop the capture, and delete any capture file if no longer needed.

## Lessons Learned

Record how interface selection, capture scope, and protocol filters affect visibility. See [Wireshark Quick Reference](../../Cheatsheets/Wireshark.md).

## Responsible Use

This exercise generates traffic only to a service bound to the local loopback address.
