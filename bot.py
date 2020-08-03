import discord
from discord.ext import commands


class Bot(commands.Bot):

    def __init__(self):
        super(Bot, self).__init__(command_prefix=['//'])

        self.add_cog(bot(self))

    async def on_ready(self):
        print(f'Logged in as {self.user.name} | {self.user.id}')


class bot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello')
    async def hello(self, ctx):
        await ctx.send('hi')

   


bot = Bot()
bot.run('YoUR NiCE ToKEn')
