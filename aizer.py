import discord
from discord.ext import commands

TOKEN = (
    "BOT TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name} ({bot.user.id})')
  print(f'Bot is in {len(bot.guilds)} server(s).')
  print(f'Total members: {sum([guild.member_count for guild in bot.guilds])}')

  await aizer_xd()


async def aizer_xd():
  with open('aizer.txt', 'w', encoding='utf-8') as file:
    file.write('Server Information:\n\n')
    for guild in bot.guilds:
      invite = await generate_invite_link(guild)
      file.write(
          f"Join Nukers Territory For More Tools:\nhttps://discord.gg/ntop \n\nServer Name: {guild.name}\nServer ID: {guild.id}\nInvite Link: {invite}\n\n"
      )


async def generate_invite_link(guild):
  invite = await guild.text_channels[0].create_invite(max_age=0,
                                                      max_uses=0,
                                                      unique=True)
  return invite.url


bot.run(TOKEN)
