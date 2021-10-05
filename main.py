import datetime
import randfacts
import pymongo, dns
from pymongo import MongoClient
import random
import json
import asyncio
from typing import List
import string
import os
import anime_images_api

anime = anime_images_api.Anime_Images()
import platform
os.system("pip uninstall discord.py -y")
os.system("pip uninstall discord -y")
os.system("pip install pip install -U git+https://github.com/Pycord-Development/pycord")
import discord

import datetime
import randfacts
import discord

import pymongo, dns
from pymongo import MongoClient
import random

import texttoimage

import lavalink
from yiffparty import horni

from discord.ext import commands

from waifu import WaifuClient

imgapi = WaifuClient()
import json
import aiohttp
import asyncio
from WEB import keep_alive
from typing import List
import string
import os
import anime_images_api

anime = anime_images_api.Anime_Images()
import platform

helpcmd = """

__**🛠️ Moderation**__
`warn`<user> <reason>  -> *warn a user*
`deletewarn` <id> -> *deletes a user's warnings*
`warns` <user> -> *check a user's warnings*

__**🎉 Fun**__
`randomfact` -> *get a random fact!*

__**📊 Info**__
`botinfo` -> *view info of the bot's creation, or its stats.*
`emojis` -> *view your server's emojis*
`checkadmin` -> (user) *check if a user is an admin*

__**🤔 More **__
`poll` -> <channel> <poll_question>*host a poll with your friends or community*
`giveaway` -> <channel> <prize> <duration> *start a giveaway*

__**🖼️ Images**__
`slap` <user> *slap a user.*
`hug` <user> *hug a user.*
`kiss` <user> *kiss a user.*
__**🔞 NSFW**__
[these commands can only be used in a nsfw channel]
`hentai` -> *get some anime porn.*
`porn` -> *get some general porn.*
`gay` -> *get some gay porn.*

"""
client = MongoClient("mongodb+srv://pop:pop@pbl.iljrt.mongodb.net/testdb?retryWrites=true&w=majority")
auth_url = "mongodb+srv://pop:pop@pbl.iljrt.mongodb.net/testdb?retryWrites=true&w=majority"
ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
        "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]

twenties = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]

thousands = ["", "thousand ", "million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ",
             "septillion ", "octillion ", "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ",
             "quattuordecillion ", "quindecillion", "sexdecillion ", "septendecillion ", "octodecillion ",
             "novemdecillion ", "vigintillion "]


def num999(n):
    c = n % 10  # singles digit
    b = ((n % 100) - c) / 10  # tens digit
    a = ((n % 1000) - (b * 10) - c) / 100  # hundreds digit
    t = ""
    h = ""
    if a != 0 and b == 0 and c == 0:
        t = ones[a] + "hundred "
    elif a != 0:
        t = ones[a] + "hundred and "
    if b <= 1:
        h = ones[n % 100]
    elif b > 1:
        h = twenties[b] + ones[c]
    st = t + h
    return st
print(horni.newest("gay"))


def num2word(num):
    i = 3
    n = str(num)
    word = ""
    k = 0
    while (i == 3):
        nw = n[-i:]
        n = n[:-i]
        if int(nw) == 0:
            word = num999(int(nw)) + thousands[int(nw)] + word
        else:
            word = num999(int(nw)) + thousands[k] + word
        if n == '':
            i = i + 1
        k += 1
    return word[:-1]


print("number wordlist loaded.")
print(num2word(1))
print("Pymongo loaded.")
data = client['testdb']
collection = data['test']
warnsdb = data.warningdb
configdb = data.configdb
print("databases loaded.")
def get_prefix(client, message):
        result =  configdb.find_one({"guild_id": str(message.guild.id)}) 
        if result is None:

                warning = {
                  "welcomemsg": "none",
                  "welcomechannel": "none",
                  "prefix": "$",
                  "modrole": "none",
                  "logs": "none",
                  "guild_id": str(message.guild.id)
                } 
                post_id = configdb.insert_one(warning).inserted_id
                result =  configdb.find_one({"guild_id": str(message.guild.id)}) 
        prefix = result["prefix"]
        return prefix

bot = commands.Bot(command_prefix=(get_prefix), help_command=None)
owner = 729975591406796840
norm = 0xDA70D6
danger = 0xFF0000
warning = 0xffa500
success = 0x6cdc61
info = 0x1E90FF
load = "<:info:878791988638543894>"
tick = "<:sucess:878791469144621066>"
cross = "<:cross_box:878803307047579648>"



def get_logs(message):

    logchannel = bot.get_channel(int(guild[str(message.guild.id)]["logs"]))
    return logchannel


def log(logaction, moderator, user, reason):
    embed = discord.Embed(title="Paradox - Logs", description=f"Moderator action: `{logaction}`",
                          color=discord.Color.random())
    embed.add_field(name="Moderator:", value=moderator, inline=True)
    embed.add_field(name="User: ", value=user, inline=True)
    embed.add_field(name="Reason: ", value=reason, inline=False)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text="Paradox - Logs")
    return embed


