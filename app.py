import os
import logging
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# GitHub Secrets ထဲက BOT_TOKEN ကို ဖတ်ယူခြင်း
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, threaded=False)

URL_AI = "https://myanmar-future-ai.vercel.app/"
URL_WEB_1 = "https://bamarthan-one.vercel.app/"
URL_WEB_2 = "https://bamarthan.vercel.app/"
URL_APK_TV = "https://t.me/Fotmovdownloader"
URL_TK_DOWN = "https://t.me/tknowatermarkdownloader"
URL_JAV = "https://t.me/myanmajav"

def get_bfa_auto_reply_markup():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🌐 BFA AI", url=URL_AI),
        InlineKeyboardButton("🌐 BFA STREAM WEB-1", url=URL_WEB_1),
        InlineKeyboardButton("🌐 BFA STREAM WEB-2", url=URL_WEB_2),
        InlineKeyboardButton("📦 BFA STREAM APK FOR TV/BOX & MOBILE PHONE", url=URL_APK_TV),
        InlineKeyboardButton("🎬 TIKTOK VIDEO DOWNLOADER", url=URL_TK_DOWN),
        InlineKeyboardButton("🎬 JAV MMSUB (🔞+)", url=URL_JAV)
    )
    return markup

@bot.message_handler(func=lambda m: True)
def handle_bfa_pure_auto_reply(message):
    try:
        response_text = (
            "🤖 **Burmar Future AI Bot မှ ကြိုဆိုပါသည်**\n\n"
            "✨ Burmar Future AI မှ ဖန်တီးပေးထားသည်များကို Free အသုံးပြုနိုင်ပါသည်ခင်ဗျာ။\n\n"
            "👇 **Burmar Future AI Links:**"
        )
        bot.send_message(
            message.chat.id, 
            response_text, 
            parse_mode="Markdown", 
            reply_markup=get_bfa_auto_reply_markup(),
            disable_web_page_preview=True
        )
    except Exception as e: logger.error(f"Bot pure auto reply error: {e}")

if __name__ == "__main__":
    logger.info("Bot is starting with Long Polling System...")
    
    # ရှိနေနိုင်တဲ့ Webhook အဟောင်းကို ရှင်းထုတ်ခြင်း
    bot.remove_webhook()
    
    # GitHub Actions Runner ပေါ်မှာ ပိတ်မသွားဘဲ စဉ်ဆက်မပြတ် မက်ဆေ့ခ်ျဖတ်ပြီး တုံ့ပြန်နိုင်ရန် ပတ်ခိုင်းခြင်း
    bot.infinity_polling(skip_pending=True)
  
