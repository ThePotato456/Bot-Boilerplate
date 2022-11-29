import discord
from discord.ext import commands
import os
import dotenv


if __name__ == "__main__":
    dotenv.load_dotenv()
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    COMMAND_PREFIX = os.getenv('COMMAND_PREFIX')
    bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents = discord.Intents.all())
    CLIENT_ID = os.getenv('CLIENT_ID')
    INVITE_LINK = os.getenv('OAUTH_LINK')

    @bot.event
    async def on_ready():
        print('[bot] Logged in as {0} ({0.id})'.format(bot.user))
        print(f'[bot] Interact with it using the prefix \'{COMMAND_PREFIX}\'')
        print('[bot] Invite to your server with this link: {0}'.format(INVITE_LINK))

    for file in os.listdir('cogs'):
        if file.endswith(".py"):
            name = file[:-3]
            print(f"[init] Loading cogs.{name}")
            bot.load_extension(f"cogs.{name}")
    bot.run(DISCORD_TOKEN)