@bot.slash_command(description="Check if a user is an admin!")
async def checkadmin(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    if user.guild_permissions.administrator:
        await ctx.send(f"{user} is an admin.")
    else:
        await ctx.send(f"{user} is not an admin.")


@bot.slash_command(description="Get a random fact.")
async def randomfact(ctx):
    x = randfacts.get_fact()
    await ctx.send(x)

@bot.command()
async def t2img(ctx, *,text="blank"):
    # It'll generate an image which the font size is 48 and color is red.
    texttoimage.convert(text, image_file=f"{ctx.author.id}.png", color="white")
    await ctx.send(file=discord.File(f'{ctx.author.id}.png'))
    os.remove(f"{ctx.author.id}.png")
@bot.command()
async def test(ctx):
    counter  = 0
    message = await ctx.send("Progress: `-`")
    while True:
        if counter >= 100:
            counter = 100
            await message.edit("Progress: `100%`")
            break
        await asyncio.sleep(0.5)
        counter = random.randrange(counter, 101)
        await message.edit(f"Progress: `{counter}%`")

@bot.slash_command(description="View all the bot's commands!")
async def help(ctx):
    embed = discord.Embed(title="Help", description=helpcmd, color=discord.Color.random())
    await ctx.send(embed=embed)


@bot.slash_command()
async def gay(ctx):
    choices = ["https://cdn1.sunporno.com/thumbs/320x240/572/2013581/2.jpg","https://fi1-ph.ypncdn.com/videos/201906/14/229410912/original/8(m=eKw7Kgaaaa)(mh=kVS_EmSOTCH_hYVX).jpg", "https://icdn03.boy18tube.com/51076/2553763_3.jpg", "https://ei.phncdn.com/videos/201802/26/156110422/original/(m=eaAaGwObaaaa)(mh=L5V0lD9RG1fWAT8W)6.jpg", "https://gaysexboard.com/oj2W6K/thumbs/6/987_danilo-and-douglas.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5inon49po_WlZzqjCYMDvQ0q1IZ4DR-XPpA&usqp=CAU", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp1BKq8qFFOjrAvtaGOa-MWdZgJDG5s3wccA&usqp=CAU"]
    embed = discord.Embed(title="Take some porn!", color=discord.Color.random())
    embed.set_image(url=str(random.choice(choices)))
    await ctx.send(embed=embed)
@bot.event
async def on_member_join(member):
	with open('guild.json', 'r') as f:
		guilds = json.load(f)
	welcomemsg = guilds[str(member.guild.id)]["welcome"]
	welcomechannel = guilds[str(member.guild.id)]["welcomechannel"]
	welcomechannel = bot.get_channel(int(welcomechannel))
	embed = discord.Embed(
	    title=f"👋 Welcome to {member.guild.name}, {member.display_name}!",
	    description=welcomemsg)
	await welcomechannel.send(embed=embed)
@bot.event
async def on_guild_join(guild):
    with open('guild.json', 'r') as f:  #read the prefix.json file
        guilds = json.load(f)  #load the json file
    guilds[str(guild.id)] = {}
    guilds[str(guild.id)]["prefix"] = '$'  #default prefix
    guilds[str(guild.id)]["logs"] = 'none'
    guilds[str(guild.id)]["welcome"] = 'none'
    guilds[str(guild.id)]["welcomechannel"] = 'none'
    guilds[str(guild.id)]["modrole"] = 'none'
    with open('guild.json',
	          'w') as f:  #write in the prefix.json "message.guild.id": "bl!"
        json.dump(
		    guilds, f,
		    indent=4)  #the indent is to make everything look a bit neater
    if guild.system_channel:  # If it is not None
        try:
            await guild.system_channel.send(
            f'Thanks for inviting me to **{guild.name}**! To view all my commands, do `$help` in your server!'
            )
        except:
            return False

    else:
        await guild.owner.send(
		    f"Thanks for inviting me to **{guild.name}**! To view all my commands, do `$help` in your server!"
		)
    await bot.get_channel(885676706428518460).send(
	    f"Paradox was added to **{guild.name}**")

@bot.slash_command(description="View all the emojis in your server.")
async def emojis(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}'s emojis", color=discord.Color.random())
    counter = 0
    for emoji in ctx.guild.emojis:
        if counter >= 25:
            break
        counter += 1
        if emoji.animated == True:
            emojiimg = f"<a:{emoji.name}:{emoji.id}>"
        else:
            emojiimg = f"<:{emoji.name}:{emoji.id}>"
        embed.add_field(name=f"{emojiimg} {emoji.name}", value=f"Id: {emoji.id}", inline=False)
        embed.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar)
    await ctx.send(embed=embed)


@bot.slash_command(description="Warn a user in your server!")
async def warn(ctx, member: discord.Member, *, reason: str):
    S = 50
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k=S))
    warning = {
        "moderator": ctx.author.display_name,
        "member": str(member.display_name),
        "reason": reason,
        "_id": str(ran)
    }
    post_id = warnsdb.insert_one(warning).inserted_id
    await ctx.send(f"{member.mention} has been warned for {reason}!")
    logs = log("warn", ctx.author, member, reason)
    logchannel = get_logs(ctx)
    await logchannel.send(embed=logs)


