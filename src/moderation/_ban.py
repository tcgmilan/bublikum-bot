import discord
async def main(ctx, member : discord.Member, reason, config):
    try:
        await member.kick()
    except:
        embed = 