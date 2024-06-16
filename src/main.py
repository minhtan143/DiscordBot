import os, discord, subprocess
from discord.ext import commands
from typing import Literal


# Define intents
intents = discord.Intents.all()

# Create a bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# @bot.command()
# async def shop(ctx, buy_sell: Literal['buy', 'sell'], amount: Literal[1, 2], *, item: str):
#     await ctx.send(f'{buy_sell.capitalize()}ing {amount} {item}(s)!')

# @bot.command()
# async def nat_hello(ctx):
#     await ctx.send("Command")

@bot.tree.command() 
async def nat_hello(interaction: discord.Interaction): 
  await interaction.response.send_message(f'Hello, {interaction.user.mention}') 

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    bot.tree.copy_global_to(guild=bot.guilds[0])
    await bot.tree.sync(guild=bot.guilds[0])


# Event handler for when a message is received
# @bot.event
# async def on_message(message):
#     # Ignore messages from the bot itself to prevent an infinite loop
#     if message.author == bot.user:
#         return

#     await message.channel.send(f'Hello, {message.author.mention}!')

#     # Add more commands or conditions as needed

#     # Let the bot process other commands if any
#     await bot.process_commands(message)


# Run the bot with the token
bot.run(
    token=os.environ['TOKEN']
)

# https://discord.com/api/oauth2/authorize?client_id=1191783216542121994&permissions=8&scope=bot%20applications.commands