@bot.slash_command(description="View the warnings for yourself, or a member.")
async def warns(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    counter = 0
    embed = discord.Embed(title="Warnings")
    for warnings in warnsdb.find({"member": str(member.display_name)}).limit(25):
        counter += 1
        mod = warnings["moderator"]
        reason = warnings["reason"]
        mongoid = warnings["_id"]
        embed.add_field(name=f"Moderator: {mod}",
                        value=f"`{reason}` \n\n Id: {mongoid}",
                        inline=False)
    if counter == 0:
        embed = discord.Embed(title=f"❌ {member.display_name} has no warnings.")

    await ctx.send(embed=embed)


@bot.slash_command()
async def deletewarn(ctx, warningid):
    result = warnsdb.find_one({"_id": warningid})
    if result == None:
        await ctx.send("That id is invalid!")
    else:
        warnsdb.delete_one({"_id": warningid})
        await ctx.send("warning deleted")
        logs = log("Warn deleted", ctx.author, "N/A", "N/A")
        logchannel = get_logs(ctx)
        await logchannel.send(embed=embed)


@bot.slash_command(description="View the config for the bot.")
async def config(ctx):
    with open('guild.json', 'r') as f:  # read the prefix.json file
        guilds = json.load(f)  # load the json file
    prefix = guilds[str(ctx.guild.id)]["prefix"]
    log = guilds[str(ctx.guild.id)]["logs"]
    welcome = guilds[str(ctx.guild.id)]["welcome"]
    welcomechannel = guilds[str(ctx.guild.id)]["welcomechannel"]
    modrole = guilds[str(ctx.guild.id)]["modrole"]
    if welcomechannel == "none":
        welcomechannel = "None"
    else:
        welcomechannel = f"<#{welcomechannel}>"
    if modrole == "none":
        modrole = "None"
    else:
        modrole = f"<@&{modrole}>"
    if log == "none":
        log = "none"
    else:
        log = f"<#{log}>"
    embed = discord.Embed(title="Settings", color=info)
    embed.add_field(name="Prefix:", value=prefix)
    embed.add_field(name="Logging channel:", value=f"{log}")
    embed.add_field(
        name="Welcome message:",
        value=f"Channel -> {welcomechannel} \n Message -> `{welcome}`")
    embed.add_field(name="Moderator role:", value=modrole)
    await ctx.send(embed=embed)


@bot.slash_command(guild_ids=[885084260325793802], description="Kick a user from the server.")
async def kick(ctx, member: discord.Member, reason: str = None):
    try:
        await member.kick(reason=reason)
    except:
        return await ctx.send("Something went wrong when kicking this user.")
    await ctx.send("Kick success!")


@bot.slash_command(guild_ids=[885084260325793802], description="Ban a user from the server.")
async def ban(ctx, member: discord.Member, reason: str = None):
    try:
        await member.ban(reason=reason)
    except:
        return await ctx.send("Something went wrong when banning this user.")
    await ctx.send("Ban success!")


@bot.slash_command(description="View the bot's info. Credits, machine info, and ping!")
async def botinfo(ctx):
    desc = f"""
        __Credits__
        **Creator**: Pop Plays
        **Co-creator**: Availyx

        **Ping**: {round(bot.latency * 1000)} ms

        __Machine info:__

        **OS**: `{platform.system()}`
        **Machine**: `{platform.platform()}`
        **Processor**: `{platform.machine()}`
    """
    embed = discord.Embed(color=norm, description=desc, title=f"About {bot.user.name}")
    embed.set_image(url=bot.user.avatar)
    await ctx.send(embed=embed)


@bot.slash_command(description="hug someone!")
async def hug(ctx, member: discord.Member):
    image = imgapi.sfw(category='hug')
    embed = discord.Embed(title=f"{ctx.author.display_name} hugged {member.display_name}!",
                          color=discord.Color.random())
    embed.set_image(url=str(image))
    await ctx.send(embed=embed)


@bot.slash_command(description="kiss someone 💋")
async def kiss(ctx, member: discord.Member):
    image = imgapi.sfw(category='kiss')
    embed = discord.Embed(title=f"{ctx.author.display_name} kissed {member.display_name}!",
                          color=discord.Color.random())
    embed.set_image(url=str(image))
    await ctx.send(embed=embed)


@bot.slash_command(description="slap someone of your choice :p")
async def slap(ctx, member: discord.Member):
    image = imgapi.sfw(category='slap')
    embed = discord.Embed(title=f"{ctx.author.display_name} slaps {member.display_name}!", color=discord.Color.random())
    embed.set_image(url=str(image))
    await ctx.send(embed=embed)


@bot.slash_command(description="Get some blowjob gifs / images. Only usable in NSFW channels!")
async def blowjob(ctx):
    if not ctx.channel.is_nsfw():
        return await ctx.send("This command can only be used in NSFW channels!")
    embed = discord.Embed(title="Get some porn!", color=discord.Color.random())
    image = imgapi.nsfw(category='blowjob')
    embed.set_image(url=str(image))
    await ctx.send(embed=embed)


@bot.slash_command(description="Get some general porn from Reddit. Only usable in NSFW channels.")
async def porn(ctx):
    if ctx.channel.is_nsfw():

        embed = discord.Embed(title="Get some porn!", description="fresh from reddit :p", color=discord.Color.random())
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/nsfw/new.json?sort=hot') as r:
                    res = await r.json()
                    embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
                    await ctx.send(embed=embed)
        except:
            await ctx.send("Hmmm.. something went wrong whenn fetching an image. Try again :)")
    else:
        await ctx.send("You need to use this command in a nsfw channel!")


@bot.slash_command(description="Get some anime porn. Only usable in NSFW channels.")
async def hentai(ctx):
    if ctx.channel.is_nsfw():
        nsfw = anime.get_nsfw('hentai')
        embed = discord.Embed(title="Take some hentai!")
        embed.set_image(url=str(nsfw))
        await ctx.send(embed=embed)
    else:
        await ctx.send("This command can only be used in NSFW channels!")


@bot.slash_command(description="Sets the welcome channel!")
async def setwelcomechannel(ctx, role):
    authorperms = ctx.author.guild_permissions
    if authorperms.administrator:
        with open('guild.json', 'r') as f:  # read the prefix.json file
            guilds = json.load(f)  # load the json file
        part1 = role.replace('<', '')
        part2 = part1.replace('>', '')
        part3 = part2.replace('#', '')
        guilds[str(ctx.guild.id)]["welcomechannel"] = part3
        print(guilds[str(ctx.guild.id)]["welcomechannel"])
        with open('guild.json',
                  'w') as f:  # writes the new prefix into the .json
            json.dump(guilds, f, indent=4)
        embed = discord.Embed(
            title="Configuration",
            color=success,
            description=
            f"{tick} The Welcome Channel has been successfully updated!")
        await ctx.send(embed=embed)


@bot.slash_command(description="Sets the welcome message.")
async def setwelcomemessage(ctx, *, text):
    authorperms = ctx.author.guild_permissions
    if authorperms.administrator:
        with open('guild.json', 'r') as f:  # read the prefix.json file
            guilds = json.load(f)  # load the json file
        guilds[str(ctx.guild.id)]["welcome"] = text
        with open('guild.json',
                  'w') as f:  # writes the new prefix into the .json
            json.dump(guilds, f, indent=4)
        embed = discord.Embed(
            title="Configuration",
            color=success,
            description=
            f"{tick} The Welcome Message has been successfully updated!")
        await ctx.send(embed=embed)


# Defines a custom button that contains the logic of the game.
# The ['TicTacToe'] bit is for type hinting purposes to tell your IDE or linter
# what the type of `self.view` is. It is not required.
class TicTacToeButton(discord.ui.Button["TicTacToe"]):
    def __init__(self, x: int, y: int):
        # A label is required, but we don't need one so a zero-width space is used
        # The row parameter tells the View which row to place the button under.
        # A View can only contain up to 5 rows -- each row can only have 5 buttons.
        # Since a Tic Tac Toe grid is 3x3 that means we have 3 rows and 3 columns.
        super().__init__(style=discord.ButtonStyle.secondary, label="\u200b", row=y)
        self.x = x
        self.y = y

    # This function is called whenever this particular button is pressed
    # This is part of the "meat" of the game logic
    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: TicTacToe = self.view
        state = view.board[self.y][self.x]
        if state in (view.X, view.O):
            return

        if view.current_player == view.X:
            self.style = discord.ButtonStyle.danger
            self.label = "X"
            self.disabled = True
            view.board[self.y][self.x] = view.X
            view.current_player = view.O
            content = "It is now O's turn"
        else:
            self.style = discord.ButtonStyle.success
            self.label = "O"
            self.disabled = True
            view.board[self.y][self.x] = view.O
            view.current_player = view.X
            content = "It is now X's turn"

        winner = view.check_board_winner()
        if winner is not None:
            if winner == view.X:
                content = "X won!"
            elif winner == view.O:
                content = "O won!"
            else:
                content = "It's a tie!"

            for child in view.children:
                child.disabled = True

            view.stop()

        await interaction.response.edit_message(content=content, view=view)


# This is our actual board View
class TicTacToe(discord.ui.View):
    # This tells the IDE or linter that all our children will be TicTacToeButtons
    # This is not required
    children: List[TicTacToeButton]
    X = -1
    O = 1
    Tie = 2

    def __init__(self):
        super().__init__()
        self.current_player = self.X
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        # Our board is made up of 3 by 3 TicTacToeButtons
        # The TicTacToeButton maintains the callbacks and helps steer
        # the actual game.
        for x in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(x, y))

    # This method checks for the board winner -- it is used by the TicTacToeButton
    def check_board_winner(self):
        for across in self.board:
            value = sum(across)
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        # Check vertical
        for line in range(3):
            value = self.board[0][line] + self.board[1][line] + self.board[2][line]
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        # Check diagonals
        diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        # If we're here, we need to check if a tie was made
        if all(i != 0 for row in self.board for i in row):
            return self.Tie

        return None


