import discord
from discord.ext import commands
import datetime
import asyncio
from discordTogether import DiscordTogether
import random
import json

prefix = "!" #What the bot's prefix is. If the prefix is ! then the help command would be !help

moderators =  #Role ID for mods.

clear_chat =  #Role ID for clear_chat perms.

admins =  #Role ID for admins.

client = commands.Bot(command_prefix=prefix, help_command=None)
togetherControl = DiscordTogether(client)

logsID = #Your logs channel 1 ID
logsID2 = #Your logs channel 2 ID

TOKEN = '' #Your bot's token.

#Rules, put \n for a new line, copy and paste your rules in.

Rules = '**__Rules__**\n '

#Remove the "#" and edit where it says ["cat", "dog"] to the words you want filtered, to add more put copy , "dog" and change dog to what you want filtered.

# filtered_words = ["cat", "dog"]  # put words you want deleted here

logs_channel = client.get_channel(logsID)

ModMailTime = '120'

ModMailChannel = 829708466582061077

status = 'hi' #What you want the bot's status to be.

status_kind = 'watching' #This dosen't change anything in the bot.

server = 'bye' #Server name.


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching , name=f'{status}'))

    print("Bot is ready")
    print(f"Server is {server}, status is {status_kind} {status}, logs channel is {logs_channel} and the rules are {Rules}.")


@client.event
async def on_message_delete(message):
    msg = str(message.author.display_name) + ' deleted message in #' + str(
        message.channel) + ': ' + str(message.content)
    print(msg)

#Remove the "#" if you want filtered words.

#@client.event
#async def on_message(msg):
#    for word in filtered_words:
#        if word in msg.content:
#            await msg.delete()

#    await client.process_commands(msg)


@client.event
async def on_command_error(ctx, error):
    support_channel = client.get_channel(logsID)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You can't do that.")
        await ctx.message.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter all the required arguments.")
        await ctx.message.delete()
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("That command dosen't exist.")
        await ctx.message.delete()
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send("You can't use that command in a DM.")
        await ctx.message.delete()
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("Command invoke error, I have messaged support to find the problem.")
        print(error)
    elif isinstance(error, commands.NoPrivateMessage):
        await ctx.send("You can't use that command in DMs.")
    else:
        raise error

@client.command()
async def rules(ctx):
    await ctx.send(Rules)
    print("Rules asked for.")


@client.command(aliases=['c'])
@commands.has_role(clear_chat)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    print("Clear was used.")

