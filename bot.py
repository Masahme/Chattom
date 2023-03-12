import logging

from typing import *

from pyrogram import Client

from pyrogram import *

from pyrogram.types import *

from config import API_ID, API_HASH, BOT_TOKEN

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":

    plugins = dict(root="chatgpt")

app = Client(

    api_id=API_ID,

    api_hash=API_HASH,

    bot_token=BOT_TOKEN,

    plugins=plugins,

    workers=300,

)

app.run()