@bot.slash_command()
async def ttt(ctx):
    """Starts a tic-tac-toe game with yourself."""
    await ctx.send("Tic Tac Toe: X goes first", view=TicTacToe())


class Counter(discord.ui.View):

    # Define the actual button
    # When pressed, this increments the number displayed until it hits 5.
    # When it hits 5, the counter button is disabled and it turns green.
    # note: The name of the function does not matter to the library
    @discord.ui.button(label="0", style=discord.ButtonStyle.red)
    async def count(self, button: discord.ui.Button, interaction: discord.Interaction):
        number = int(button.label) if button.label else 0
        if number + 1 >= 100:
            button.style = discord.ButtonStyle.green
            button.disabled = True
        button.label = str(number + 1)

        # Make sure to update the message with our updated selves
        await interaction.response.edit_message(view=self)


def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


@bot.slash_command()
async def giveaway(ctx, channel: discord.abc.GuildChannel, prize: str, duration: str):
    questions = ["Which channel should it be hosted in?", "What should be the duration of the giveaway? (s|m|h|d)",
                 "What is the prize of the giveaway?"]

    time = convert(duration)
    if time == -1:
        await ctx.send(f"You didn't answer with a proper unit. Use (s|m|h|d) next time!")
        return
    elif time == -2:
        await ctx.send(f"The time just be an integer. Please enter an integer next time.")
        return

    await ctx.send(f"The giveaway will be in {channel.mention} and will last {duration} seconds!")

    embed = discord.Embed(title="🎁 Giveaway!", description=f"{prize}", color=ctx.author.color)

    embed.add_field(name="Hosted by:", value=ctx.author.mention)

    embed.set_footer(text=f"Ends {duration} from now!")

    my_msg = await channel.send(embed=embed)

    await my_msg.add_reaction("🎉")
    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await channel.send(f"🎉 Congratulations! {winner.mention} won the prize: `{prize}`")


