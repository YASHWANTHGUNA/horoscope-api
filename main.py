# main.py (Modified)
from core import app
from dotenv import load_dotenv

load_dotenv() # Loads the .env file

if __name__ == '__main__':
    app.run()