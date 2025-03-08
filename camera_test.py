from picamera2.outputs import FfmpegOutput

stream = FfmpegOutput("-f mpegts udp://10.230.64.26:8000")