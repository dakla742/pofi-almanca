import asyncio, os
import edge_tts

os.makedirs("out", exist_ok=True)
TR = "tr-TR-EmelNeural"
DE = "de-DE-KatjaNeural"

# (dosya adı, metin, ses, videodaki başlangıç saniyesi)
LINES = [
    ("v0", "Merhaba! Bugün Almancada yeni bir kelime öğreniyoruz.", TR, 0.4),
    ("v1", "Gece yarısı. Mutfak sessiz.", TR, 4.2),
    ("v2", "Pofi aç. Hem de çok aç.", TR, 8.2),
    ("v3", "Ve elma... tam karşısında.", TR, 12.4),
    ("v4", "Pofi'nin bununla hiçbir ilgisi yok.", TR, 16.8),
    ("v5", "Peki elmaya Almancada ne denir?", TR, 21.0),
    ("v6", "Der Apfel.", DE, 24.0),
    ("v7", "Bir daha dinle.", TR, 26.4),
    ("v8", "Der Apfel.", DE, 28.2),
    ("v9", "Yarın görüşürüz.", TR, 30.4),
]

async def main():
    for name, text, voice, _start in LINES:
        rate = "-25%" if voice == DE else "-10%"
        await edge_tts.Communicate(text, voice, rate=rate).save(f"out/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
