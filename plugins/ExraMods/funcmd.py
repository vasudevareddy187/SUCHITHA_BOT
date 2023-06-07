import random
from pyrogram import Client, filters

@Client.on_message(filters.command("funcmd")) 
async def funcmd(_, message):
    hm = await message.reply_text("GETTING ALL MY FUN COMMANDS READY................")
    await hm.edit("/iloveu - TO PROPOSE THE BOT.\n\n/suchitha - TO KNOW ABOUT THE BOT. \n\n/botmood - TO KNOW THE BOT MOOD. ")

   
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
async def mood_command_handler(_, message):
    # Choose a random emoji from the list
    random_emoji = random.choice(emojis)
    # Send the emoji as a message reply
    await message.reply_text(random_emoji)
