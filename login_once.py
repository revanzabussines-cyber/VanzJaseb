from telethon import TelegramClient

API_ID = 32237619
API_HASH = "69773d4b41c196f0334ea4a4556ea929"
SESSION_NAME = "vanz_userbot"

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def main():
    await client.start()
    me = await client.get_me()
    print("Login sukses sebagai:", me.first_name, f"(@{me.username})")
    print("Session tersimpan ke file:", SESSION_NAME + ".session")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
