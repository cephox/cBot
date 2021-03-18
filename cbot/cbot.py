import os

from discord.ext.commands import AutoShardedBot

import logger
from database.database import db
from info import GITHUB_LINK

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

bot.run(os.environ["TOKEN"])
