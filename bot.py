import discord
from discord.ext import commands


class Bot(commands.Bot):

    def __init__(self):
        super(Bot, self).__init__(command_prefix=['//'])

    async def on_ready(self):
        print(f'Logged in as {self.user.name} | {self.user.id}')




    @commands.command(name='connect')
    async def connect_(self, ctx, *, channel: discord.VoiceChannel = None):
        

   

bot = Bot()
bot.run('YoUr NiCE ToKEn')
