from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("suchitha"))
async def suchitha_command_handler(client: Client, message: Message):
    pm = await message.reply_text("FEATURING ABOUT ME...............")
    await pm.edit(f"HI 👋👋\n\n MY NAME IS SUCHITHA. I KNOW YOU WILL THINK WHY MY NAME IS SUCHITHA . IT IS LONG LOVE STORY FOR MY CREATOR  <a href='https://t.me/sula20062007'>𝗟𝗔𝗧𝗛𝗘𝗘𝗦𝗛</a>  . IT IS A SAD STORY FOR MY CREATOR . BUT DONT THINK THERE IS AN SAD ENDING FOR THIS STORY IT IS STILL NOT YET GET ENDED. IF YOU WANT TO KNOW THE STORY OF THE NAME 'SUCHITHA' . I WAS FIRST BORN IN THE MONTH FEBRUARY OF 2023 . \n\n I AM MAINLY CREATED TO PRODUCE MOVIES . \n\n THANKS FOR YOUR PASSIONS IN LISTENING MY STORY ")
