import random
from retrive_data import *
from symbols import fetch, interval_dict

async def send_symbols_in_chunks(symbols_dict, message,is_private, chunk_size=10):
    keys = list(symbols_dict.keys())
    chunks = [keys[i:i + chunk_size] for i in range(0, len(keys), chunk_size)]
    
    for chunk in chunks:
        symbols_list = "Symbols     : Exchanges\n"
        symbols_list += "\n".join([f"{symbol:<12}: {symbols_dict[symbol][0]}" for symbol in chunk])
        formatted_text = f"```\n{symbols_list}\n```"
        await message.author.send(formatted_text) if is_private else await message.channel.send(formatted_text)

import discord
async def handle_response(user_message, message,is_private) -> str:
    if not isinstance(user_message, str):
        user_message = str(user_message)

    p_message = user_message.upper()
    print("p_message", p_message)
    responses = {
        "HI": """
            *Hello there!*
            This bot is designed to provide divergence alerts to the user.
            To learn more about how to use this bot, type `Help`.
        """,
        "HELLO": "**Hello there! How can I assist you?**",
        "HELP": """
            *This bot is here to provide you with divergence alerts. Here's how you can interact with it:*
            - To view all available symbols: `list symbols`.

            - To start receiving divergence alerts, use the following commands:
                
                - `START-15-MINUTE`
                
                - `START-1-HOUR`
                
                - `START-4-HOUR`
                
                - `START-DAILY`
                
                - `START-WEEKLY`
                - `All Interval`

            - To stop the bot and alerts, use: `STOP-BOT`.
        """,
        "LIST SYMBOLS": "list symbols",
        "LIST INTERVAL": list(interval_dict.keys()),
    }
    embed=None
    if p_message in responses:
        if p_message == "LIST SYMBOLS":
            await send_symbols_in_chunks(fetch(), message,is_private)
        else:
            return responses[p_message]
    elif p_message == "START-15-MINUTE":
        embed = discord.Embed(
                color=discord.Color(0xE5E242),
                description="Started 15-MINUTE interval."
            )
        await message.author.send(embed=embed) if is_private else await message.channel.send(embed=embed)
        await find_symbol_exchange(message,is_private, Interval.in_15_minute)
    elif p_message == "START-1-HOUR":
        embed = discord.Embed(
                color=discord.Color(0xE5E242),
                description="Started 1-HOUR interval."
            )
        await message.author.send(embed=embed) if is_private else await message.channel.send(embed=embed)
        await find_symbol_exchange(message,is_private, Interval.in_1_hour)
    elif p_message == "START-4-HOUR":
        embed = discord.Embed(
                color=discord.Color(0xE5E242),
                description="Started 4-HOUR interval."
            )
        await message.author.send(embed=embed) if is_private else await message.channel.send(embed=embed)
        await find_symbol_exchange(message,is_private, Interval.in_4_hour)
    elif p_message == "START-DAILY":
        embed = discord.Embed(
                color=discord.Color(0xE5E242),
                description="Started START-DAILY interval."
            )
        await message.author.send(embed=embed) if is_private else await message.channel.send(embed=embed)
        await find_symbol_exchange(message,is_private, Interval.in_daily)
    elif p_message == "START-WEEKLY":
        embed = discord.Embed(
                color=discord.Color(0xE5E242),
                description="Started START-WEEKLY interval."
            )
        await message.author.send(embed=embed) if is_private else await message.channel.send(embed=embed)
        await find_symbol_exchange(message,is_private, Interval.in_weekly)

    elif p_message == "STOP-BOT":
        await stop_all_jobs(message,is_private)
        return 
    else:
        return "Something went wrong"
    