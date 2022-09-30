# bot.py
# Daniel Kogan
# 09.28.2022

from discord.ext import commands
from dotenv import load_dotenv
import discord
import os
import datetime
import pymongo  # import database api

intents = discord.Intents.all()
load_dotenv()
TOKEN = os.environ.get('TOKEN', 3)

client = pymongo.MongoClient(f"mongodb+srv://" + os.environ.get("DBUSER") + ":" + os.environ.get(
    "DBPASSWORD") + "@" + os.environ.get("DBUSER") + ".c0rpsj1.mongodb.net/?retryWrites=true&w=majority")
db = client.discord  # this will create the database
# this will create our collection, our data is stored in the collection
exampleCollection = db.exampleCollection

bot = commands.Bot(command_prefix="m", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def create(ctx, key, value):
    get_from_database = exampleCollection.find_one({'author': ctx.author.id})
    if (get_from_database != None): 
      exampleCollection.update_one({'author': ctx.author.id}, {"$set": {key:value}})
    else : 
      example_entry = {
        # implement this new author line
        'author': ctx.author.id,
        key: value
      }
      exampleCollection.insert_one(example_entry)
      #example_entry = {key:value}
    await ctx.send("submitted")

@bot.command()
async def remove(ctx, key):
    get_from_database = exampleCollection.find_one({'author': ctx.author.id, key: {'$exists': True}})
    if (get_from_database != None): 
      exampleCollection.update_one({'author': ctx.author.id}, {"$unset": {key:""}})
      await ctx.send(f"removed key {key}")
    else: 
      await ctx.send(f"key {key} does not exist")

@bot.command()
async def delete(ctx):
    get_from_database = exampleCollection.find_one({'author': ctx.author.id})
    if (get_from_database != None): 
      exampleCollection.delete_one({'author': ctx.author.id})
      await ctx.send(f"deleted user profile")
    else: 
      await ctx.send(f"user profile does not exist")

@bot.command()
async def read(ctx, key):
    get_from_database = exampleCollection.find_one({'author': ctx.author.id})
    await ctx.send(get_from_database[key])

bot.run(TOKEN)
