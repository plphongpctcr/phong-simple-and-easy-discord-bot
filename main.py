import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
token = "" # Bot OAuth2 Token

@client.event
async def on_ready():
    print('Logged in: ', client.user) # show on console
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='Hello, World!'))

@client.command(pass_context=True)
async def report(ctx, *, text = None):
    if isinstance(ctx.channel, discord.DMChannel):
        if text is None:
            await ctx.author.send("```Usage: !report [content]```")
        else:
            admin_channel = client.get_channel(605000000012345678) # Channel ID
            await admin_channel.send("@everyone **{}**({}) : {}".format(ctx.author, ctx.author.id, text))
            await ctx.author.send("**INFO:** A message was sent to the server administrator.")
    else:
        await ctx.message.delete()
        await ctx.author.send("**ERROR:** The report command is only available on the DM channel.\nPlease re-enter the command here.\n**You Entered:**\n```!report {}```".format(text))


@client.command(pass_context=True)
async def nick(ctx, *, nickname):
    try:
        await ctx.message.delete()
        await ctx.author.edit(nick=nickname)
    except discord.errors.Forbidden:
        await ctx.author.send("**ERROR:** Permission Denied")
    else:
        await ctx.author.send("**INFO:** Your nickname has been changed.")

client.run(token)