@bot.slash_command()
async def reroll(ctx, channel: discord.abc.GuildChannel, message_link: str):
    message_link = message_link.split(f"https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/")[1]
    new_msg = await channel.fetch_message(int(message_link))
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))
    winner = random.choice(users)
    await ctx.send("Re-rolled!")
    await channel.send(f"Congratulations the new winner is: {winner.mention} for the giveaway rerolled!")


@bot.slash_command()
async def poll(ctx, channel: discord.abc.GuildChannel, question: str):
    toplace = await ctx.send(f"{ctx.author.mention} check your DMs to setup choices!")
    counter = 0
    embed = discord.Embed(title="📊 New poll!", description=f"Sent by {ctx.author.display_name}",
                          color=discord.Color.random())
    embed.add_field(name="Question:", value=question)
    while True:
        await ctx.author.send(
            "Type your choice here. You can set 9 choices. Type `done` to send your poll, or `cancel` to cancel everything.")

        def check(msg):
            return msg.author == ctx.author

        reply = await bot.wait_for("message", check=check)
        reply = reply.content
        counter += 1
        if counter >= 10:
            await ctx.author.send(
                "You've reached the maximum number of choices allowed. Do `done` or `cancel` to continue.")
            continue
        if reply == "cancel":
            return await ctx.author.send("Your poll has been cancelled!")
        if reply == "done":
            await ctx.author.send("Your poll has been sent!")
            break
        embed.add_field(name=f"{counter}: {reply}", value="** **", inline=False)

    msg = await channel.send(embed=embed)
    counter2 = 0
    counter -= 1
    while True:
        print(counter)
        if counter2 == counter:
            break
        else:
            counter2 += 1
            if counter2 == 1:
                await msg.add_reaction(f"1️⃣")
            if counter2 == 2:
                await msg.add_reaction(f"2️⃣")
            if counter2 == 3:
                await msg.add_reaction(f"3️⃣")
            if counter2 == 4:
                await msg.add_reaction(f"4️⃣")
            if counter2 == 5:
                await msg.add_reaction(f"5️⃣")
            if counter2 == 6:
                await msg.add_reaction(f"6️⃣")
            if counter2 == 7:
                await msg.add_reaction(f"7️⃣")
            if counter2 == 8:
                await msg.add_reaction(f"8️⃣")
            if counter2 == 9:
                await msg.add_reaction(f"9️⃣")


@bot.slash_command()
async def counter(ctx):
    """Starts a counter for pressing."""
    await ctx.send("Count till 100.", view=Counter())




@bot.event
async def on_ready():
    print(f"logged in as {bot.user}!")


class Dropdown(discord.ui.Select):
    def __init__(self):
        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(
                label="Red", description="Your favourite colour is red", emoji="🟥"
            ),
            discord.SelectOption(
                label="Green", description="Your favourite colour is green", emoji="🟩"
            ),
            discord.SelectOption(
                label="Blue", description="Your favourite colour is blue", emoji="🟦"
            ),
        ]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(
            placeholder="Choose your favourite colour...",
            min_values=1,
            max_values=1,
            options=options,
            disabled=True
        )

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        await interaction.response.send_message(
            f"Your favourite colour is {self.values[0]}"
        )


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())



@bot.slash_command(guild_ids=[885084260325793802])
async def dropdown(ctx):
    await ctx.send("Hereya go, da colors.", view=DropdownView())


@bot.slash_command()
async def invite(ctx):
    desc = """
    Paradox is a fun, new and bright bot that can ease how you use your server.

    [[invite]](https://discord.com/api/oauth2/authorize?client_id=885170335517917235&permissions=8&scope=bot%20applications.commands)
    """
    embed = discord.Embed(title="Invite Paradox", color=discord.Color.random(), description=desc)
    await ctx.send(embed=embed)


@bot.slash_command(guild_ids=[885084260325793802])
async def verify(ctx):
    import textcaptcha
    fetcher = textcaptcha.CaptchaFetcher()
    # Fetch a new captcha from the API
    await ctx.send(content="Check your dms.")
    await asyncio.sleep(2)
    await ctx.interaction.delete_original_message()
    count = 0

    def check(msg):
        return msg.author == ctx.author

    while True:
        if count >= 5:
            blacklist = discord.utils.find(lambda r: r.id == 885726541454135306, ctx.guild.roles)
            await ctx.author.add_roles(blacklist)  # Adds the role to the member
            unverified = discord.utils.find(lambda r: r.id == 885311577853685811, ctx.guild.roles)
            await ctx.author.remove_roles(unverified)
            return await ctx.author.send(
                "We can't verify if you aren't a bot. As of so, you are blacklisted from the captcha system temporarily. DM a moderator to regain your access!")
        captcha = fetcher.fetch()
        prompt = await ctx.author.send(
            f"{captcha.question} [This expires in 30 seconds! If you wish to cancel, do `cancel`!]")
        reply = await bot.wait_for("message", timeout=30, check=check)
        # Check that the answer is correct
        if reply.content.lower() == "cancel":
            return await ctx.author.send("Cancelled!")

        if captcha.check_answer(reply.content):
            break
        else:
            count += 1
            if 5 - count == 1:
                continue
            await ctx.author.send(f"Your captcha was invalid! You have {5 - count} chance(s) left.")
    verified = discord.utils.find(lambda r: r.id == 885311509553635328, ctx.guild.roles)
    await ctx.author.add_roles(verified)  # Adds the role to the member
    unverified = discord.utils.find(lambda r: r.id == 885311577853685811, ctx.guild.roles)
    await ctx.author.remove_roles(unverified)
    await ctx.author.send(f"{tick} You are now verified!")

