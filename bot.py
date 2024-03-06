import discord
import responses
from dotenv import load_dotenv
import os
from scheduler import scheduler
load_dotenv()
async def send_message(message, user_message, is_private):
    try:
        user_message = str(user_message)  # Ensure user_message is a string
        print("Received message:", user_message, )

        response = responses.handle_response(user_message,message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = os.getenv('TOKEN')
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        scheduler.start()
        print(f"{client.user} Bot Started")
   
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        print(message)
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f"{username} said: '{user_message}' {channel}")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)

        else:
            await send_message(message, user_message, is_private=False)    
    client.run(TOKEN)
    



