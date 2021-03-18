from discord.ext.commands import Cog


def register_cogs(bot, *cogs):
    for cog_class in cogs:
        if cog_class is None:
            continue
        cog: Cog = cog_class(bot)
        bot.add_cog(cog)
