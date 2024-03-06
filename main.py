# import discord
# import responses
# from dotenv import load_dotenv
# import asyncio
# import os
# from scheduler import scheduler
# client = discord.Client(intents=discord.Intents.default())
# async def send_message(message, user_message, is_private):
#     try:
#         user_message = str(user_message)  # Ensure user_message is a string
#         print("Received message:", user_message, )

#         response = await responses.handle_response(user_message,message)
#         await message.author.send(response) if is_private else await message.channel.send(response)
#     except Exception as e:
#         print(e)

# async def on_ready():
#     scheduler.start()
#     print("Bot Started")

# async def on_message(message):
#     if message.author == client.user:
#         return
#     print(message)
#     username = str(message.author)
#     user_message = str(message.content)
#     channel = str(message.channel)
#     print(f"{username} said: '{user_message}' {channel}")

#     if user_message[0] == '?':
#         user_message = user_message[1:]
#         await send_message(message, user_message, is_private=True)
#     else:
#         await send_message(message, user_message, is_private=False)
 


# async def main():
#     load_dotenv()
#     TOKEN = os.getenv('TOKEN')
#     client.event(on_ready)  # Register on_ready directly as a coroutine function
#     client.event(on_message)  # Pass client to on_message
#     try:
#         await client.start(TOKEN)
#     except KeyboardInterrupt:
#         await client.logout()
#         scheduler.shutdown()

# if __name__ == '__main__':
#     asyncio.run(main())


import discord
import responses
from dotenv import load_dotenv
import os
from scheduler import scheduler
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="--", case_insensitive=True, intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    scheduler.start()
    print("Bot Started")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    print(f"{username} said: '{user_message}' {channel}")

    if user_message.startswith('?'):
        user_message = user_message[1:]
        pass
        # await send_message(message, user_message, is_private=True)
    else:
        await send_message(message, user_message, is_private=False)

async def send_message(message, user_message, is_private):
    try:
        user_message = str(user_message)
        print("Received message:", user_message)

        response = await responses.handle_response(user_message, message,is_private)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def main():
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
