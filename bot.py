# bot.py
import os
import random
import discord

import myglobals as mg
import commands

client = discord.Client()

@client.event
async def on_ready():

	mhg = discord.utils.get(client.guilds, name=mg.GUILD)
	print(
		f'{client.user} is connected to the following guild:\n'
		f'{mhg.name}(id: {mhg.id})'
	)

	mhg_members = '\n - '.join([member.name for member in mhg.members])
	print(f'MHG Members:\n - {mhg_members}')

	activity = discord.Activity(name='ta maison', type=discord.ActivityType.watching)
	await client.change_presence(activity=activity)

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	print(f'{message.guild.name}.{message.channel}.{message.created_at} by {message.author} : {message.content}')

	# brooklyn_99_quotes = [
	# 	'I\'m the human form of the 💯 emoji.',
	# 	'Bingpot!',
	# 	(
	# 		'Cool. Cool cool cool cool cool cool cool, '
	# 		'no doubt no doubt no doubt no doubt.'
	# 	),
	# ]

	# if message.content == '99!':
	# 	response = random.choice(brooklyn_99_quotes)
	# 	await message.channel.send(response)

	# await commands.launch_command(client, commands.help, message)

	await commands.check_command_list(commands.command_list, client, message)



client.run(mg.TOKEN)
