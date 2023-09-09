from pyrogram import Client,filters
from pyrogram.types import Message


@Client.on_message(filters.command("dice"))
async def throw_dice(client, message: Message):
    six = False

    c = message.chat.id
    if not six:
        return await client.send_dice(c, "🎲")

    m = await client.send_dice(c, "🎲")

    while m.dice.value != 6:
        await m.delete()
        m = await client.send_dice(c, "🎲")




@Client.on_message(filters.command("spinner"))
async def spinner_throw(client, message: Message):
    six = False

    c = message.chat.id
    if not six:
        return await client.send_dice(c, "🎰")

    m = await client.send_dice(c, "🎰")

    while m.dice.value != 6:
        await m.delete()
        m = await client.send_dice(c, "🎰")


@Client.on_message(filters.command("focus"))
async def arrow_throw(client, message: Message):
    six = False

    c = message.chat.id
    if not six:
        return await client.send_dice(c, "🎯")

    m = await client.send_dice(c, "🎯")

    while m.dice.value != 6:
        await m.delete()
        m = await client.send_dice(c, "🎯")

    
@Client.on_message(filters.command("aim"))
async def ball_throw(client, message: Message):
    six = False

    c = message.chat.id
    if not six:
        return await client.send_dice(c, "🎳")

    m = await client.send_dice(c, "🎳")

    while m.dice.value != 6:
        await m.delete()
        m = await client.send_dice(c, "🎳")
