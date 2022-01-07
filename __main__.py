import discord
import inspect
import configparser
import datetime
import json
from discord import activity
from discord.ext.commands import *
from discord.ext.tasks import *
from discord_components import *

from src.servers import minecraft_server, scp_server
from src.moderation import _mute, _unmute


def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_command(user, process_name):
    log = open(log_path, "a", encoding="utf8")
    log.write(f"[{now()}] - {user} lefuttatta ezt a parancsot: {process_name}\n")
    log.close()

config = configparser.ConfigParser()
config.read("settings.ini")

activity = discord.Activity(type = discord.ActivityType.watching, name = "Fejlesztés Alatt @tcgmilan")
status = discord.Status.dnd

bot = Bot(command_prefix=config["bot"]["prefix"], activity = activity, status = status)
DiscordComponents(bot)
guild = None


log_path = config["logging"]["log_path"] + config["logging"]["log_name"].replace("$date", now()) + ".txt"
log = open(log_path, "a", encoding="utf8")

mc_message = None
scp_message = None


@bot.event
async def on_ready():
    global guild
    guild = bot.get_guild(886920763368701982)
    print(f"[{now()}] » Bot Elindult!")
    print(f"[{now()}] » Logolás Elindult! (" + log_path + ")")

    mc_log.start(discord.utils.get(guild.channels, id = int(config["minecraft"]["channel"])))
    #scp_log.start(discord.utils.get(guild.channels, id = int(config["scp"]["channel"])))


@bot.command()
@has_any_role(*json.loads(config.get("mute","allowed_roles")))
async def mute(ctx, member : discord.Member, *reason : str):
    global guild
    log_command(ctx.author, inspect.stack()[0][3])
    await ctx.send(embed = await _mute.main(ctx, member, reason, config))


@bot.command()
@has_any_role(*json.loads(config.get("mute","allowed_roles")))
async def unmute(ctx, member : discord.Member):
    global guild
    log_command(ctx.author, inspect.stack()[0][3])
    await ctx.send(embed = await _unmute.main(ctx, member, config))


@bot.command()
async def ping(ctx):
    log_command(ctx.author, inspect.stack()[0][3])
    await ctx.send("Pong!")

@loop(seconds = int(config["scp"]["refresh"]))
async def scp_log(scp_message_channel):
    global scp_message

    await scp_message_channel.purge(limit = 10)

    await scp_message_channel.send(embed = await scp_server.main(config))

    log_command("Szerver", inspect.stack()[0][3])

@loop(seconds = int(config["minecraft"]["refresh"]))
async def mc_log(mc_message_channel):
    global mc_message

    await mc_message_channel.purge(limit = 10)

    await mc_message_channel.send(embed = await minecraft_server.main(config))
    
    log_command("Szerver", inspect.stack()[0][3])




bot.run(config["bot"]["token"])


