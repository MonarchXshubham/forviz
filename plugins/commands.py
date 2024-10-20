import os
import sys
import pytz
import asyncio 
from database import db, mongodb_version
from config import Config, temp
from platform import python_version
from translation import Translation
from datetime import datetime
from pyrogram import Client, filters, enums, __version__ as pyrogram_version
from pyrogram.types import *
TIMEZONE = "Asia/Kolkata"

main_buttons = [[
        InlineKeyboardButton('🏡', callback_data='start'),
        InlineKeyboardButton('⚙️', callback_data='settings#main'),
        InlineKeyboardButton('🆘', callback_data='how_to_use'),
        InlineKeyboardButton('🖥', callback_data='status'),
        InlineKeyboardButton('⚡️', callback_data='about')
        ],[
        InlineKeyboardButton('🦋 ᴜᴘᴅᴀᴛᴇs ', url='https://t.me/vr_unreal'),
        InlineKeyboardButton(' sᴜᴘᴘᴏʀᴛ ✨', url='https://t.me/vr_support')
        ],[
        InlineKeyboardButton('🛠️ ʜᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton(' ᴀʙᴏᴜᴛ ⚡️', callback_data='about')
        ],[
        InlineKeyboardButton('🛠️ sᴇᴛᴛɪɴɢs ⚙️', callback_data='settings#main')
        ]]
#===================Start Function===================#

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    user = message.from_user
    if Config.FORCE_SUB_ON:
        # Check if the user has joined the force subscription channel
        try:
            member = await client.get_chat_member(Config.FORCE_SUB_CHANNEL, user.id)
            if member.status == "kicked":
                await client.send_message(
                    chat_id=message.chat.id,
                    text="You are banned from using this bot.",
                )
                return
        except:
            # Send a message asking the user to join the channel
            join_button = [
                [InlineKeyboardButton("Join Channel", url=f"{Config.FORCE_SUB_CHANNEL}")],
                [InlineKeyboardButton("↻ Tʀʏ Aɢᴀɪɴ", url=f"https://t.me/{client.username}?start=start")]
            ]
            await client.send_message(
                chat_id=message.chat.id,
                text="Please join our channel to use this bot.",
                reply_markup=InlineKeyboardMarkup(join_button)
            )
            return

    if not await db.is_user_exist(user.id):
        await db.add_user(user.id, message.from_user.mention)
        # Log the new user to the log channel
        log_channel = Config.LOG_CHANNEL # Replace with your log channel ID
        await client.send_message(
            chat_id=log_channel,
            text=f"#NewUser\n\nIᴅ - {user.id}\nNᴀᴍᴇ - {message.from_user.mention}"
        )

    reply_markup = InlineKeyboardMarkup(main_buttons)
    current_time = datetime.now(pytz.timezone(TIMEZONE))
    curr_time = current_time.hour        
    if curr_time < 12:
        gtxt = "ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 🌞" 
    elif curr_time < 17:
        gtxt = "ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ 🌗" 
    elif curr_time < 21:
        gtxt = "ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ 🌘"
    else:
        gtxt = "ɢᴏᴏᴅ ɴɪɢʜᴛ 🌑"
    await client.send_photo(
        chat_id=message.chat.id,
        photo=Config.PICS,
        reply_markup=reply_markup,
        caption=Translation.START_TXT.format(message.from_user.mention, gtxt)
    )

#==================Restart Function==================#

@Client.on_message(filters.private & filters.command(['restart']) & filters.user(Config.BOT_OWNER_ID))
async def restart(client, message):
    msg = await message.reply_text(
        text="<i>Trying to restarting.....</i>"
    )
    await asyncio.sleep(5)
    await msg.edit("<i>Server restarted successfully ✅</i>")
    os.execl(sys.executable, sys.executable, *sys.argv)
    
#==================Callback Functions==================#

@Client.on_callback_query(filters.regex(r'^help'))
async def helpcb(bot, query):
    await query.message.edit_text(
        text=Translation.HELP_TXT,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('🏡', callback_data='start'),
            InlineKeyboardButton('⚙️', callback_data='settings#main'),
            InlineKeyboardButton('🆘', callback_data='how_to_use'),
            InlineKeyboardButton('🖥', callback_data='status'),
            InlineKeyboardButton('⚡️', callback_data='about')
            ],[
            InlineKeyboardButton('🛠️ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ 🛠️', callback_data='how_to_use')
            ],[
            InlineKeyboardButton('⚙️ sᴇᴛᴛɪɴɢs ⚙️', callback_data='settings#main'),
            InlineKeyboardButton('📊 sᴛᴀᴛᴜs 📊', callback_data='status')
            ],[
            InlineKeyboardButton('⛔ ʙᴀᴄᴋ', callback_data='back')
            ]]
        ))

@Client.on_callback_query(filters.regex(r'^how_to_use'))
async def how_to_use(bot, query):
    await query.message.edit_text(
        text=Translation.HOW_USE_TXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⛔ Back', callback_data='help')]]),
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex(r'^back'))
async def back(bot, query):
    reply_markup = InlineKeyboardMarkup(main_buttons)
    current_time = datetime.now(pytz.timezone(TIMEZONE))
    curr_time = current_time.hour        
    if curr_time < 12:
        gtxt = "ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 🌞" 
    elif curr_time < 17:
        gtxt = "ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ 🌗" 
    elif curr_time < 21:
        gtxt = "ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ 🌘"
    else:
        gtxt = "ɢᴏᴏᴅ ɴɪɢʜᴛ 🌑"
    await query.message.edit_media(
        media=InputMediaPhoto(
        media=Config.PICS,
        caption=Translation.START_TXT.format(query.from_user.mention, gtxt)),
        reply_markup=reply_markup)
        
@Client.on_callback_query(filters.regex(r'^about'))
async def about(bot, query):
    await query.message.edit_media(
        media=InputMediaPhoto(
        media="https://vault.pictures/p/4add4cab289149138c7f5ea4ec9d4813",
        caption=Translation.ABOUT_TXT),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⛔ Back', callback_data='back')]])
        )

@Client.on_callback_query(filters.regex(r'^status'))
async def status(bot, query):
    users_count, bots_count = await db.total_users_bots_count()
    total_channels = await db.total_channels()
    await query.message.edit_text(
        text=Translation.STATUS_TXT.format(users_count, bots_count, temp.forwardings, total_channels, temp.BANNED_USERS ),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⛔ Back', callback_data='help')]]),
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
    )
@Client.on_message(filters.private & filters.command(['stats']) & filters.user(Config.BOT_OWNER_ID))
async def stats(client, message):
    users_count, bots_count = await db.total_users_bots_count()
    total_channels = await db.total_channels()
    await client.send_message(
        chat_id=message.chat.id,
        text=Translation.STATUS_TXT.format(users_count, bots_count, temp.forwardings, total_channels, temp.BANNED_USERS )
    )
