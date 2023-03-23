import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.dm_messages = True
intents.members = True

client = commands.Bot(command_prefix="_", intents=intents)

client_status = True
#------------------------------------------------------------------------------------------------------------------------------------------
# BOT SETUP
#------------------------------------------------------------------------------------------------------------------------------------------

@client.event
async def on_ready():
  await client.change_presence(status = discord.Status.idle, activity = discord.Streaming(name="watch my queen w/me", url='https://www.twitch.tv/amouranth'))
  print('We have logged in as {0.user}'.format(client))

  try:
    synced = await client.tree.sync()
    print(f"Synced{len(synced)} command(s)")
  except Exception as e:
    print(e)


#------------------------------------------------------------------------------------------------------------------------------------------
# SLASH COMMANDS
#------------------------------------------------------------------------------------------------------------------------------------------

@client.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
  await interaction.response.send_message(f"Hey {interaction.user.mention}!")

@client.tree.command(name="shut")
async def shut(interaction: discord.Interaction):
  await interaction.response.send_message(f"{interaction.user.mention}, I have committed shut. If you wish for me to speak, then you must `unshut` me.")
  global client_status 
  client_status = False

@client.tree.command(name="unshut")
async def unshut(interaction: discord.Interaction):
  await interaction.response.send_message(f"{interaction.user.mention}, I have committed unshut. If you wish for me to not speak, then you must `shut` me.")
  global client_status
  client_status = True

#------------------------------------------------------------------------------------------------------------------------------------------
# COMMANDS
#------------------------------------------------------------------------------------------------------------------------------------------

@client.command(name="DM")
async def send_message(ctx, user_id: int, *, message: str):
  user = await client.fetch_user(user_id)
  if user:
    if not user.dm_channel:
      await user.create_dm()
    await user.send(message)
    await ctx.send(f"Sent message to {user.mention}.")
    print("-"*100, f"\n\n{ctx.author.name} sent a message to {user.name}\n")
  else:
    await ctx.send("User not found.")

@client.command(name="CM")
async def send_annoucement(ctx, channel_id: int, *message: str):
	channel = client.get_channel(channel_id)
	if channel and ctx.author.id == 326339687184728064:
		string = " ".join(message)
		await channel.send(string)
		await ctx.send(f"Sent message to {channel_id}")
	else:
		await ctx.send("Channel not found.")
