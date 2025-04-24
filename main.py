import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler
from bot.handlers import start, gita
from bot.navigation import handle_navigation

load_dotenv()

def main():
    """Run the bot"""
    application = Application.builder().token(os.getenv('TELEGRAM_TOKEN')).build()
    
    # Add handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('gita', gita))
    application.add_handler(CallbackQueryHandler(handle_navigation, pattern='^nav:'))
    
    # Start the bot
    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
