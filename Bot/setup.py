import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import random
import sys
import asyncio

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()

client = commands.Bot(command_prefix="-", intents=intents, case_insensitive=False,)

