import discord
from commands import client
from msg_processing import msg_proc

#------------------------------------------------------------------------------------------------------------------------------------------
# MESSAGE EVENT
#------------------------------------------------------------------------------------------------------------------------------------------

@client.event
async def on_message(message):
  await msg_proc(message)

#------------------------------------------------------------------------------------------------------------------------------------------
# RUNNING
#------------------------------------------------------------------------------------------------------------------------------------------
TOKEN = "MTA4Mzc2ODMxODY4MDM4MzUyMA.GJwPqU.rmbgrXsTbFyqaQAKNYqLFum5l_F9sb-A5FuyI4"


if TOKEN:
  client.run(TOKEN)