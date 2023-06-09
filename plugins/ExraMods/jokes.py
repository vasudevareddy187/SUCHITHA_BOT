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

    "Why don't scientists trust atoms? Because they make up everything!",
    
    "Why don't scientists trust atoms? Because they make up everything!",

  "Why did the scarecrow win an award? Because he was outstanding in his field!",

  "What do you call fake spaghetti? An impasta!",

  "Why don't seagulls fly by the bay? Because then they would be bagels!",

  "How does a penguin build its house? Igloos it together!",

  "Why don't oysters share their pearls? Because they're shellfish!",

  "Why do cows wear bells? Because their horns don't work!",

  "What's the best way to watch a fly fishing tournament? Live stream!",

  "Why did the cyclist keep falling over? Because he was two-tired!",

  "What do you call a lazy kangaroo? A pouch potato!",

  "Why did the frog call his insurance company? He had a jump in his car!",

  "What do you call a snake that works for the government? A civil serpent!",

  "Why don't ants get sick? They have tiny ant-bodies!",

  "Why do bees hum? Because they don't know the words!",

  "What do you call an alligator in a vest? An investigator!",

  "Why don't trees have social media? Because they prefer face-to-face interactions!",

  "What do you call a sleeping bull? A bulldozer!",

  "Why couldn't the bicycle stand up by itself? It was two-tired!",

  "What do you call a fish with no eyes? Fsh!",

  "Why don't cats play poker in the jungle? Too many cheetahs!",

  "Why did the tomato turn red? Because it saw the salad dressing!",

  "Why do fish live in saltwater? Because pepper water makes them sneeze!",

  "What did one leaf say to the other? I'm falling for you!",

  "Why was the math book sad? Because it had too many problems!",

  "Why don't elephants use computers? They're afraid of mice!",

  "Why can't a leopard hide? Because he's always spotted!",

  "Why did the cow go to space? To see the moooon!",

  "What do you call a bear with no teeth? A gummy bear!",

  "Why did the mushroom go to the party? Because he was a fungi!",

  "Why don't trees like to go to parties? Because they're afraid of getting leafed out!",

  "What do you call a bird that's afraid to fly? A chicken!",

  "Why did the banana go to the doctor? Because it wasn't peeling well!",

  "What do you get when you cross a snowman and a shark? Frostbite!",

  "How do you know if a tree is a dogwood? When it barks!",

  "What do you call an alligator in a vest? An investigator!",

  "Why are frogs always happy? They eat whatever bugs them!",

  "Why was the broom late? It swept in!",

  "Why couldn't the bicycle stand up by itself? It was two-tired!",

  "What do you call an owl magician? Hoo-dini!",

  "Why do bees have sticky hair? Because they use honeycombs!",

  "What do you call a deer with no eyes? No eye-deer!",

  "Why did the chicken join a band? To play its drumsticks!",

  "Why don't chickens wear pants? Because their peckers are on their faces!",

  "Why was the belt sent to jail? For holding up pants!",

  "Why do birds fly south for the winter? Because it's too far to walk!",

  "Why did the cookie go to the doctor? Because it felt crummy!",

  "What do you call a bear with no ears? B!",

  "Why don't snakes have legs? They prefer slithering!",

  "What's a tree's favorite drink? Root beer!",

  "Why do seagulls fly over the sea? Because if they flew over the bay, they would be bagels!",

  "What did the grape say when it got stepped on? Nothing, it just let out a little wine!",

  "Why was the math book sad? Because it had too many problems!",

  "Why did the tomato turn red? Because it saw the salad dressing!",

  "Why don't trees like to go to parties? Because they're afraid of getting leafed out!"

    "What do you call a bear with no teeth? 🐻🦷 A gummy bear!",

    "Why don't elephants use computers? 🐘💻 They're afraid of mice!",

    "Why are fish so smart? 🐟🧠 Because they're always in schools!",

    "What did the grape say when the elephant stepped on it? 🍇💬 Nothing. It just let out a little wine!",

    "Why are frogs always so happy? 🐸😄 They eat whatever bugs them!",

    "How does a penguin build its house? ❄️🐧 Igloos it together!",

    "Why did the cow go to outer space? 🐮🚀 To see the moooon!",

    "Why don't dogs make good dancers? 🐶💃 They have two left feet!",

    "What do you call a happy turtle? 🐢😊 A shell-ebration!",

    "Why don't birds play video games? 🐦🎮 They prefer real life tweet-ment!",

    "Why do spiders make bad baseball players? 🕷️⚾️ They always get caught in the web!",

    "What do you get when you cross a snake and a pie? 🐍🥧 A python!",

    "Why did the crab never share with anyone? 🦀🙅‍♀️ He was shellfish!",

    "Why don't pandas like to borrow things? 🐼🤲 They always return them chewed!",

    "What do you call a group of cows playing instruments? 🐮🎶 A moo-sical band!",

    "What's a frog's favorite drink? 🐸☕️ Croak-o!",

    "Why did the monkey cross the road? 🐒🚦 To get to the banana tree on the other side!",

    "What do you call a sheep that can sing? 🐑🎤 Ewe-nique!",

    "Why don't ants get sick? 🐜💊 They have tiny ant-bodies!",

    "Why are fish so smart? 🐠🧠 Because they're always in schools!",

    "What's a shark's favorite game? 🦈🏀 Sink-a-ball!",

    "Why did the zebra go to the doctor? 🦓👨‍⚕️ Because its stripes were starting to run!",

    "Why do kangaroos hate rainy days? 🦘☔️ They can't hop inside!",

    "What's a snake's favorite subject in school? 🐍📚 Hiss-tory!",

    "What do you call an alligator in a vest? 🐊🧥 An investigator!",

    "Why did the horse get a job at the casino? 🐴🎲 He was an excellent neigh-sayer!",

    "What did the grape say when it got stepped on? 🍇💬 Nothing, it just let out a little wine!",

    "Why don't ducks use umbrellas? 🦆☔️ They prefer to waddle in the rain!",

    "What do you call a bee that's always complaining? 🐝😫 A buzz-kill!",

    "Why did the snail paint racing stripes on his shell? 🐌🎨 So he could go faster!",

    "What do you call a bear with no ears? 🐻👂 B!",

    "Why do owls always make great students? 🦉📚 Because they're wise!",

    "What do you call a sleeping wolf? 🐺💤 A werewolf!",

    "Why did the tiger wear stripes? 🐅👕 Because spots were too plain!",

    "Why did the cow break up with her boyfriend? 🐮❤️ He was udderly boring!",

    "Why are spiders great at swimming? 🕷️🏊‍♂️ They have eight flippers!",

    "What do you call a bear that's always on the go? 🐻🏃‍♂️ A bear-o-dynamic!",

    "Why don't elephants ever use computers? 🐘💻 They prefer paper-trunks!",

    "What do you call a cat that likes to eat lemons? 🐱🍋 A sourpuss!",

    "Why couldn't the bicycle stand up by itself? 🚲 It was two-tired!",

    "What do you get when you cross a sheep and a kangaroo? 🐑🦘 A woolly jumper!"

    
]

@Client.on_message(filters.command("jokes"))

async def joke(_, message):

    hm = await message.reply_text("Let me think of a good one...")

    await asyncio.sleep(3)

    joke = random.choice(jokes)

    await hm.edit(joke)
    
