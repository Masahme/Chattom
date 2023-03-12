from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", 9157919))

API_HASH = getenv("API_HASH", "b90c282e584222babde5f68b5b63ee3b")

BOT_TOKEN = getenv("BOT_TOKEN", "5921031219:AAHgPZysStwEE6APKt9W2oOaDfsDDtLi9mE")

OPENAI_API = getenv("OPENAI_API", "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") # get api key : https://platform.openai.com/account/api-keys
