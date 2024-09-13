import discord
from colorama import Fore
from discord import Embed, Intents, Member, app_commands, Interaction, Role, TextChannel, Embed
from discord.ext import commands
from matplotlib.dvired import Page
from response import get_response

intents = Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix = '!', intents = intents)
async def send_message(message: discord.Message, user_message: str) -> None:
  if not user_message:
    print('mensagem vazia mano?')
    return
  if is_private := user_message[0] == '#':
    user_message = user_message[1:]

  try:
    response : str = get_response(user_input=user_message)
    await message.author.send(response) if is_private else await message.channel.send(response)

  except Exception as e:
    print(f'Ocorreu um erro: {e}')


@bot.event
async def on_ready(self):
  print(Fore.GREEN + f'bot online {self.user}')
  try:
    synced = await bot.tree.sync()
    print(Fore.YELLOW + f'Synced {len(synced)} command(s)')
    print(Fore.RED + '---------------------------------------')

  except Exception as e:
    print(Fore.RED + f'Ocorreu um erro: {e}')

@bot.event
async def member_join(member: Member) -> None:
  welcome_channel_id = '1284138748468265041'
  welcome_channel = bot.get_channel(welcome_channel_id)
  if welcome_channel:
    embed = Embed(title='Bem-vindo(a) ao servidor!', description=f'Olá {member.mention}, bem vindo ao {member.guild.name}', color = discord.Color.green())
    await welcome_channel.send(embed=embed)

@bot.tree.command(name = 'member_count' , description = 'Mostra a quantidade de membros no servidor')
async def member_count(interaction: discord.Interaction) -> None:
  member_count = interaction.guild.member_count
  await interaction.response.send_message(f'O servidor tem {member_count} membros!')

@bot.tree.command(name = 'ping' , description = 'Mostra o ping do bot')
async def ping(interaction: discord.Interaction) -> None:
  latency = round(bot.latency * 1000)
  await interaction.response.send_message(f'Pong! Latência: {latency}ms!')

@bot.tree.command(name = 'warn' , description = 'Avisa um membro')
@app_commands.check.has_permissions(manage_messages = True)
async def warn(interaction: discord.Interaction, member: discord.Member, reason: str) -> None:
  await interaction.response.send_message(f'O membro {member.mention} foi avisado por {reason}')
  await member.send(f'Você foi avisado no servidor {interaction.guild.name} por {reason}')

@bot.tree.command(name = 'clear' , description = 'Limpa mensagens')
@app_commands.check.has_permissions(manage_messages = True)
async def clear(interaction: discord.Interaction, amount: int):
  await interaction.channel.purge(limit = amount + 1)

@bot.event
async def on_message(message: discord.Message) -> None:
  if message.author == bot.user:
    return
  user_name : str = str(message.author)
  user_message : str = message.content
  channel : str = str(message.channel)

  await send_message(message, user_message)


def main() -> None:
  bot.run('your token')

if __name__ == '__main__':
  main()
