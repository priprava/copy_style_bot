from dotenv import load_dotenv
import os, json

load_dotenv()
os.chdir(os.path.dirname(os.path.abspath(__file__)))

BOT_TOKEN=os.getenv("BOT_TOKEN")
COMFY_API=os.getenv("COMFY_API")

with open(os.path.dirname(os.path.abspath(__file__)) + "/lora.json") as f:
    templates = json.load(f)

STYLE=templates