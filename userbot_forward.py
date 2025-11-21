from telethon import TelegramClient, events

# ==========================
# CONFIG USERBOT
# ==========================

API_ID = 32237619  # <-- API ID lu
API_HASH = "69773d4b41c196f0334ea4a4556ea929"  # <-- API HASH lu

SESSION_NAME = "vanz_userbot"   # nama file session, bebas

# Channel / grup Sumber (tempat lu posting dulu)
SOURCE = "VanzDisscussion"      # bisa "VanzDisscussion" atau link "https://t.me/VanzDisscussion"

# Target forward (boleh banyak)
TARGETS = [
    "Jualan_Masker",            # contoh, bisa grup / channel / user
    # "NamaTargetLain",
]

# ==========================


client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


@client.on(events.NewMessage(chats=SOURCE))
async def handler(event):
    """
    Tiap ada pesan baru di SOURCE -> auto forward ke semua TARGETS.
    """
    print("Pesan baru terdeteksi, forwarding...")

    for target in TARGETS:
        try:
            await client.forward_messages(entity=target, messages=event.message)
            print(f"Berhasil forward ke {target}")
        except Exception as e:
            print(f"Gagal forward ke {target}: {e}")


def main():
    print("Start userbot...")
    # Pertama kali jalan akan minta nomor HP & kode verifikasi di terminal
    client.start()
    me = client.loop.run_until_complete(client.get_me())
    print(f"Userbot login sebagai: {me.first_name} (@{me.username})")
    print(f"Listening dari: {SOURCE}")
    print("Waiting for new messages...")
    client.run_until_disconnected()


if __name__ == "__main__":
    main()
