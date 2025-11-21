import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

# ========== CONFIG ==========

# Ambil token dari env BOT_TOKEN (lebih aman)
BOT_TOKEN = os.getenv("BOT_TOKEN", "ISI_TOKEN_KALO_MAU_HARDCODE")

# Username channel sumber TANPA @
SOURCE_USERNAME = "VanzDisscussion"

# Daftar target forward (bisa channel / grup / user) TANPA @
# Misal: ["VanzForwardCenter", "VanzBackupChannel"]
TARGET_USERNAMES = [
    "Jualan_Masker"  # contoh, ganti sesuai kebutuhan lu
]

# ============================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def forward_from_source_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Auto-forward semua post dari channel sumber ke semua target."""
    channel_post = update.channel_post
    if not channel_post:
        return

    chat = channel_post.chat
    channel_username = (chat.username or "").lower()

    # Cek: ini bener dari channel sumber kita nggak?
    if channel_username != SOURCE_USERNAME.lower():
        return

    logger.info("Dapet post baru dari @%s, mulai forward...", channel_username)

    # Kirim ke semua target
    for target_username in TARGET_USERNAMES:
        target_username = target_username.strip()
        if not target_username:
            continue

        try:
            await channel_post.forward(chat_id=f"@{target_username}")
            logger.info("Berhasil forward ke @%s", target_username)
        except Exception as e:
            logger.error("Gagal forward ke @%s: %s", target_username, e)


async def on_startup(app):
    logger.info("Bot jaseb forward sudah jalan, nunggu post dari @%s ...", SOURCE_USERNAME)


def main():
    # Cek token
    if not BOT_TOKEN or BOT_TOKEN == "ISI_TOKEN_KALO_MAU_HARDCODE":
        raise RuntimeError("BOT_TOKEN belum di-set. Set di env Railway atau hardcode di main.py")

    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handler global: kita cek sendiri apakah itu dari channel sumber
    application.add_handler(MessageHandler(filters.ALL, forward_from_source_channel))

    application.post_init = on_startup

    # Run polling (non-stop)
    application.run_polling(close_loop=False)


if __name__ == "__main__":
    main()
