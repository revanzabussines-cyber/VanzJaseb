import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = 36235512
API_HASH = "e4e449529f535e74ecf2153e740e888e"

# ambil dari Railway Variables
SESSION_STRING = os.getenv("SESSION_STRING")

# TARGET dulu ke 'me' (Saved Messages) buat test
TARGETS = ["https://t.me/Jualan_Masker"]

# interval kirim (detik)
INTERVAL_SECONDS = 60  # 300 = 5 menit, boleh ganti 60 / 30

PROMO_TEXT = """
🔥 PROMO GILA VANZSHOP.ID 🔥

💎 Canva Lifetime
Invite Only → Rp 10.000
Head (Full Access) → Rp 50.000

🎬 CapCut Premium 1 Bulan (Garansi Aktif)
→ Rp 2.900

🎧 Spotify Premium 1 Bulan
→ Rp 4.000

📺 YouTube Premium 1 Bulan
→ Rp 3.000

🧠 Gemini VEO 3 (1 Tahun + 2TB Google Drive)
→ Rp 10.000

🎥 Alight Motion 1 Tahun (Private Full Access)
→ Rp 2.000

📺 Viu Lifetime (Full Access)
→ Rp 2.000

🎞️ Bstation 1 Tahun (Premium Access)
→ Rp 10.000

🎬 MovieBox Active s.d. 2027
→ Rp 17.000

🛡️ ExpressVPN / HMA VPN (1 Bulan)
→ Rp 5.000

🍿 Netflix Premium Sharing
1P1U → Rp 12.000
1P2U → Rp 22.000

---

⚡ Auto Order: @VanzShopBot
💬 Info: @VanzDisscusion
👑 Owner: @VanzzSkyyID

🌐 VanzShop.ID
"""

async def send_loop():
    if not SESSION_STRING:
        raise RuntimeError("SESSION_STRING belum di-set di Railway Variables")

    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
    await client.start()
    me = await client.get_me()
    print(f"Login sebagai: {me.first_name} (@{me.username})")
    print(f"Target: {TARGETS}")
    print(f"Interval: {INTERVAL_SECONDS} detik\n")

    while True:
        print("Mengirim promo...")
        for target in TARGETS:
            try:
                await client.send_message(target, PROMO_TEXT)
                print(f"✔ Terkirim ke {target}")
            except Exception as e:
                print(f"✖ Gagal kirim ke {target}: {e}")

        print(f"Tunggu {INTERVAL_SECONDS} detik...\n")
        await asyncio.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    asyncio.run(send_loop())
