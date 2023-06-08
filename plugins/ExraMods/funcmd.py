import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("funcmd")) 
async def funcmd(_, message):
    hm = await message.reply_text("GETTING ALL MY FUN COMMANDS READY................")
    await asyncio.sleep(5)
    await hm.edit("/iloveu - TO PROPOSE THE BOT.\n\n/suchitha - TO KNOW ABOUT THE BOT. \n\n/botmood - TO KNOW THE BOT MOOD.\n\n/lovestory - TO GET A SMALL LOVE STORY FOR TIME PASS.  ")

   
