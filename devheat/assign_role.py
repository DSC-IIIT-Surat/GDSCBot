import discord

target_server_id = "123..."
target_role_id   = "456..."

@bot.command(pass_context=True)
async def gimmieRole(bot, ctx):
    if not ctx.message.channel.is_private:
        await bot.say("Private command only")
    server = await bot.get_Server(target_server_id)
    role = discord.utils.get(server.roles, id=target_role_id)
    member = server.get_member(ctx.message.author.id)
    if member:
        await bot.add_roles(member, role)
    else:
        await bot.say("You are not a member")