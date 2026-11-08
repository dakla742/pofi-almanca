import asyncio, os
import edge_tts

os.makedirs("out", exist_ok=True)
LINES = [
    ("tr1", "Pofi aç. Hem de çok aç.", "tr-TR-EmelNeural"),
    ("tr2", "Pofi'nin bununla hiçbir ilgisi yok.", "tr-TR-EmelNeural"),
    ("de1", "Der Apfel.", "de-DE-KatjaNeural"),
]

async def main():
    for name, text, voice in LINES:
        await edge_tts.Communicate(text, voice, rate="-10%").save(f"out/{name}.mp3")

asyncio.run(main())