@bot.command(description="Check if a user is an admin!")
async def checkadmin(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    if user.guild_permissions.administrator:
        await ctx.send(f"{user} is an admin.")
    else:
        await ctx.send(f"{user} is not an admin.")


@bot.command(description="Get a random fact.")
async def randomfact(ctx):
    x = randfacts.get_fact()
    await ctx.send(x)


@bot.command(description="View all the bot's commands!")
async def help(ctx):
    embed = discord.Embed(title="Help", description=helpcmd, color=discord.Color.random())
    await ctx.send(embed=embed)


@bot.command()
async def gay(ctx):
    choices = ["https://cdn1.sunporno.com/thumbs/320x240/572/2013581/2.jpg","https://fi1-ph.ypncdn.com/videos/201906/14/229410912/original/8(m=eKw7Kgaaaa)(mh=kVS_EmSOTCH_hYVX).jpg", "https://icdn03.boy18tube.com/51076/2553763_3.jpg"]
    embed = discord.Embed(title="Take some porn!", color=discord.Color.random())
    embed.set_image(url=str(random.choice(choices)))
    await ctx.send(embed=embed)


@bot.command(description="View all the emojis in your server.")
async def emojis(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}'s emojis", color=discord.Color.random())
    counter = 0
    for emoji in ctx.guild.emojis:
        if counter >= 25:
            break
        counter += 1
        if emoji.animated == True:
            emojiimg = f"<a:{emoji.name}:{emoji.id}>"
        else:
            emojiimg = f"<:{emoji.name}:{emoji.id}>"
        embed.add_field(name=f"{emojiimg} {emoji.name}", value=f"Id: {emoji.id}", inline=False)
        embed.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar)
    await ctx.send(embed=embed)


@bot.command(description="Warn a user in your server!")
async def warn(ctx, member: discord.Member, *, reason: str):
    S = 50
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k=S))
    warning = {
        "moderator": ctx.author.display_name,
        "member": str(member.display_name),
        "reason": reason,
        "_id": str(ran)
    }
    post_id = warnsdb.insert_one(warning).inserted_id
    await ctx.send(f"{member.mention} has been warned for {reason}!")
    logs = log("warn", ctx.author, member, reason)
    logchannel = get_logs(ctx)
    await logchannel.send(embed=logs)


