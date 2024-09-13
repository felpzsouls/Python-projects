import discord;

class MyClient(discord.Client):
  async def on_ready(self):
    print(f'Bot online {self.user}');

  async def on_message(self, msg):
    print(f'mensagem de {msg.author}: {msg.content}');

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('bot token')
