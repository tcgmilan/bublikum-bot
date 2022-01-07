from os import stat
import discord
from mcstatus import MinecraftServer

async def main(config):
    ip = config["minecraft"]["ip"]
    server = MinecraftServer.lookup(ip)
    status = server.status()

    max = status.players.max
    online = status.players.online
    dc = status.description
    icon = status.favicon
    version = status.version
    ping = status.latency

    embed = discord.Embed(title = f"[{version.name}] | Minecraft Server", description = dc, color = 0x00ff00)
    embed.add_field(name = "Maximum Játékos", value = max, inline=True)
    embed.add_field(name = "Online Játékos", value = online, inline=True)
    embed.set_footer(text=f"IP: {ip} | PING: {ping}ms")

    return embed
