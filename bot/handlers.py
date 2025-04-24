from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from .core import GitaBot

bot = GitaBot()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message"""
    welcome = (
        "🕉 *Welcome to Bhagavad Gita As It Is Bot* 🕉\n\n"
        "This bot provides verses from the original 1972 Macmillan edition.\n\n"
        "To begin, use:\n`/gita <chapter> <verse>`\n\n"
        "Example: `/gita 2 13` or `/gita 7 1-3`"
    )
    await update.message.reply_text(welcome, parse_mode='Markdown')

async def gita(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /gita command"""
    if len(context.args) < 2:
        await update.message.reply_text("Usage: /gita <chapter> <verse>")
        return
    
    try:
        chapter = int(context.args[0])
        verse = context.args[1]
    except ValueError:
        await update.message.reply_text("Chapter must be a number (1-18)")
        return
    
    is_valid, verse_ref = bot._validate_verse(chapter, verse)
    if not is_valid:
        await update.message.reply_text(f"Invalid verse: {verse_ref}")
        return
    
    # Format the verse text
    text = bot._format_verse_text(chapter, verse_ref)
    
    # Create navigation buttons
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
    
    await update.message.reply_text(
        text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )
