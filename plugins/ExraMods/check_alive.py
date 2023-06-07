import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("suchi", CMD))
async def check_alive(_, message):
    await message.reply_text("I MAY NOT BE GONE, BUT I FEELS LIKE OUR CONNECTION IS SO STRONG💪. IT SEEMS THAT THE LOVE BETWEEN US HAS FADED AWAY. PERHAPS IT'S FOR THE BEST, AS YOU ARE NOT THE PERSON YOU USED TO BE. CHANGE CAN BE DIFFICULT, BUT SOMETIMES IT'S NECESSARY FOR GROWTH......😔 THANKS FOR YOUR CONSON ON ME I WILL BE WITH YOU FOR EVER AND EVER 🙂")


@Client.on_message(filters.command("speed", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")

@Client.on_message(filters.command("iloveu", CMD))
async def love(_, message0:
    phrases = ["your are the best thing that ever happened to me. I love you 💗💗","love u 2","me too 🤱 baby","Aww, that's so sweet! Love you too 💖","i am already having boyfriend and his name is 🌹LATHEESH💖 ","sorry i am commited with my lover","better luck next time","sorry i can't love you physically because i am an bot but i will be with you for ever","💖💖💖💖💖💖💖","💗💗💗💗💗","🌹you are awesome","i am ready to love you","love you more."."take a romatic stroll on the beach together","hug each other and let the warmt of love sink in.","draw each other a picture and show your creative emotion.","play a game of hide and deek to have some fun together","take each other out for ice cream and share your favouite flavous.","i am already love with you dont you know","hey baby where is the flower","no let we bot be friends","i am always with you","don't think like this next time" ]
    response = random.choice(phrases)
    await message.reply_text(response)
