import os

from dotenv import load_dotenv

load_dotenv()

MJ_APIKEY_PUBLIC = os.environ.get("MJ_APIKEY_PUBLIC")
MJ_APIKEY_PRIVATE = os.environ.get("MJ_APIKEY_PRIVATE")
