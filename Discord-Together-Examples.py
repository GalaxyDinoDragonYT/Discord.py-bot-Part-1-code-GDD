#For Youtube

@client.command()
async def startYT(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Click the blue link!\n{link}")
    
#For Chess

@client.command()
async def startYT(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'chess')
    await ctx.send(f"Click the blue link!\n{link}")
    
#For fishing 

@client.command()
async def startYT(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'fishing')
    await ctx.send(f"Click the blue link!\n{link}")
    
 #For poker

@client.command()
async def startYT(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'poker')
    await ctx.send(f"Click the blue link!\n{link}")
    
 #For betrayal 

@client.command()
async def startYT(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'betrayal')
    await ctx.send(f"Click the blue link!\n{link}")
    
 #For a custom app

@client.command()
async def startYT(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'CUSTOM_APP_ID_HERE')
    await ctx.send(f"Click the blue link!\n{link}")
