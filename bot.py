from discord.ext import commands
import discord
import json

with open("config/presets.json") as presets:
	config = json.load(presets)


TOKEN = config["token"]
PREFIX = config["prefix"]


bot = commands.Bot(command_prefix=PREFIX)
bot.remove_command("help")

cogs = [
	"cogs.events",
	"cogs.commands",
	"cogs.modcommands",
]

for cog in cogs:
	bot.load_extension(cog)
	# print("Loaded Cog Files: {}".format(cog[])) used for debugging purposed


bot.run(TOKEN, reconnect=True)