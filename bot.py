import discord
from discord.ext import commands

# تابع برای دریافت توکن از کاربر
def get_token():
    token = input("Enter Bot Token: ")
    return token

# تنظیم توکن ربات
token = get_token()

# ساخت شیء کلاینت دیسکورد
bot = commands.Bot(command_prefix='!')

# رویداد آماده بودن ربات
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('------')

# کامند برای بن کردن یک کاربر
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
    await member.ban()
    await ctx.send(f'{member.mention} banned!')

# کامند برای کیک کردن یک کاربر
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f'{member.mention} kicked!')

# اتصال ربات به سرور دیسکورد
bot.run(token)
