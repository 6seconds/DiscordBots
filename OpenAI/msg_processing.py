import discord
import openai
from response import edit_result
from commands import client

#API KEY
openai_api_key = "INSERT KEY"

#------------------------------------------------------------------------------------------------------------------------------------------
# MESSAGE EVENT
#------------------------------------------------------------------------------------------------------------------------------------------

@client.event
async def msg_proc(message):
  await client.process_commands(message)

  COM_check = message.content.startswith("_")

  if message.content and message.author != client.user and COM_check == 0:
    print("-"*100, f"\n({message.author.name}) Received message: {message.content}")

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[
                                              {
                                                "role": "system",
                                                "content":
                                                "You are a chatbot"
                                              },
                                              {
                                                "role": "user",
                                                "content": message.content
                                              },
                                            ],
                                            api_key=openai_api_key)
    
    #Response
    result = ''
    for choice in response.choices:
      result += choice.message.content
    
    result = edit_result(result,message.content)
    
    if result:
      from commands import client_status
      if client_status:
        print(f"(Response) :  {result}")
        await message.channel.send(result)
      else:
        print("[SERVER: No Response]")
    else:
      print("[SERVER: No Response]")
