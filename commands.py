import random
import discord
import difflib

import asyncio

async def check_command_list(cmd_list, client, message):
	r = []
	for cmd in cmd_list:
		_r = await launch_command(client, cmd, message)
		r.append(_r)

	# await asyncio.sleep(1)

	# print(r)

	if not 1 in r:
		if len(message.content) < 4:
			return
		# x = difflib.SequenceMatcher(None, message.content[:4], "!mhg").quick_ratio()
		if "!mhg" == message.content[:4].lower():
			await send_help_message(message, custom_title=f"Oops, je ne connais pas la commande {message.content}...")
		elif difflib.SequenceMatcher(None, message.content[:4], "!mhg").quick_ratio() == 1.0: #1.0 is same letters but different order, 0.75 is 3 commun letters
			await message.channel.send(f"Tu veux dire \'!mhg\' ? Sinon je m'en vais...")


async def launch_command(client, command, message):
	return await command(client, message)

async def bot_help(client, message):
	if message.content.lower() != '!mhg help':
		return -1

	await send_help_message(message)
	return 1

async def send_help_message(message, custom_title=None):
	
	title = "MHBot à la rescousse !!" if custom_title == None else custom_title
	embedVar = discord.Embed(title=title, description="Voici l'aide pour utiliser toutes mes commandes !", color=0x00ff00)
	
	embedVar.add_field(name="!mhg help", value="Celui là tu la connais j'en suis sûr, c'est ce qui affiche l'aide !", inline=False)
	
	await message.channel.send(embed=embedVar)

command_list = [bot_help]