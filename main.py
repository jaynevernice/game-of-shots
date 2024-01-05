import discord
import os
# import sys
import random
from replit import db
from keep_alive import keep_alive
from lists import *
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

if "responding" not in db.keys():
  db["responding"] = True


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user}')
  await bot.change_presence(activity=discord.Activity(
    type=discord.ActivityType.listening, name="/play"))
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  await bot.process_commands(message)

  msg = message.content

  if msg.startswith(".listPar"):
    parList = []
    if "paranoia" in db.keys():
      paranoia = list(db["paranoia"])
      await message.channel.send(paranoia)


##########################
# Slash Command


@bot.tree.command(name="dev", description="Meet the developer")
async def dev(interaction: discord.Interaction):
  await interaction.response.send_message(f"This bot was created by" + "<@" +
                                          str(658544779579359242) + ">.RIP")


@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
  await interaction.response.send_message(
    f"Hey {interaction.user.mention}! This is a slash command!",
    ephemeral=True)


@bot.tree.command(name="say")
@app_commands.describe(thing_to_say="What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
  await interaction.response.send_message(
    f"{interaction.user.name} said: `{thing_to_say}`")


#==========Gossip==========
@bot.tree.command(name="gossip_add", description="Add a new Gossip question")
@app_commands.describe(
  new_gossip="ex: Do you think the victim is a sex addict?")
async def gossip_add(interaction: discord.Interaction, new_gossip: str):
  update_gossip(new_gossip)
  await interaction.response.send_message("Successfully updated Gossip")


@bot.tree.command(name="gossip_delete", description="Delete a Gossip question")
@app_commands.describe(
  index="Enter the index of the question you want to delete")
async def gossip_add(interaction: discord.Interaction, index: int):
  gossip = []
  if "gossip" in db.keys():
    delete_gossip(index)
    gossip = list(db['gossip'])
    await interaction.response.send_message(gossip)


@bot.tree.command(name="gossip_list",
                  description="List all the Gossip questions")
async def gossip_list(interaction: discord.Interaction):
  gossipList = []
  if "gossip" in db.keys():
    gossip = list(db["gossip"])
    await interaction.response.send_message(gossip)


#==========Never Have I Ever==========
@bot.tree.command(name="nhie_add",
                  description="Add a new Never Have I Ever question")
@app_commands.describe(new_nhie="ex: Danced naked in front of a mirror")
async def nhie_add(interaction: discord.Interaction, new_nhie: str):
  update_nhie(new_nhie)
  await interaction.response.send_message(
    "Successfully update Never Have I Ever")


@bot.tree.command(name="nhie_delete",
                  description="Delete a Never Have I Ever question")
@app_commands.describe(
  index="Enter the index of the question you want to delete")
async def nhie_delete(interaction: discord.Interaction, index: int):
  nhie = []
  if "nhie" in db.keys():
    delete_nhie(index)
    nhie = list(db['nhie'])
    await interaction.response.send_message(nhie)


@bot.tree.command(name="nhie_list",
                  description="List all the Never Have I Ever questions")
async def nhie_list(interaction: discord.Interaction):
  nhieList = []
  if "nhie" in db.keys():
    nhie = list(db["nhie"])
    await interaction.response.send_message(nhie)


#==========Paranoia==========
@bot.tree.command(name="paranoia_add",
                  description="Add a new Paranoia question")
@app_commands.describe(
  new_paranoia="ex: Who is most likely to be a perfect kisser?")
async def paranoia_add(interaction: discord.Interaction, new_paranoia: str):
  update_paranoia(new_paranoia)
  await interaction.response.send_message("Successfully updated Paranoia")


@bot.tree.command(name="paranoia_delete",
                  description="Delete a Paranoia question")
@app_commands.describe(
  index="Enter the index of the question you want to delete")
async def paranoia_delete(interaction: discord.Interaction, index: int):
  paranoia = []
  if "paranoia" in db.keys():
    delete_paranoia(index)
    paranoia = list(db['paranoia'])
    await interaction.response.send_message(paranoia)


@bot.tree.command(name="paranoia_list",
                  description="List all the Paranoia questions")
async def paranoia_list(interaction: discord.Interaction):
  parList = []
  if "paranoia" in db.keys():
    paranoia = list(db["paranoia"])
    await interaction.response.send_message(paranoia)


#==========Truth==========
@bot.tree.command(name="truth_add", description="Add a new Truth question")
@app_commands.describe(new_truth="ex: Do you have any fetishes?")
async def truth_add(interaction: discord.Interaction, new_truth: str):
  update_truth(new_truth)
  await interaction.response.send_message("Successfully updated Truth")


@bot.tree.command(name="truth_delete", description="Delete a Truth question")
@app_commands.describe(
  index="Enter the index of the question you want to delete")
async def truth_delete(interaction: discord.Interaction, index: int):
  truth = []
  if "truth" in db.keys():
    delete_truth(index)
    truth = list(db['truth'])
    await interaction.response.send_message(truth)


@bot.tree.command(name="truth_list",
                  description="List all the Truth questions")
async def truth_list(interaction: discord.Interaction):
  truthList = []
  if "truth" in db.keys():
    truth = list(db["truth"])
    await interaction.response.send_message(truth)


@bot.tree.command(name="dare_add", description="Add a new Dare")
@app_commands.describe(
  new_dare="ex: Say two honest things about everyone in the group")
async def dare_add(interaction: discord.Interaction, new_dare: str):
  update_dare(new_dare)
  await message.channel.send("Successfully updated Dare")


@bot.tree.command(name="dare_delete", description="Delete a Dare")
@app_commands.describe(
  index="Enter the index of the question you want to delete")
async def dare_delete(interaction: discord.Interaction, index: int):
  dare = []
  if "dare" in db.keys():
    delete_dare(index)
    dare = list(db['dare'])
    await interaction.response.send_message(dare)


@bot.tree.command(name="dare_list", description="List all the Dare")
async def dare_list(interaction: discord.Interaction):
  dareList = []
  if "dare" in db.keys():
    dare = list(db["dare"])
    await interaction.response.send_message(dare)


#==========Would You Rather==========
@bot.tree.command(name="wyr_add",
                  description="Add a new Would You Rather Question")
@app_commands.describe(
  new_wyr=
  "ex: Get diarrhea on vacation or the day of a big presentation at work?")
async def wyr_add(interaction: discord.Interaction, new_wyr: str):
  new_wyr = msg.split(".newWyr ", 1)[1]
  update_wyr(new_wyr)
  await interaction.response.send_message(
    "Successfully updated Would You Rather")


@bot.tree.command(name="wyr_delete",
                  description="Delete a Would You Rather Question")
@app_commands.describe(
  index="Enter the index of the question you want to delete")
async def wyr_delete(interaction: discord.Interaction, index: int):
  wyr = []
  if "wyr" in db.keys():
    delete_wyr(index)
    wyr = list(db['wyr'])
    await interaction.response.send_message(wyr)


@bot.tree.command(name="wyr_list",
                  description="List all the Would You Rather Question")
async def wyr_list(interaction: discord.Interaction):
  wyrList = []
  if "wyr" in db.keys():
    wyr = list(db["wyr"])
    await interaction.response.send_message(wyr)


#os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
########################


#Play Menu
@bot.tree.command(name="play", description="Play")
async def play(ctx):
  playEmb = discord.Embed(title="Game of Shots", color=0xe74c3c)
  playEmb.set_image(
    url=
    "https://media1.giphy.com/media/wpVM8uZMwThC0/giphy.gif?cid=ecf05e470lmdw1a5nzvyli2hoy6ebp6c3zfvndfpnu9ijkcq&rid=giphy.gif&ct=g"
  )
  playEmb.add_field(
    name="\nGossip",
    value=
    "Each player have to answer a question about the indicated player. The aforementioned person will say the correct answer when the rest of the players have given their answers. Those who have failed will have to drink",
    inline=False)
  playEmb.add_field(
    name="\nMad Gab",
    value=
    "Two teams have two minutes to sound out three puzzles. The puzzles, also known as mondegreens, contain small words that, when put together, make a word or phrase.",
    inline=False)
  playEmb.add_field(
    name="\nNever Have I Ever",
    value=
    "Players take turns asking other players about things they have not done. Other players who have done this thing respond by taking a drink.",
    inline=False)
  playEmb.add_field(
    name="\nParanoia",
    value=
    "This game involves whispering a question to the person on your right, the answer of which has to be somebody playing the game. The recipient then has to point to the person who they think is the answer to that question. If the person pointed to wants to know what the question was, they have to take a drink.",
    inline=False)
  playEmb.add_field(
    name="\nTruth or Dare",
    value=
    "Players are given the choice between answering a question truthfully, or performing a dare.",
    inline=False)
  playEmb.add_field(
    name="\nWould You Rather",
    value=
    "One person reads out the WYR question from the list. Whoever is the current player has decided on option '1' or '2', there is no right or wrong answer.",
    inline=False)

  gossipBtn = Button(label="Gossip", style=discord.ButtonStyle.red, emoji="🫢")
  madGabBtn = Button(label="Mad Gab",
                     style=discord.ButtonStyle.green,
                     emoji="🗣️")
  nhieBtn = Button(label="Never Have I Ever",
                   style=discord.ButtonStyle.blurple,
                   emoji="🙅")
  paranoiaBtn = Button(label="Paranoia",
                       style=discord.ButtonStyle.green,
                       emoji="🤫")
  todBtn = Button(label="Truth or Dare",
                  style=discord.ButtonStyle.red,
                  emoji="😈")
  wyrBtn = Button(label="Would You Rather",
                  style=discord.ButtonStyle.blurple,
                  emoji="🎭")
  settingsBtn = Button(label="Setting",
                       style=discord.ButtonStyle.gray,
                       emoji="🛠️")

  playView = View()
  playView.add_item(gossipBtn)
  playView.add_item(madGabBtn)
  playView.add_item(nhieBtn)
  playView.add_item(paranoiaBtn)
  playView.add_item(todBtn)
  playView.add_item(wyrBtn)
  playView.add_item(settingsBtn)

  # Gossip Portion
  async def gossipBtn_callback(interaction):
    gossipEmb = discord.Embed(color=0x992d22)
    gossipEmb.add_field(name="Gossip", value=f"{random.choice(gossipOptions)}")
    await interaction.response.send_message(embed=gossipEmb, view=gossipView)

  gossipBtn2 = Button(label="Gossip", style=discord.ButtonStyle.red, emoji="🫢")

  gossipView = View()
  gossipView.add_item(gossipBtn2)

  async def gossipBtn2_callback(interaction):
    gossipEmb2 = discord.Embed(color=0x992d22)
    gossipEmb2.add_field(name="Gossip",
                         value=f"{random.choice(gossipOptions)}")
    await interaction.response.send_message(embed=gossipEmb2, view=gossipView)

  gossipBtn2.callback = gossipBtn2_callback

  gossipBtn.callback = gossipBtn_callback

  # Mad Gab Portion
  async def madGabBtn_callback(interaction):
    madGabEmb = discord.Embed(color=0x11806a)
    madGabEmb.add_field(name="Mad Gab",
                        value=f"{random.choice(madGabOptions)}")
    await interaction.response.send_message(embed=madGabEmb, view=madGabView)

  madGabBtn2 = Button(label="Mad Gab",
                      style=discord.ButtonStyle.green,
                      emoji="🗣️")

  madGabView = View()
  madGabView.add_item(madGabBtn2)

  async def madGabBtn2_callback(interaction):
    madGabEmb2 = discord.Embed(color=0x11806a)
    madGabEmb2.add_field(name="Mad Gab",
                         value=f"{random.choice(madGabOptions)}")
    await interaction.response.send_message(embed=madGabEmb2, view=madGabView)

  madGabBtn2.callback = madGabBtn2_callback

  madGabBtn.callback = madGabBtn_callback

  # Never Have I Ever Portion
  async def nhieBtn_callback(interaction):
    nhieEmb = discord.Embed(color=0x3498db)
    nhieEmb.add_field(name="Never Have I Ever",
                      value=f"{random.choice(nhieOptions)}")
    await interaction.response.send_message(embed=nhieEmb, view=nhieView)

  nhieBtn2 = Button(label="Never Have I Ever",
                    style=discord.ButtonStyle.blurple,
                    emoji="🙅")

  nhieView = View()
  nhieView.add_item(nhieBtn2)

  async def nhieBtn2_callback(interaction):
    nhieEmb2 = discord.Embed(color=0x3498db)
    nhieEmb2.add_field(name="Never Have I Ever",
                       value=f"{random.choice(nhieOptions)}")
    await interaction.response.send_message(embed=nhieEmb2, view=nhieView)

  nhieBtn2.callback = nhieBtn2_callback

  nhieBtn.callback = nhieBtn_callback

  # Paranoia Portion
  async def paranoiaBtn_callback(interaction):
    paranoiaEmb = discord.Embed(color=0x1f8b4c)
    paranoiaEmb.add_field(name="Paranoia",
                          value=f"{random.choice(parOptions)}")
    await interaction.response.send_message(embed=paranoiaEmb,
                                            view=paranoiaView)

  parBtn2 = Button(label="Paranoia",
                   style=discord.ButtonStyle.green,
                   emoji="🤫")

  paranoiaView = View()
  paranoiaView.add_item(parBtn2)

  async def parBtn2_callback(interaction):
    parEmb2 = discord.Embed(color=0x1f8b4c)
    parEmb2.add_field(name="Paranoia", value=f"{random.choice(parOptions)}")
    await interaction.response.send_message(embed=parEmb2, view=paranoiaView)

  parBtn2.callback = parBtn2_callback

  paranoiaBtn.callback = paranoiaBtn_callback

  # Truth or Dare Portion
  async def todBtn_callback(interaction):
    todEmb = discord.Embed(color=0x992d22)
    todEmb.add_field(name="Truth or Dare", value=f"{random.choice(todRandom)}")
    await interaction.response.send_message(embed=todEmb, view=todView)

  truthBtn = Button(label="Truth", style=discord.ButtonStyle.green, emoji="😇")
  dareBtn = Button(label="Dare", style=discord.ButtonStyle.red, emoji="😈")
  randomBtn = Button(label="Random", style=discord.ButtonStyle.grey, emoji="🎲")

  todView = View()
  todView.add_item(truthBtn)
  todView.add_item(dareBtn)
  todView.add_item(randomBtn)

  async def truthBtn_callback(interaction):
    truthEmb = discord.Embed(color=0x1f8b4c)
    truthEmb.add_field(name="Truth", value=f"{random.choice(truthOptions)}")
    await interaction.response.send_message(embed=truthEmb, view=todView)

  truthBtn.callback = truthBtn_callback

  async def dareBtn_callback(interaction):
    dareEmb = discord.Embed(color=0xe74c3c)
    dareEmb.add_field(name="Dare", value=f"{random.choice(dareOptions)}")
    await interaction.response.send_message(embed=dareEmb, view=todView)

  dareBtn.callback = dareBtn_callback

  async def randomBtn_callback(interaction):
    randomEmb = discord.Embed(color=0x607d8b)
    randomEmb.add_field(name="Random", value=f"{random.choice(todRandom)}")
    await interaction.response.send_message(embed=randomEmb, view=todView)

  randomBtn.callback = randomBtn_callback

  todBtn.callback = todBtn_callback

  # Would You Rather Portion
  async def wyrBtn_callback(interaction):
    wyrEmb = discord.Embed(color=0x9b59b6)
    wyrEmb.set_author(name=f"Requested by {ctx.user.display_name}",
                      icon_url=ctx.user.avatar.url)
    wyrEmb.add_field(name="Would You Rather",
                     value=f"{random.choice(wyrOptions)}")
    await interaction.response.send_message(embed=wyrEmb, view=wyrView)

  wyrBtn2 = Button(label="Would You Rather",
                   style=discord.ButtonStyle.blurple,
                   emoji="🎭")

  wyrView = View()
  wyrView.add_item(wyrBtn2)

  async def wyrBtn2_callback(interaction):
    wyrEmb2 = discord.Embed(color=0x9b59b6)
    wyrEmb2.set_author(name=f"Requested by {ctx.user.display_name}",
                       icon_url=ctx.user.avatar.url)
    wyrEmb2.add_field(name="Would You Rather",
                      value=f"{random.choice(wyrOptions)}")
    await interaction.response.send_message(embed=wyrEmb2, view=wyrView)

  wyrBtn2.callback = wyrBtn2_callback

  wyrBtn.callback = wyrBtn_callback

  await ctx.response.send_message(embed=playEmb, view=playView)


# Gossip Menu
@bot.tree.command(name="gossip", description="Start playing Gossip")
async def gossip(ctx):
  gossipEmb = discord.Embed(color=0x992d22)
  gossipEmb.set_author(name=f"Requested by {ctx.user.display_name}",
                       icon_url=ctx.user.avatar.url)
  gossipEmb.add_field(name="Gossip", value=f"{random.choice(gossipOptions)}")

  gosBtn = Button(label="Gossip", style=discord.ButtonStyle.red, emoji="🫢")

  gosView = View()
  gosView.add_item(gosBtn)

  async def gosBtn_callback(interaction):
    gosEmb = discord.Embed(color=0x992d22)
    gosEmb.set_author(name=f"Requested by {ctx.user.display_name}",
                      icon_url=ctx.user.avatar.url)
    gosEmb.add_field(name="Gossip", value=f"{random.choice(gossipOptions)}")
    await interaction.response.send_message(embed=gosEmb, view=gosView)

  gosBtn.callback = gosBtn_callback

  await ctx.response.send_message(embed=gossipEmb, view=gosView)


# Mad Gab Menu
@bot.tree.command(name="madgab", description="Start playing Mad Gabs")
async def madGab(ctx):
  madGabEmb = discord.Embed(color=0x11806a)
  madGabEmb.set_author(name=f"Requested by {ctx.user.display_name}",
                       icon_url=ctx.user.avatar.url)
  madGabEmb.add_field(name="Mad Gab", value=f"{random.choice(madGabOptions)}")

  madGabBtn2 = Button(label="Mad Gab",
                      style=discord.ButtonStyle.green,
                      emoji="🗣️")

  madGabView = View()
  madGabView.add_item(madGabBtn2)

  async def madGabBtn2_callback(interaction):
    madGabEmb2 = discord.Embed(color=0x11806a)
    madGabEmb2.set_author(name=f"Requested by {ctx.user.display_name}",
                          icon_url=ctx.user.avatar.url)
    madGabEmb2.add_field(name="Mad Gab",
                         value=f"{random.choice(madGabOptions)}")
    await interaction.response.send_message(embed=madGabEmb2, view=madGabView)

  madGabBtn2.callback = madGabBtn2_callback

  await ctx.response.send_message(embed=madGabEmb, view=madGabView)


# Never Have I Ever Menu
@bot.tree.command(name="nhie", description="Start playing Never Have I Ever")
async def nhie(ctx):
  nhieEmb = discord.Embed(color=0x3498db)
  nhieEmb.set_author(name=f"Requested by {ctx.user.display_name}",
                     icon_url=ctx.user.avatar.url)
  nhieEmb.add_field(name="Never Have I Ever",
                    value=f"{random.choice(nhieOptions)}")

  nhieBtn = Button(label="Never Have I Ever",
                   style=discord.ButtonStyle.blurple,
                   emoji="🙅")

  nhieView = View()
  nhieView.add_item(nhieBtn)

  async def nhieBtn_callback(interaction):
    nhieQEmb = discord.Embed(color=0x3498db)
    nhieQEmb.set_author(name=f"Requested by {ctx.user.display_name}",
                        icon_url=ctx.user.avatar.url)
    nhieQEmb.add_field(name="Never Have I Ever",
                       value=f"{random.choice(nhieOptions)}")
    await interaction.response.send_message(embed=nhieQEmb, view=nhieView)

  nhieBtn.callback = nhieBtn_callback

  await ctx.response.send_message(embed=nhieEmb, view=nhieView)


# Paranoia Menu
@bot.tree.command(name="paranoia", description="Start playing Paranoia")
async def paranoia(ctx):
  parEmb = discord.Embed(color=0x1f8b4c)
  parEmb.set_author(name=f"Requested by {ctx.user.display_name}",
                    icon_url=ctx.user.avatar.url)
  parEmb.add_field(name="Paranoia", value=f"{random.choice(parOptions)}")

  parBtn = Button(label="Paranoia", style=discord.ButtonStyle.green, emoji="🤫")

  parView = View()
  parView.add_item(parBtn)

  async def parBtn_callback(interaction):
    parQEmb = discord.Embed(color=0x1f8b4c)
    parQEmb.set_author(name=f"Requested by {ctx.user.display_name}",
                       icon_url=ctx.user.avatar.url)
    parQEmb.add_field(name="Paranoia", value=f"{random.choice(parOptions)}")
    await interaction.response.send_message(embed=parQEmb, view=parView)

  parBtn.callback = parBtn_callback

  await ctx.response.send_message(embed=parEmb, view=parView)


# TOD Menu
@bot.tree.command(name="tod", description="Start playing Truth or Dare")
async def tod(ctx):
  todEmb = discord.Embed(color=0x992d22)
  todEmb.set_author(name=f"Requested by {ctx.user.display_name}",
                    icon_url=ctx.user.avatar.url)
  todEmb.add_field(name="Truth or Dare", value=f"{random.choice(todRandom)}")

  truthBtn = Button(label="Truth", style=discord.ButtonStyle.green, emoji="😇")
  dareBtn = Button(label="Dare", style=discord.ButtonStyle.red, emoji="😈")
  randomBtn = Button(label="Random", style=discord.ButtonStyle.grey, emoji="🎲")

  todView = View()
  todView.add_item(truthBtn)
  todView.add_item(dareBtn)
  todView.add_item(randomBtn)

  async def truthBtn_callback(interaction):
    truthEmb = discord.Embed(color=0x1f8b4c)
    truthEmb.set_author(name=f"Requested by {ctx.user.display_name}",
                        icon_url=ctx.user.avatar.url)
    truthEmb.add_field(name="Truth", value=f"{random.choice(truthOptions)}")
    await interaction.response.send_message(embed=truthEmb, view=todView)

  truthBtn.callback = truthBtn_callback

  async def dareBtn_callback(interaction):
    dareEmb = discord.Embed(color=0xe74c3c)
    dareEmb.set_author(name=f"Requested by {ctx.user.display_name}",
                       icon_url=ctx.user.avatar.url)
    dareEmb.add_field(name="Dare", value=f"{random.choice(dareOptions)}")
    await interaction.response.send_message(embed=dareEmb, view=todView)

  dareBtn.callback = dareBtn_callback

  async def randomBtn_callback(interaction):
    randomEmb = discord.Embed(color=0x607d8b)
    randomEmb.set_author(name=f"Requested by {ctx.user.display_name}",
                         icon_url=ctx.user.avatar.url)
    randomEmb.add_field(name="Random", value=f"{random.choice(todRandom)}")
    await interaction.response.send_message(embed=randomEmb, view=todView)

  randomBtn.callback = randomBtn_callback

  await ctx.response.send_message(embed=todEmb, view=todView)


# Would You Rather Menu
@bot.tree.command(name="wyr", description="Start playing Would You Rather")
async def wyr(ctx):
  wyrEmb = discord.Embed(color=0x9b59b6)
  wyrEmb.set_author(name=f"Requested by {ctx.user.display_name}",
                    icon_url=ctx.user.avatar.url)
  wyrEmb.add_field(name="Would You Rather",
                   value=f"{random.choice(wyrOptions)}")
  wyrBtn = Button(label="Would You Rather",
                  style=discord.ButtonStyle.blurple,
                  emoji="🎭")

  wyrView = View()
  wyrView.add_item(wyrBtn)

  async def wyrBtn_callback(interaction):
    wyrQEmb = discord.Embed(color=0x9b59b6)
    wyrQEmb.add_field(name="Would You Rather",
                      value=f"{random.choice(wyrOptions)}")
    await interaction.response.send_message(embed=wyrQEmb, view=wyrView)

  wyrBtn.callback = wyrBtn_callback

  await ctx.response.send_message(embed=wyrEmb, view=wyrView)


my_secret = os.environ['TOKEN']

keep_alive()
bot.run(my_secret)
