from discord.ext import commands
import discord
import json # for later use with config


class ModCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	@commands.cooldown(10, 1, commands.BucketType.user)
	async def clear(self, ctx, amount=None):
		if not amount:
			pass
		else:
			await ctx.channel.purge(limit=int(amount))
			await ctx.send("{} messages have been purged by: {}".format(amount, ctx.author.mention))

	@clear.error
	async def clear_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send("You dont have enough permission to use this command")
		if isinstance(error, commands.CommandOnCooldown):
			pass

	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.cooldown(10, 1, commands.BucketType.user)
	async def kick(self, ctx, member: discord.Member=None, *, reason=None):
		if not member:
			pass
		elif not reason:
			pass
		else:
			await member.kick(reason=reason)
			await ctx.send("{} has been kicked by: {}\n\nReason: ``{}``".format(member.mention, ctx.author.mention, reason))

	@kick.error
	async def kick_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send("You dont have enough permission to use this command")
		if isinstance(error, commands.CommandOnCooldown):
			pass

	@commands.command()
	@commands.has_permissions(ban_members=True)
	@commands.cooldown(10, 1, commands.BucketType.user)
	async def ban(self, ctx, member: discord.Member=None, *, reason=None):
		if not member:
			pass
		elif not reason:
			pass
		else:
			await member.ban(1, reason=reason)
			await ctx.send("{} has been banned by: {}\n\nReason: ``{}``".format(member.mention, ctx.author.mention, reason))

	@ban.error
	async def kick_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send("You dont have enough permission to use this command")
		if isinstance(error, commands.CommandOnCooldown):
			pass

	@commands.command()
	@commands.has_permissions(manage_roles=True)
	@commands.cooldown(10, 1, commands.BucketType.user)
	async def mute(self, ctx, member: discord.Member=None, *, reason=None):
		if not member:
			pass
		elif not reason:
			pass
		else:
			await member.kick(reason=reason)
			await ctx.send("{} has been kicked by: {}\n\nReason: ``{}``".format(member.mention, ctx.author.mention, reason))

	@mute.error
	async def mute_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send("You dont have enough permission to use this command")
		if isinstance(error, commands.CommandOnCooldown):
			pass



def setup(bot):
	bot.add_cog(ModCommands(bot))