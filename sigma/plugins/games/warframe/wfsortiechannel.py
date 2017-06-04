import discord
from sigma.core.permission import check_admin

async def wfsortiechannel(cmd, message, args):
    if check_admin(message.author, message.channel):
        if message.channel_mentions:
            target_channel = message.channel_mentions[0]
        else:
            if args:
                if args[0].lower() == 'disable':
                    cmd.db.set_settings(message.guild.id, 'WarframeSortieChannel', None)
                    response = discord.Embed(title=f'✅ Warframe Sortie Channel Disabled', color=0x66CC66)
                    await message.channel.send(embed=response)
                    return
                else:
                    return
            else:
                target_channel = message.channel
        cmd.db.set_settings(message.guild.id, 'WarframeSortieChannel', target_channel.id)
        response = discord.Embed(title=f'✅ Warframe Sortie Channel set to #{target_channel.name}', color=0x66CC66)
    else:
        response = discord.Embed(title='⛔ Unpermitted. Server Admin Only.', color=0xDB0000)
    await message.channel.send(embed=response)