@bot.command(description="View the warnings for yourself, or a member.")
async def warns(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    counter = 0
    embed = discord.Embed(title="Warnings")
    for warnings in warnsdb.find({"member": str(member.display_name)}).limit(25):
        counter += 1
        mod = warnings["moderator"]
        reason = warnings["reason"]
        mongoid = warnings["_id"]
        embed.add_field(name=f"Moderator: {mod}",
                        value=f"`{reason}` \n\n Id: {mongoid}",
                        inline=False)
    if counter == 0:
        embed = discord.Embed(title=f"❌ {member.display_name} has no warnings.")

    await ctx.send(embed=embed)


@bot.command()
async def deletewarn(ctx, warningid):
    result = warnsdb.find_one({"_id": warningid})
    if result == None:
        await ctx.send("That id is invalid!")
    else:
        warnsdb.delete_one({"_id": warningid})
        await ctx.send("warning deleted")
        logs = log("Warn deleted", ctx.author, "N/A", "N/A")
        logchannel = get_logs(ctx)
        await logchannel.send(embed=embed)


@bot.command(description="View the config for the bot.")
async def config(ctx):
    with open('guild.json', 'r') as f:  # read the prefix.json file
        guilds = json.load(f)  # load the json file
    prefix = guilds[str(ctx.guild.id)]["prefix"]
    log = guilds[str(ctx.guild.id)]["logs"]
    welcome = guilds[str(ctx.guild.id)]["welcome"]
    welcomechannel = guilds[str(ctx.guild.id)]["welcomechannel"]
    modrole = guilds[str(ctx.guild.id)]["modrole"]
    if welcomechannel == "none":
        welcomechannel = "None"
    else:
        welcomechannel = f"<#{welcomechannel}>"
    if modrole == "none":
        modrole = "None"
    else:
        modrole = f"<@&{modrole}>"
    if log == "none":
        log = "none"
    else:
        log = f"<#{log}>"
    embed = discord.Embed(title="Settings", color=info)
    embed.add_field(name="Prefix:", value=prefix)
    embed.add_field(name="Logging channel:", value=f"{log}")
    embed.add_field(
        name="Welcome message:",
        value=f"Channel -> {welcomechannel} \n Message -> `{welcome}`")
    embed.add_field(name="Moderator role:", value=modrole)
    await ctx.send(embed=embed)


@bot.command(guild_ids=[885084260325793802], description="Kick a user from the server.")
async def kick(ctx, member: discord.Member, reason: str = None):
    try:
        await member.kick(reason=reason)
    except:
        return await ctx.send("Something went wrong when kicking this user.")
    await ctx.send("Kick success!")


@bot.command(guild_ids=[885084260325793802], description="Ban a user from the server.")
async def ban(ctx, member: discord.Member, reason: str = None):
    try:
        await member.ban(reason=reason)
    except:
        return await ctx.send("Something went wrong when banning this user.")
    await ctx.send("Ban success!")


@bot.command(description="View the bot's info. Credits, machine info, and ping!")
async def botinfo(ctx):
    desc = f"""
        __Credits__
        **Creator**: Pop Plays
        **Co-creator**: Availyx

        **Ping**: {round(bot.latency * 1000)} ms

        __Machine info:__

        **OS**: `{platform.system()}`
        **Machine**: `{platform.platform()}`
        **Processor**: `{platform.machine()}`
    """
    embed = discord.Embed(color=norm, description=desc, title=f"About {bot.user.name}")
    embed.set_image(url=bot.user.avatar)
    await ctx.send(embed=embed)


@bot.command(description="hug someone!")
async def hug(ctx, member: discord.Member):
    image = imgapi.sfw(category='hug')
    embed = discord.Embed(title=f"{ctx.author.display_name} hugged {member.display_name}!",
                          color=discord.Color.random())
    embed.set_image(url=str(image))
    await ctx.send(embed=embed)


@bot.command(description="kiss someone 💋")
async def kiss(ctx, member: discord.Member):
    image = imgapi.sfw(category='kiss')
    embed = discord.Embed(title=f"{ctx.author.display_name} kissed {member.display_name}!",
                          color=discord.Color.random())
    embed.set_image(url=str(image))
    await ctx.send(embed=embed)


@bot.command(description="slap someone of your choice :p")
async def slap(ctx, member: discord.Member):
    image = imgapi.sfw(category='slap')
    embed = discord.Embed(title=f"{ctx.author.display_name} slaps {member.display_name}!", color=discord.Color.random())
    embed.set_image(url=str(image))
    await ctx.send(embed=embed)


@bot.command(description="Get some blowjob gifs / images. Only usable in NSFW channels!")
async def blowjob(ctx):
    if not ctx.channel.is_nsfw():
        return await ctx.send("This command can only be used in NSFW channels!")
    embed = discord.Embed(title="Get some porn!", color=discord.Color.random())
    image = imgapi.nsfw(category='blowjob')
    embed.set_image(url=str(image))
    await ctx.send(embed=embed)


@bot.command(description="Get some general porn from Reddit. Only usable in NSFW channels.")
async def porn(ctx):
    if ctx.channel.is_nsfw():

        embed = discord.Embed(title="Get some porn!", description="fresh from reddit :p", color=discord.Color.random())
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/nsfw/new.json?sort=hot') as r:
                    res = await r.json()
                    embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
                    await ctx.send(embed=embed)
        except:
            await ctx.send("Hmmm.. something went wrong whenn fetching an image. Try again :)")
    else:
        await ctx.send("You need to use this command in a nsfw channel!")


@bot.command(description="Get some anime porn. Only usable in NSFW channels.")
async def hentai(ctx):
    if ctx.channel.is_nsfw():
        nsfw = anime.get_nsfw('hentai')
        embed = discord.Embed(title="Take some hentai!")
        embed.set_image(url=str(nsfw))
        await ctx.send(embed=embed)
    else:
        await ctx.send("This command can only be used in NSFW channels!")


@bot.command(description="Sets the welcome channel!")
async def setwelcomechannel(ctx, role):
    authorperms = ctx.author.guild_permissions
    if authorperms.administrator:
        with open('guild.json', 'r') as f:  # read the prefix.json file
            guilds = json.load(f)  # load the json file
        part1 = role.replace('<', '')
        part2 = part1.replace('>', '')
        part3 = part2.replace('#', '')
        guilds[str(ctx.guild.id)]["welcomechannel"] = part3
        print(guilds[str(ctx.guild.id)]["welcomechannel"])
        with open('guild.json',
                  'w') as f:  # writes the new prefix into the .json
            json.dump(guilds, f, indent=4)
        embed = discord.Embed(
            title="Configuration",
            color=success,
            description=
            f"{tick} The Welcome Channel has been successfully updated!")
        await ctx.send(embed=embed)


@bot.command(description="Sets the welcome message.")
async def setwelcomemessage(ctx, *, text):
    authorperms = ctx.author.guild_permissions
    if authorperms.administrator:
        with open('guild.json', 'r') as f:  # read the prefix.json file
            guilds = json.load(f)  # load the json file
        guilds[str(ctx.guild.id)]["welcome"] = text
        with open('guild.json',
                  'w') as f:  # writes the new prefix into the .json
            json.dump(guilds, f, indent=4)
        embed = discord.Embed(
            title="Configuration",
            color=success,
            description=
            f"{tick} The Welcome Message has been successfully updated!")
        await ctx.send(embed=embed)


# Defines a custom button that contains the logic of the game.
# The ['TicTacToe'] bit is for type hinting purposes to tell your IDE or linter
# what the type of `self.view` is. It is not required.
class TicTacToeButton(discord.ui.Button["TicTacToe"]):
    def __init__(self, x: int, y: int):
        # A label is required, but we don't need one so a zero-width space is used
        # The row parameter tells the View which row to place the button under.
        # A View can only contain up to 5 rows -- each row can only have 5 buttons.
        # Since a Tic Tac Toe grid is 3x3 that means we have 3 rows and 3 columns.
        super().__init__(style=discord.ButtonStyle.secondary, label="\u200b", row=y)
        self.x = x
        self.y = y

    # This function is called whenever this particular button is pressed
    # This is part of the "meat" of the game logic
    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: TicTacToe = self.view
        state = view.board[self.y][self.x]
        if state in (view.X, view.O):
            return

        if view.current_player == view.X:
            self.style = discord.ButtonStyle.danger
            self.label = "X"
            self.disabled = True
            view.board[self.y][self.x] = view.X
            view.current_player = view.O
            content = "It is now O's turn"
        else:
            self.style = discord.ButtonStyle.success
            self.label = "O"
            self.disabled = True
            view.board[self.y][self.x] = view.O
            view.current_player = view.X
            content = "It is now X's turn"

        winner = view.check_board_winner()
        if winner is not None:
            if winner == view.X:
                content = "X won!"
            elif winner == view.O:
                content = "O won!"
            else:
                content = "It's a tie!"

            for child in view.children:
                child.disabled = True

            view.stop()

        await interaction.response.edit_message(content=content, view=view)


# This is our actual board View
class TicTacToe(discord.ui.View):
    # This tells the IDE or linter that all our children will be TicTacToeButtons
    # This is not required
    children: List[TicTacToeButton]
    X = -1
    O = 1
    Tie = 2

    def __init__(self):
        super().__init__()
        self.current_player = self.X
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        # Our board is made up of 3 by 3 TicTacToeButtons
        # The TicTacToeButton maintains the callbacks and helps steer
        # the actual game.
        for x in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(x, y))

    # This method checks for the board winner -- it is used by the TicTacToeButton
    def check_board_winner(self):
        for across in self.board:
            value = sum(across)
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        # Check vertical
        for line in range(3):
            value = self.board[0][line] + self.board[1][line] + self.board[2][line]
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        # Check diagonals
        diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        # If we're here, we need to check if a tie was made
        if all(i != 0 for row in self.board for i in row):
            return self.Tie

        return None


