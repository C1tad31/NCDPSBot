from discord.ext import commands
import discord
import json # for later use with config
from datetime import datetime


class Events(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print("Bot Connected as: {}".format(self.bot.user.name))

	@commands.Cog.listener()
	async def on_message(self, message):
		log_channel = discord.utils.get(message.guild.channels, name="server-logs")
		if message.author == self.bot.user:
			return

		message_embed = discord.Embed(
			title="Message Logs",
			description="Message Received from: {}\nMessage Content: {}\nChannel: {}".format(message.author.mention, message.clean_content, message.channel.mention),
			colour=discord.Colour.blurple(),
		)
		message_embed.timestamp = datetime.utcnow()
		await log_channel.send(embed=message_embed)

	@commands.Cog.listener()
	async def on_message_delete(self, message):
		message_embed = discord.Embed(
			title="Message Logs",
			description="Message Received from: {}\nDeleted message Content: {}\nChannel: {}".format(message.author.mention, message.clean_content, message.channel.mention),
			colour=discord.Colour.blurple(),
		)
		message_embed.timestamp = datetime.utcnow()
		await log_channel.send(embed=message_embed)

	@commands.Cog.listener()
	async def on_message_edit(self, before, after):
		message_embed = discord.Embed(
			title="Message Logs",
			description="Message Received from: {}\nBefore Message Content: {}\nAfter Message Content: {}\nChannel: {}".format(message.author.mention, before.clean_content, after.clean_content, message.channel.mention),
			colour=discord.Colour.blurple(),
		)
		message_embed.timestamp = datetime.utcnow()
		await log_channel.send(embed=message_embed)


	@commands.Cog.listener()
	async def on_guild_role_create(self, role):
		message_embed = discord.Embed(
			title="Message Logs",
			description="Message Received from: {}\nBefore Message Content: {}\nAfter Message Content: {}\nChannel: {}".format(message.author.mention, before.clean_content, after.clean_content, message.channel.mention),
			colour=discord.Colour.blurple(),
		)
		message_embed.timestamp = datetime.utcnow()
		await log_channel.send(embed=message_embed)

	@commands.Cog.listener()
	async def on_guild_role_delete(self, role):
		message_embed = discord.Embed(
			title="Message Logs",
			description="Message Received from: {}\nBefore Message Content: {}\nAfter Message Content: {}\nChannel: {}".format(message.author.mention, before.clean_content, after.clean_content, message.channel.mention),
			colour=discord.Colour.blurple(),
		)
		message_embed.timestamp = datetime.utcnow()
		await log_channel.send(embed=message_embed)



def setup(bot):
	bot.add_cog(Events(bot))