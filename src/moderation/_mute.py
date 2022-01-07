import discord

async def main(ctx, member : discord.Member, reason, config):
    id = int(config["moderation"]["muted_role_id"])
    mute_role = ctx.guild.get_role(id)
    if mute_role in member.roles:
        embed = discord.Embed(title = config["mute"]["already_muted"].replace("$target", member.display_name))

        return embed
    else:
        try:
            await member.add_roles(mute_role)
            reason = " ".join(reason)
            embed = discord.Embed(title = config["mute"]["muted"].replace("$target", member.display_name).replace("$author", ctx.author.name), description = f"Indok: {reason}", color = 0xff0000)
        except:
            embed = discord.Embed(title = config["mute"]["cant_mute"])
        finally:
            return embed