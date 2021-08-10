from discord.ext import commands
import discord
import json # for later use with config
from datetime import datetime


class Commands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx):
		await ctx.message.delete()
		help_embed = discord.Embed(
			title="{}'s Help Menu".format(self.bot.user.name),
			description="Displays a list of commands for the bot",
			colour=discord.Colour.blurple(),
		)
		help_embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
		help_embed.set_thumbnail(url="")
		help_embed.add_field(name=".help", value="Displays this menu", inline=False)
		help_embed.add_field(name=".info", value="Displays info about a user", inline=False)
		help_embed.add_field(name=".serverinfo", value="Displays info about the server", inline=False)
		help_embed.add_field(name=".clear", value="Clear a specified number of messages from the chat", inline=False)
		help_embed.add_field(name=".kick", value="Kick a specified user", inline=False)
		help_embed.add_field(name=".ban", value="Ban a specified user", inline=False)
		help_embed.add_field(name=".mute", value="Mute a specified user", inline=False)
		help_embed.add_field(name=".unmute", value="Unmute a specified user", inline=False)
		help_embed.timestamp = datetime.utcnow()
		help_embed.set_footer(text="Official Evil Core Discord Bot")
		await ctx.send(embed=help_embed)

	@commands.command()
	async def info(self, ctx):
		pass

	@commands.command()
	async def serverinfo(self, ctx):
		pass




def setup(bot):
	bot.add_cog(Commands(bot))