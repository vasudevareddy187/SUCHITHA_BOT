 from pyrogram import filters , Client 
 from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message   
 import requests 
 @Client.on_message(filters.command("write")) 
 async def handwrite(_, message: Message): 
     if message.reply_to_message: 
         text = message.reply_to_message.text 
     else: 
         text =message.text.split(None, 1)[1] 
     m =await message.reply_text( "`Please wait...,\n\nWriting your text...`") 
     write = requests.get(f"https://apis.xditya.me/write?text={text}").url 
  
     caption = f""" 
 sᴜᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘 
 ✨ **ᴡʀɪᴛᴛᴇɴ ʙʏ :** [{BOT_NAME}](https://t.me/{BOT_USERNAME}) 
 🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention} 
 """ 
     await m.delete() 
     await message.reply_photo(photo=write,caption=caption) 
 