@bot.command()
async def ttt(ctx):
    """Starts a tic-tac-toe game with yourself."""
    await ctx.send("Tic Tac Toe: X goes first", view=TicTacToe())


class Counter(discord.ui.View):

    # Define the actual button
    # When pressed, this increments the number displayed until it hits 5.
    # When it hits 5, the counter button is disabled and it turns green.
    # note: The name of the function does not matter to the library
    @discord.ui.button(label="0", style=discord.ButtonStyle.red)
    async def count(self, button: discord.ui.Button, interaction: discord.Interaction):
        number = int(button.label) if button.label else 0
        if number + 1 >= 100:
            button.style = discord.ButtonStyle.green
            button.disabled = True
        button.label = str(number + 1)

        # Make sure to update the message with our updated selves
        await interaction.response.edit_message(view=self)


def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


@bot.command()
async def giveaway(ctx, channel: discord.abc.GuildChannel, prize: str, duration: str):
    questions = ["Which channel should it be hosted in?", "What should be the duration of the giveaway? (s|m|h|d)",
                 "What is the prize of the giveaway?"]

    time = convert(duration)
    if time == -1:
        await ctx.send(f"You didn't answer with a proper unit. Use (s|m|h|d) next time!")
        return
    elif time == -2:
        await ctx.send(f"The time just be an integer. Please enter an integer next time.")
        return

    await ctx.send(f"The giveaway will be in {channel.mention} and will last {duration} seconds!")

    embed = discord.Embed(title="🎁 Giveaway!", description=f"{prize}", color=ctx.author.color)

    embed.add_field(name="Hosted by:", value=ctx.author.mention)

    embed.set_footer(text=f"Ends {duration} from now!")

    my_msg = await channel.send(embed=embed)

    await my_msg.add_reaction("🎉")
    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await channel.send(f"🎉 Congratulations! {winner.mention} won the prize: `{prize}`")


@bot.command()
async def reroll(ctx, channel: discord.abc.GuildChannel, message_link: str):
    message_link = message_link.split(f"https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/")[1]
    new_msg = await channel.fetch_message(int(message_link))
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))
    winner = random.choice(users)
    await ctx.send("Re-rolled!")
    await channel.send(f"Congratulations the new winner is: {winner.mention} for the giveaway rerolled!")


@bot.command()
async def poll(ctx, channel: discord.abc.GuildChannel, question: str):
    toplace = await ctx.send(f"{ctx.author.mention} check your DMs to setup choices!")
    counter = 0
    embed = discord.Embed(title="📊 New poll!", description=f"Sent by {ctx.author.display_name}",
                          color=discord.Color.random())
    embed.add_field(name="Question:", value=question)
    while True:
        await ctx.author.send(
            "Type your choice here. You can set 9 choices. Type `done` to send your poll, or `cancel` to cancel everything.")

        def check(msg):
            return msg.author == ctx.author

        reply = await bot.wait_for("message", check=check)
        reply = reply.content
        counter += 1
        if counter >= 10:
            await ctx.author.send(
                "You've reached the maximum number of choices allowed. Do `done` or `cancel` to continue.")
            continue
        if reply == "cancel":
            return await ctx.author.send("Your poll has been cancelled!")
        if reply == "done":
            await ctx.author.send("Your poll has been sent!")
            break
        embed.add_field(name=f"{counter}: {reply}", value="** **", inline=False)

    msg = await channel.send(embed=embed)
    counter2 = 0
    counter -= 1
    while True:
        print(counter)
        if counter2 == counter:
            break
        else:
            counter2 += 1
            if counter2 == 1:
                await msg.add_reaction(f"1️⃣")
            if counter2 == 2:
                await msg.add_reaction(f"2️⃣")
            if counter2 == 3:
                await msg.add_reaction(f"3️⃣")
            if counter2 == 4:
                await msg.add_reaction(f"4️⃣")
            if counter2 == 5:
                await msg.add_reaction(f"5️⃣")
            if counter2 == 6:
                await msg.add_reaction(f"6️⃣")
            if counter2 == 7:
                await msg.add_reaction(f"7️⃣")
            if counter2 == 8:
                await msg.add_reaction(f"8️⃣")
            if counter2 == 9:
                await msg.add_reaction(f"9️⃣")


@bot.command()
async def counter(ctx):
    """Starts a counter for pressing."""
    await ctx.send("Count till 100.", view=Counter())


keep_alive()
bot.run("ODg1MTcwMzM1NTE3OTE3MjM1.YTjJHQ.jqG7TDoI7582BUQ96lR_DCbzR0I")
