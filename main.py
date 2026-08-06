import os

from dotenv import load_dotenv

from app import create_app

load_dotenv()
env = os.environ.get("API_ENV", "dev")
app = create_app(env)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)