@client.command()
async def startYT(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command()
async def chess(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'chess')
    await ctx.send(f'Click the blue link!\n{link}')

@client.command(aliases=['k'])
@commands.has_any_role(moderators, admins, clear_chat, 827475273138176071)
async def kick(ctx, member: discord.Member, *, reason="No reason provided."):
    try:
      try:
        await member.kick(reason=reason)
        await member.send(f"You have been kicked from {server}, because: " + reason)
      except:
        logs_channel = client.get_channel(logsID)
        logs_channel2 = client.get_channel(logsID2)
        await ctx.send(f"Unable to kick {member.mention}.")
        print("Unable to kick.")
        await logs_channel.send(f"{ctx.author.display_name} used kick on {member.display_name} for {reason} but was unable to kick them.")
        print("kick used, log sent.")
        await logs_channel2.send(f"{ctx.author.display_name} used kick on {member.display_name} for {reason} but was unable to kick them.")
        print("kick used, log sent.")
      try:
        logs_channel = client.get_channel(logsID)
        logs_channel2 = client.get_channel(logsID2)
        await logs_channel.send(f"{ctx.author.display_name} used kick on {member.display_name} for {reason}")
        print("kick used, log sent.")
        await logs_channel2.send(f"{ctx.author.display_name} used kick on {member.display_name} for {reason}")
        print("kick used, log sent.")
      except:
        print("Kick used")

    except:
      logs_channel = client.get_channel(logsID)
      logs_channel2 = client.get_channel(logsID2)
      await ctx.send("The member has their DMs closed.")
      await member.kick(reason=reason)
      await logs_channel.send(f"{ctx.author.display_name} used kick on {member.display_name} for {reason} unable to DM.")
      print("Kick used, DMs closed.")
      await logs_channel2.send(f"{ctx.author.display_name} used kick on {member.display_name} for {reason} unable to DM.")
      print("Kick used, DMs closed.")

@client.command
async def hello(ctx):
  await ctx.send("Hello!")

@client.command(aliases=['b'])
@commands.has_role(admins)
async def ban(ctx, member: discord.Member, *, reason="No reason provided."):
    try:
      try:
        await member.ban(reason=reason)
        await member.send(f"You have been banned from {server}, because: " + reason)
      except:
        logs_channel = client.get_channel(logsID)
        await ctx.send(f"Unable to ban {member.mention}.")
        print("Unable to ban.")
        await logs_channel.send(f"{ctx.author.display_name} used ban on {member.display_name} for {reason} but was unable to ban them.")
      try:
        logs_channel = client.get_channel(logsID)
        await logs_channel.send(f"{ctx.author.display_name} used ban on {member.display_name} for {reason}")
        print("ban used, log sent.")
      except:
        print("ban used")

    except:
      logs_channel = client.get_channel(logsID)
      await ctx.send("The member has their DMs closed.")
      await member.ban(reason=reason)
      await logs_channel.send(f"{ctx.author.display_name} used ban on {member.display_name} for {reason}")
      print("ban used, DMs closed.")


@client.command(aliases=['ub'])
@commands.has_role(admins)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')
    logs_channel = client.get_channel(logsID)

    for banned_entry in banned_users:
        user = banned_entry.user

        if (user.name, user.discriminator) == (member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send(member_name + "has been unbanned.")
            await logs_channel.send(f"{ctx.author.display_name} used unban on {member.display_name}.")
            print("Unban used.")
            return

    await ctx.send(member=" was not found.")
    print("Unban used, member not found.")


@client.command(aliases=['m'])
@commands.has_role(moderators)
async def mute(ctx, member: discord.Member, *, reason="No reason provided."):
    muted_role = ctx.guild.get_role(819230704005021696)
    logs_channel = client.get_channel(logsID)

    await member.add_roles(muted_role)
    await member.send(f"You have been muted in {server} becasue: {reason}")
    await logs_channel.send(f"{ctx.author.display_name} used mute on {member.display_name} for {reason}.")

    await ctx.send(member.mention + "has been muted.")
    print("Mute used.")


@client.command(aliases=['um'])
@commands.has_role(moderators)
async def unmute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(827474396431646732) #Muted role id

    await member.remove_roles(muted_role)
    await logs_channel.send(f"{ctx.author.display_name} used unmute on {member.display_name}.")

    await ctx.send(member.mention + "has been unmuted.")
    print("Unmute used.")


@client.command()
async def emoji(ctx):
    await ctx.send("🔻")  #emojis you want to send put here
    await ctx.send("🔎")
    await ctx.send("🔻")


@client.command(aliases=['pl'])
async def poll(ctx, *, msg):
    channel = ctx.channel
    try:
        op1, op2 = msg.split("or")
        txt = f"react with ✅️ for {op1} or ❌ for {op2}"
    except:
        await channel.send("Correct Syntax: [Choice1] or [Choice2]")
        return

    embed = discord.Embed(title="Poll",
                          description=txt,
                          colour=discord.Colour.red())
    message_ = await channel.send(embed=embed)
    await message_.add_reaction("✅") #Up vote reaction
    await message_.add_reaction("❌") #Down vote reaction
    await ctx.message.delete()


@client.command()
async def dm(ctx, user: discord.User, *, value):
    await user.send(f"{value}")


snipe_message_content = None
snipe_message_author = None
snipe_message_id = None


@client.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author.name
    snipe_message_id = message.id
    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None


@client.command()
async def snipe(message):
    if snipe_message_content == None:
        await message.channel.send("Theres nothing to snipe.")
        print("Snipe used, nothing was sniped.")
    else:
        embed = discord.Embed(description=f"{snipe_message_content}")
        embed.set_footer(
            text=
            f"Sniped by {message.author.name}#{message.author.discriminator}",
            icon_url=message.author.avatar_url)
        embed.set_author(name=f"{snipe_message_author} Deleted")
        await message.channel.send(embed=embed)
        print(f"Snipe used, {snipe_message_content} **was sniped.")
        return

@client.command()
async def modmail(ctx, message):
  await ctx.send(f'{ctx.author.mention} check your DMs.')
  await ctx.author.send(f"What do you need help with? This prompt will time out in {ModMailTime} seconds.")
  try:
    if str(message.channel.type) == "private":
       ModMail_Channel = client.get_channel(ModMailChannel)
       await ModMail_Channel.send("[" + message.author.display_name + "]")
  except:
    await asyncio.sleep(ModMailTime)


@client.group(invoke_without_command=True)
async def help(ctx,):
  embed = discord.Embed(title = "Help", description = f"Do {prefix}help <command> for more information on the command.",color = ctx.author.color)

  embed.add_field(name = "Moderation", value = "`kick` , `ban` , `mute`")
  embed.add_field(name = "Misc and fun", value = "`snipe` , `dm` , `ping` , `poll` , `rules` , `help` , `startYT` , `chess`")

  await ctx.send(embed=embed)

@help.command()
async def kick(ctx):

  embed = discord.Embed(title = "**kick**", description = "Kicks a member from this server.", color = ctx.author.color)

  embed.add_field(name = "Permission level", value = "Moderators")

  embed.add_field(name = "**Usage**", value = f"{prefix}kick <member> [reason]")

  await ctx.send(embed=embed)

@help.command()
async def ban(ctx):

  embed = discord.Embed(title = "**ban**", description = "bans a member from this server.", color = ctx.author.color)

  embed.add_field(name = "Permission level", value = "Moderators")

  embed.add_field(name = "**Usage**", value = f"{prefix}ban <member> [reason]")

  await ctx.send(embed=embed)

@help.command()
async def mute(ctx):

  embed = discord.Embed(title = "**mute**", description = "mutes a member in this server.", color = ctx.author.color)

  embed.add_field(name = "Permission level", value = "Moderators")

  embed.add_field(name = "**Usage**", value = f"{prefix}mute <member>")

  await ctx.send(embed=embed)

@help.command()
async def poll(ctx):

  embed = discord.Embed(title = "**poll**", description = "Makes a poll.", color = ctx.author.color)

  embed.add_field(name = "Permission level", value = "Everyone")

  embed.add_field(name = "**Usage**", value = f"{prefix}poll <option 1> <option 2>")

  await ctx.send(embed=embed)

@help.command()
async def snipe(ctx):

  embed = discord.Embed(title = "**Snipe**", description = "Says the last deleted message.", color = ctx.author.color)

  embed.add_field(name = "Permission level", value = "Everyone")

  embed.add_field(name = "**Usage**", value = f"{prefix}snipe")

  await ctx.send(embed=embed)

@help.command()
async def dm(ctx):

  embed = discord.Embed(title = "**dm**", description = "Sends a DM to a member.", color = ctx.author.color)

  embed.add_field(name = "Permission level", value = "Everyone")

  embed.add_field(name = "**Usage**", value = f"{prefix}dm <member> [message]")

  await ctx.send(embed=embed)

@help.command()
async def ping(ctx):

  embed = discord.Embed(title = "**Ping**", description = "Tells you what your ping is.", color = ctx.author.color)

  embed.add_field(name = "Permission level", value = "Everyone")

  embed.add_field(name = "**Usage**", value = f"{prefix}ping")

  await ctx.send(embed=embed)

@help.command()
async def rules(ctx):

  embed = discord.Embed(title = "**Rules**", description = "Tells you what the rules are.", color = ctx.author.color)

  embed.add_field(name = "Permission level", value = "Everyone")

  embed.add_field(name = "**Usage**", value = f"{prefix}rules")

  await ctx.send(embed=embed)

@help.command()
async def startYT(ctx):

  embed = discord.Embed(title = "**StartYT**", description = "Starts Youtube in Discord.", color = ctx.author.color)

  embed.add_field(name = "Permission level", value = "Everyone")

  embed.add_field(name = "**Usage**", value = f"{prefix}startYT")

  await ctx.send(embed=embed)

@help.command()
async def chess(ctx):

  embed = discord.Embed(title = "**Chess**", description = "Starts a game of chess in Discord.", color = ctx.author.color)

  embed.add_field(name = "Permission level", value = "Everyone")

  embed.add_field(name = "**Usage**", value = f"{prefix}chess")

  await ctx.send(embed=embed)

@help.command()
async def help(ctx):

  embed = discord.Embed(title = "**Help**", description = "Shows you the help message.", color = ctx.author.color)

  embed.add_field(name = "Permission level", value = "Everyone")

  embed.add_field(name = "**Usage**", value = f"{prefix}help")

  await ctx.send(embed=embed)


client.run(TOKEN)
