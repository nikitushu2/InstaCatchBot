import os
import requests
from dotenv import load_dotenv
from typing import Final
from discord.ext import commands
import discord
from dataclasses import dataclass


load_dotenv()

BOT_TOKEN: Final = os.getenv("BOT_TOKEN")
CHANNEL_ID = 1185569801368768552

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello! InstaCatchBot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! InstaCatchBot is ready!")


def get_instagram_profile(username):
 
    # Base URL for the Instagram API
    base_url = "https://www.instagram.com/"
 
    # Construct the URL for the profile
    profile_url = base_url + username
    
 
    try:
        # Send a GET request to the profile URL
        response = requests.get(profile_url)
 
        # Check if the profile exists
        if "[184,88]" in response.text:
            return "User not found."
        if response.status_code == 200:
            print(response.text)
            return profile_url
        else:
            # Profile not found or error occurred
            return {}
    except requests.exceptions.RequestException as e:
        # Error occurred during the request
        print(f"Error retrieving Instagram profile: {e}")
        return {}

@bot.command()
async def search(ctx, arg):
    await ctx.send(get_instagram_profile(arg))


bot.run(BOT_TOKEN)
