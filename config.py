import os
from dotenv import load_dotenv
load_dotenv()
# print(os.getenv('DATABASE_URL'))
# print(os.environ.get('SECRET_KEY'))
# print(os.getenv("PYTHONPATH"))
env = os.getenv("DATABASE_URL")
print(env)
