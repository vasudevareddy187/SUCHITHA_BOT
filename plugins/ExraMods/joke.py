import requests

@Client.on_message(filters.command("joke"))

async def joke_command_handler(client: Client, message: Message):

    pm = await message.reply_text("Let me think of a good one...")

    

    # Fetch a random joke from an API

    response = requests.get("https://official-joke-api.appspot.com/random_joke")

    if response.status_code == 200:

        joke_data = response.json()

        await pm.edit(f"{joke_data['setup']}\n\n{joke_data['punchline']}")

    else:

        await pm.edit("Oops, something went wrong. Can't think of a joke right now.")

