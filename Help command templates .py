@client.group(invoke_without_command=True)
async def help(ctx,):
  embed = discord.Embed(title = "Help", description = f"Do {prefix}help <command> for more information on the command.",color = ctx.author.color)

  embed.add_field(name = "Moderation", value = "`COMMAND1` , `COMMAND2` , `COMMAND3`")
  embed.add_field(name = "Misc and fun", value = "`COMMAND1` , `COMMAND2` , `COMMAND3`")

  await ctx.send(embed=embed)

@help.command()
async def COMMAND_NAME(ctx):

  embed = discord.Embed(title = "**COMMAND_NAME**", description = "COMMAND DESCRIPTION", color = ctx.author.color)

  embed.add_field(name = "Permission level", value = "Everyone")

  embed.add_field(name = "**Usage**", value = f"{prefix}COMMAND_NAME")

  await ctx.send(embed=embed)
