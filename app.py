import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define the start command handler
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! Send me a GitHub repository link, and I will provide you with a ZIP download link.')

# Define the handler for processing text messages
async def handle_message(update: Update, context: CallbackContext) -> None:
    link = update.message.text
    if 'github.com' in link:
        download_link = f"{link}/archive/refs/heads/master.zip"
        caption = (
            f"📂 GitHub Repository ZIP File\n\n"
            f"[Click here to download ZIP file]({download_link})\n\n"
            f"👨‍💻 Developer: [Md. Shahriar Ahmed Shovon](https://t.me/FisherMan_Earn)"
        )
        
        inline_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Download ZIP 📥", url=download_link)],
            [InlineKeyboardButton("Developer 👨‍💻", url="https://t.me/FisherMan_Earn")]
        ])
        
        try:
            await context.bot.send_document(
                chat_id=update.message.chat_id, 
                document=download_link, 
                caption=caption, 
                parse_mode="Markdown", 
                reply_markup=inline_keyboard
            )
        except Exception as e:
            logger.error(f"Error: {e}")
            await update.message.reply_text(
                "❌ Unable to send the document. Please use the button below to download.",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Download ZIP 📥", url=download_link)]])
            )
    else:
        await update.message.reply_text("Please send a valid GitHub repository link.")
    
    # Prompt for another link
    await update.message.reply_text("Send me another GitHub repository link, and I will provide you with a ZIP download link.")

def main() -> None:
    # Insert your Bot's token here
    token = ('7217822006:AAG69nqMhQ-UTyHFLOJ1zqxADC9UPq_mOV8')
    
    # Create the Application and pass it your bot's token
    application = Application.builder().token(token).build()
    
    # Register the handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
