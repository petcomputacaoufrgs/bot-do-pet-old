import os
import discord
import datetime
import pytz
from discord.ext import commands, tasks
#from discord.ui import Button, View

#Constants
PETIANES = os.environ['PETIANES_ID']
logchannel = os.environ['LOG_CHANNEL']
key_holder = 0
command_starts = ("pet.")


class Key_commands(commands.Cog):
    """Commands about the PET's room key"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.check_key.start()

    @commands.command(name="peguei")
    async def got_the_key(self, ctx):
        global logchannel
        if int(ctx.channel.id) == int(logchannel):
            global key_holder
            global command_starts

            def check_rules(m):
                return (m.author == self.bot.user) or (
                    (command_starts in m.clean_content.lower()) and
                    (m.pinned == False))

            await ctx.channel.purge(check=check_rules)

            #button1 = Button(label = "Teste", style = discord.ButtonStyle.green)
            #view = View()
            #view.add_item(button1)
            #await ctx.send("Teste", view=view)

            key_holder = ctx.author.id

            em = discord.Embed(color=0xFFFFFF)
            em.add_field(name=f"**Cadê a chave?**",
                         value=f"Atualmente está com <@{key_holder}>.",
                         inline=False)
            await ctx.send(embed=em)
        else:
            await ctx.send(
                f"Tá usando o comando no canal errado, animal. Tenta de novo no <#{logchannel}>!"
            )

    @commands.command(name="passei")
    async def passed_the_key(self, ctx, arg):
        global logchannel
        if int(ctx.channel.id) == int(logchannel):

            global key_holder
            global command_starts

            def check_rules(m):
                return (m.author == self.bot.user) or (
                    (command_starts in m.clean_content) and
                    (m.pinned == False))

            await ctx.channel.purge(check=check_rules)

            key_holder = arg

            em = discord.Embed(color=0xFFFFFF)
            em.add_field(name=f"**Cadê a chave?**",
                         value=f"Atualmente está com {key_holder}.",
                         inline=False)
            await ctx.send(embed=em)
        else:
            await ctx.send(
                f"Tá usando o comando no canal errado, animal. Tenta de novo no <#{logchannel}>!"
            )

    @commands.command(name="devolvi")
    async def returned(self, ctx):
        global logchannel
        if int(ctx.channel.id) == int(logchannel):

            global key_holder
            global command_starts

            def check_rules(m):
                return (m.author == self.bot.user) or (
                    (command_starts in m.clean_content) and
                    (m.pinned == False))

            await ctx.channel.purge(check=check_rules)

            key_holder = 0
            em = discord.Embed(color=0xFFFFFF)
            em.add_field(
                name=f"**Cadê a chave?**",
                value=f"Está na recepção. Qualquer coisa, converse com a tia!",
                inline=False)
            await ctx.send(embed=em)
        else:
            await ctx.send(
                f"Tá usando o comando no canal errado, animal. Tenta de novo no <#{logchannel}>!"
            )

    @commands.command(name="chave")
    async def key(self, ctx):
        global logchannel
        if int(ctx.channel.id) == int(logchannel):

            global key_holder
            global command_starts

            def check_rules(m):
                return (m.author == self.bot.user) or (
                    (command_starts in m.clean_content) and
                    (m.pinned == False))

            await ctx.channel.purge(check=check_rules)

            if (key_holder == 0):
                em = discord.Embed(color=0xFFFFFF)
                em.add_field(
                    name=f"**Cadê a chave?**",
                    value=
                    f"Está na recepção. Qualquer coisa, converse com a tia!",
                    inline=False)
            else:
                if ("@" in str(key_holder)):
                    em = discord.Embed(color=0xFFFFFF)
                    em.add_field(name=f"**Cadê a chave?**",
                                 value=f"Atualmente está com {key_holder}.",
                                 inline=False)
                else:
                    em = discord.Embed(color=0xFFFFFF)
                    em.add_field(name=f"**Cadê a chave?**",
                                 value=f"Atualmente está com <@{key_holder}>.",
                                 inline=False)
            await ctx.send(embed=em)
        else:
            await ctx.send(
                f"Tá usando o comando no canal errado, animal. Tenta de novo no <#{logchannel}>!"
            )

    @commands.command(name="clear")
    async def clear_msg(self, ctx):
        global logchannel
        if int(ctx.channel.id) == int(logchannel):

            def check_rules(m):
                return (m.author != self.bot.user) and (m.pinned == False)

            await ctx.channel.purge(check=check_rules)
        else:
            await ctx.send(
                f"Tá usando o comando no canal errado, animal. Tenta de novo no <#{logchannel}>!"
            )

    @tasks.loop(hours=1)
    async def check_key(self):
        global key_holder
        now = datetime.datetime.now(pytz.timezone('Brazil/East'))
        channel = self.bot.get_channel(int(logchannel))
        if now.hour > 17:
            if key_holder != 0:
                await channel.send(f"Tu ainda ta com a PORRA da chave, <@{key_holder}>?")
        if now.hour == 0:
            def check_rules(m):
                return (m.author != self.bot.user) and (m.pinned == False)

            await channel.purge(check=check_rules)


async def setup(bot):
    await bot.add_cog(Key_commands(bot))
