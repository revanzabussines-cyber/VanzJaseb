import asyncio
from telethon import TelegramClient

# ========== CONFIG ==========
API_ID = 32237619
API_HASH = "69773d4b41c196f0334ea4a4556ea929"
SESSION_NAME = "vanz_userbot"

# Target pengiriman
TARGETS = ["Jualan_Masker"]

# Interval kirim (detik)
INTERVAL_SECONDS = 300  # 300 detik = 5 menit
# Ubah ke 60 untuk 1 menit, atau 30 untuk 30 detik

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
# ============================


async def send_loop():
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    await client.start()
    print("Userbot aktif. Mulai auto-kirim...")

    while True:
        for target in TARG
