from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from .core import GitaBot

bot = GitaBot()

async def handle_navigation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle inline button presses"""
    query = update.callback_query
    await query.answer()
    
    _, chapter, verse_ref = query.data.split(':')
    chapter = int(chapter)
    
    # Get the verse text
    text = bot._format_verse_text(chapter, verse_ref)
    
    # Update buttons
    buttons = []
    nav = bot.get_navigation_buttons(chapter, verse_ref)
    
    if nav['prev']:
        prev_ch, prev_v = nav['prev']
        buttons.append(
            InlineKeyboardButton("◀ Previous", callback_data=f"nav:{prev_ch}:{prev_v}")
        )
    
    if nav['next']:
        next_ch, next_v = nav['next']
        buttons.append(
            InlineKeyboardButton("Next ▶", callback_data=f"nav:{next_ch}:{next_v}")
        )
    
    reply_markup = InlineKeyboardMarkup([buttons]) if buttons else None
    
    await query.edit_message_text(
        text=text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )
