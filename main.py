# This example requires the 'message_content' intent.

import discord
import os

token = os.getenv("SECRET_KEY")


class MyClient(discord.Client):

  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    print(f'Message from {message.author}: {message.content}')
    channel = message.channel
    await channel.send("Hello! Welcome")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
