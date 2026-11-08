import subprocess
from make_voice import LINES

TOTAL = 33.2
inputs, filt = [], []
for i, (name, _t, _v, start) in enumerate(LINES):
    inputs += ["-i", f"out/{name}.mp3"]
    ms = int(start * 1000)
    filt.append(f"[{i}:a]adelay={ms}|{ms}[a{i}]")
mix = "".join(f"[a{i}]" for i in range(len(LINES)))
filt.append(f"{mix}amix=inputs={len(LINES)}:normalize=0[aout]")

subprocess.run(["ffmpeg", "-y", *inputs, "-filter_complex", ";".join(filt),
                "-map", "[aout]", "-t", str(TOTAL), "out/voice.m4a"], check=True)
subprocess.run(["ffmpeg", "-y", "-framerate", "24", "-i", "frames/f%05d.jpg",
                "-i", "out/voice.m4a", "-c:v", "libx264", "-pix_fmt", "yuv420p",
                "-crf", "20", "-c:a", "aac", "-t", str(TOTAL),
                "-movflags", "+faststart", "out/video.mp4"], check=True)
