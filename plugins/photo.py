from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters


@Client.on_message(filters.photo & filters.private)
async def photo(client: Client, message: Message):
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="Select your required mode from below",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="𝖡RIGHT", callback_data="bright"),
                        InlineKeyboardButton(text="𝖬IXED", callback_data="mix"),
                        InlineKeyboardButton(text="𝖡 & 𝖶", callback_data="b|w"),
                    ],
                    [
                        InlineKeyboardButton(text="𝖢IRCLE", callback_data="circle"),
                        InlineKeyboardButton(text="𝖡LUR", callback_data="blur"),
                        InlineKeyboardButton(text="𝖡ORDER", callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton(text="𝖲TICKER🎫", callback_data="stick"),
                        InlineKeyboardButton(text="𝖱OTATE", callback_data="rotate"),
                        InlineKeyboardButton(text="𝖢CONTRAST", callback_data="contrast"),
                    ],
                    [
                        InlineKeyboardButton(text="𝖲EPIA", callback_data="sepia"),
                        InlineKeyboardButton(text="𝖯ENCIL", callback_data="pencil"),
                        InlineKeyboardButton(text="𝖢ARTOON", callback_data="cartoon"),
                    ],
                    [
                        InlineKeyboardButton(text="𝖨NVERT", callback_data="inverted"),
                        InlineKeyboardButton(text="𝖦LITCH", callback_data="glitch"),
                        InlineKeyboardButton(
                            text="𝖡𝖦 REMOVER", callback_data="removebg"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="𝖢𝗅𝗈𝗌𝖾", callback_data="close_data"),
                    ],
                ]
            ),
            reply_to_message_id=message.id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text(f"{e} \nSomething went wrong!", quote=True)
            except Exception:
                return
