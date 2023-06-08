import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from love_stories import stories

@Client.on_message(filters.command("suchitha"))
async def suchitha_command_handler(client: Client, message: Message):
    # Choose a random story from the list
    story = random.choice(stories)
    
    pm = await message.reply_text("WRITING AN LOVE STORY FOR YOU...............")
    await asyncio.sleep(10)  # wait for 10 seconds
    
    await pm.edit(f"{story}\n\n CREDITS  <a href='https://t.me/TG_LATHEESH'>𝗟𝗔𝗧𝗛𝗘𝗘𝗦𝗛</a>  ")
