import dotenv
import os

dotenv.load_dotenv()

token = os.getenv("bot_token")
file_location = os.getenv("file_location")