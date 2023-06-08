import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("funcmd")) 
async def funcmd(_, message):
    hm = await message.reply_text("GETTING ALL MY FUN COMMANDS READY................")
    await asyncio.sleep(5)
    await hm.edit("/iloveu - TO PROPOSE THE BOT.\n\n/suchitha - TO KNOW ABOUT THE BOT. \n\n/botmood - TO KNOW THE BOT MOOD.\n\n/lovestory - TO GET A SMALL LOVE STORY FOR TIME PASS.  ")

   
emojis = ["😀 Grinning", "😃 Smiling", "😄 Grinning With Smiling Eyes",
          "😁 Beaming With Smiling Eyes", "😆 Grinning Squinting",
          "😅 Grinning With Sweat", "😂 Tears of Joy",
          "🤣 Rolling on the Floor Laughing", "☺️ Smiling",
          "😊 Smiling With Smiling Eyes", "😇 Smiling With Halo",
          "🙂 Slightly Smiling", "🙃 Upside-Down",
          "😉 Winking", "😌 Relieved", "😍 Smiling With Heart-Eyes",
          "🥰 Smiling With Hearts", "😘 Blowing a Kiss",
          "😗 Kissing", "😙 Kissing With Smiling Eyes",
          "😚 Kissing With Closed Eyes", "😋 Savoring Food",
          "😛 With Tongue", "😝 Squinting With Tongue",
          "😜 Winking With Tongue", "🤪 Zany", "🤨 Raised Eyebrow",
          "🧐 Monocle", "🤓 Nerd", "😎 With Sunglasses",
          "🤩 Star-Struck", "🥳 Partying", "😏 Smirking",
          "😒 Unamused", "😞 Disappointed", "😔 Pensive",
          "😟 Worried", "😕 Confused", "🙁 Slightly Frowning",
          "😣 Persevering", "😖 Confounded", "😫 Tired",
          "😩 Weary", "🥺 Pleading", "😢 Crying",
          "😭 Loudly Crying", "😤 With Steam From Nose",
          "😠 Angry", "😡 Pouting", "🤬 With Symbols on Mouth",
          "🤯 Exploding Head", "😳 Flushed", "🥵 Overheated",
          "🥶 Freezing", "😱 Screaming in Fear", "😨 Fearful",
          "😰 Anxious With Sweat", "😥 Sad but Relieved",
          "😓 Downcast With Sweat", "🤗 Hugging"]


@Client.on_message(filters.command("botmood"))
async def suchitha_command_handler(client: Client, message: Message):
    # adding message for the reply 
    mood_checking_msg = await message.reply_text("CHECKING MY MOOD....................")
    # setting sleep for 5 seconds
    await asyncio.sleep(5)
    # Choose a random emoji from the list
    random_emoji = random.choice(emojis)
    # Send the emoji as a message reply
    await mood_checking_msg.edit(random_emoji)
