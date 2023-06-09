import random

import asyncio

from pyrogram import Client, filters

from pyrogram.types import Message

jokes = [

    "Why did the tomato turn red? Because it saw the salad dressing!",

    "Why don't scientists trust atoms? Because they make up everything!",

    "Why was the math book sad? Because it had too many problems.",

    "What do you call an alligator in a vest? An investigator!",

    "Why don’t oysters give to charity? Because they’re shellfish.",

    "Why do seagulls fly over the sea? Because if they flew over the bay, they’d be bagels!",

    "What do you get when you cross a snowman and a shark? Frostbite!",

    "Why did the scarecrow win an award? Because he was outstanding in his field!",

    "Why don’t skeletons fight each other? They don’t have the guts!",

    "Why did the elephant wear green sneakers? Because the red ones were in the wash!",

    "Why couldn’t the bicycle stand up by itself? Because it was two-tired!",

    "Why did the chicken cross the road? To get to the other side!",

    "Why did the cookie go to the doctor? Because he felt crummy.",

    "What do you get when you cross a cow and a duck? Milk and quackers!",

    "Why did the banana go to the doctor? Because it wasn’t peeling well.",

    "What do you get when you cross a snowman and a vampire? Frostbite!",

    "What did the grape say when it got stepped on? Nothing, it just let out a little wine!",

    "Why did the hipster burn his tongue? He drank his coffee before it was cool.",

    "What do you call a fake noodle? An impasta!",

    "Why did the frog call his insurance company? He had a jump in his car!",

    "Why don't dinosaurs drive cars? Because they're extinct!",

    "What do you get when you cross a snake and a pie? A python!",

    "Why did the tomato turn green? Because it was unripe!",

    "Why did the bear cross the road? To get to the honey on the other side!",

    "What do you call an alligator in a vest? An investigator!",

    "Why did the strawberry cry? Because its mother was in a jam.",

    "Why did the monkey like the banana? Because it had appeal!",

    "What did the grape say when it got stepped on? Nothing, it just let out a little wine!",

    "Why did the duck go to the doctor? Because he was feeling a bit down.",

    "Why do bees have sticky hair? Because they use honeycombs!",

    "What did one hat say to the other? You stay here, I'll go on ahead!",

    "Why did the cookie go to the doctor? Because he felt crumbly!",

    "What do you give a sick bird? Tweetment!",

    "Why do cows wear bells? Because their horns don’t work!",

    "Why couldn’t the pirate learn the alphabet? Because he kept getting lost at C!",

    "What did the left eye say to the right eye? Between us, something smells!",

    "What did the big flower say to the little flower? Hey, bud!",

    "Why don’t scientists trust atoms? Because they make up everything!",

    "Why did the belt go to jail? For holding up pants!",

    "Why did the computer go to the doctor? Because it had a virus!",

    "Why did the fireman wear red suspenders? To keep his pants up!",

    "What did the grape say when it got stepped on? Nothing, it just let out a little wine!",

    "Why was the math book sad? Because it had too many problems.",

    "Why did the boy sprinkle sugar on his pillow before he went to sleep? So he could have sweet dreams!",

    "Why did the teacher wear sunglasses? Because her class was so bright!",

    "Why did the man put his money in the freezer? He wanted cold hard cash!",

    "What did the grape say when it got stepped on? Nothing, it just let out a little wine!",

    "Why did the kid cross the playground? To get to the other slide!",

    "Why do bicycles fall over? Because they're two-tired!",

    "What do you call a dog magician? A Labracadabrador!",

    "Why did the tomato turn red? Because it saw the salad dressing!",

    "What do you call a bear with no teeth? A gummy bear!",

    "Why don't scientists trust atoms? Because they make up everything!"
]

@Client.on_message(filters.command("joke"))

async def joke(_, message):

    hm = await message.reply_text("Let me think of a good one...")

    await asyncio.sleep(3)

    joke = random.choice(jokes)

    await hm.edit(joke)
    
