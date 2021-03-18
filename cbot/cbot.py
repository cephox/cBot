import os

from discord.ext.commands import AutoShardedBot

import logger
from cogs import COGS
from database.database import db
from info import GITHUB_LINK
from utils.cog import register_cogs

logger = logger.logger

print(
    "\u001b[38;5;10m"
    r"""
              ____        __
        _____/ __ )____  / /_
       / ___/ __  / __ \/ __/
      / /__/ /_/ / /_/ / /_
      \___/_____/\____/\__/
    """
    "\u001b[0m"
)

logger.info("Starting cBot (%s)", GITHUB_LINK)
db.create_tables()

bot = AutoShardedBot(command_prefix="-", case_insensitive=True)
bot.remove_command("help")


@bot.event
async def on_ready():
    logger.info("Logged in as %s", bot.user)


enabled_cogs = []
for cog in COGS:
    enabled_cogs.append(cog)

register_cogs(bot, *enabled_cogs)

if bot.cogs:
    print()
    logger.info("\033[1m\033[32m%s Cog%s enabled:\033[0m", len(bot.cogs), "s" if len(bot.cogs) > 1 else "")
    for cog in bot.cogs.values():
        commands = ", ".join(cmd.name for cmd in cog.get_commands())
        logger.info(" + %s %s", cog.__class__.__name__, str(commands) if commands else "")
    print()

bot.run(os.environ["TOKEN"])
