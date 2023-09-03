from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import requests

# Weather API key
weather_apikey = "8de2d8b3a93542c9a2d8b3a935a2c909"

@Client.on_message(filters.command("wether"))
async def handwrit(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text = message.text.split(None, 1)[1]
    m = await message.reply_text("`Please wait...\n\nWriting your text...`")
  
    # Weather API integration
    weather_url = f"https://api.weatherapi.com/v1/current.json?key={weather_apikey}&q=London"
    weather_response = requests.get(weather_url)
    if weather_response.status_code == 200:
        weather_data = weather_response.json()
        # Extract necessary weather information here
        # Example: temperature = weather_data['current']['temp_c']
    else:
        # Handle API error here
        await m.edit("Failed to fetch weather data.")
        return
  
    write = requests.get(f"https://apis.xditya.me/write?text={text}").url
  
    caption = f"""
    sᴜᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘
    
    🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
    🌡️ **Cᴜʀʀᴇɴᴛ Tᴇᴍᴘᴇʀᴀᴛᴜʀᴇ:** {temperature}°C
    🌀 **POWERED BY** : <a href=https://t.me/llathu63035<💕NTM💕></a>
    """
    await m.delete()
    await message.reply_photo(photo=write, caption=caption)
