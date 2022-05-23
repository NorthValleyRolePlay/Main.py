import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(commands_prefix="!")

@client.event
async def on_ready();
   print("Online")
  
  @client.event
  async def on_member_join(member):
    channel = client.get_channel(977340438048567379)
    embed=discord.Embed(title=f"Welcome {member.name",description="Welcome to this server\n thank you for joining",color=0x9208ea
    embed.set_thumbnail(url=mmeber.avatar_url)
    embed.set_footer(text="Hello")


    await channel.send(embed=embed)
   

    @client.command(pass_context=True)
    async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}")
  
    client.run("OTc1MDY0ODc0MjY4ODg1MDIy.GYOxuq.4pJdkSbJvtkehulPkiCWVtKwxVIneM7SM4n5HI")
