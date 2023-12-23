import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

URL_API = os.getenv("URL_API")
PATH_AUTH = "/users/local/authenticate"
PATH_ACC = "/users/account-data"
BALANCE = "/affiliates/balances"
DATA_AUTH = {
    "browserFingerprint": "1231231231231231212312312",
    "email": email,
    "password": password
    }

def fpath(path: str) -> str:
    return URL_API + path

session = requests.session()
auth = session.post(fpath(PATH_AUTH), DATA_AUTH)
print("status auth",auth.status_code)
acc_data = session.get(fpath(PATH_ACC))
print(json.dumps(acc_data.json(), indent=2))
userId = acc_data.json()["userId"]
print("userId", userId)
