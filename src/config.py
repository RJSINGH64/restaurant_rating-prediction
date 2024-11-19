from dotenv import load_dotenv
from dataclasses import dataclass
import os ,sys
import pymongo as pm

print(f' Loading .env')
load_dotenv()

#creating class for Environment Variables
@dataclass
class EnvironmentVariables:
    mongo_url:str=os.getenv("MONGO_DB_URL")



env=EnvironmentVariables()

mongo_client=pm.MongoClient(env.mongo_url)
print(f'Connected to MongoDB Database')