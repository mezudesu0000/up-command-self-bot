import discord
import os
from flask import Flask
import threading

TOKEN = os.environ.get('USER_TOKEN')
CHANNEL_ID = 1421271498785685554
CMD_ID = 1363739182672904354

client = discord.Client(intents=discord.Intents.default())  # discord.py-self 用 Client
app = Flask(__name__)

@app.route("/")
def home():
    return "Self-bot is running!"

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        commands = await channel.guild.fetch_application_commands(discord.Object(id=client.user.id))
        cmd = discord.utils.get(commands, id=CMD_ID)
        if cmd:
            await cmd(channel=channel)
            print("upコマンドを実行しました")
        else:
            print("コマンドが見つかりません")

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_flask).start()
client.run(TOKEN, bot=False)
