import os
from dotenv import load_dotenv

load_dotenv('src/.env')

GITHUB_API_TOKEN = os.environ.get('GITHUB_API_TOKEN')
OPENAI_API_TOKEN = os.environ.get('OPENAI_API_TOKEN')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
