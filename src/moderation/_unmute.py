import discord

async def main(ctx, member : discord.Member, config):
    id = int(config["moderation"]["muted_role_id"])
    mute_role = ctx.guild.get_role(id)
    if mute_role not in member.roles:
        embed = discord.Embed(title = config["mute"]["already_unmuted"].replace("$target", member.display_name))
        return embed
    else:
        try:
            await member.remove_roles(mute_role)
            embed = discord.Embed(title = config["mute"]["unmuted"].replace("$target", member.display_name).replace("$author", ctx.author.name), color = 0x00ff00)
        except:
            embed = discord.Embed(title = config["mute"]["cant_unmute"])
        finally:
            return embed