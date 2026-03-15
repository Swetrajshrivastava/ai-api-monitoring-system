import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
import json
import time
from datetime import datetime
from utils.alert_system import check_alert
# Load API list
with open("config/api_list.json") as f:
    data = json.load(f)

apis = data["apis"]

LOG_FILE = "logs/api_logs.json"


def check_api(api):

    start = time.time()

    try:
        response = requests.get(api)

        response_time = round(time.time() - start, 2)

        result = {
            "api": api,
            "status": response.status_code,
            "response_time": response_time,
            "timestamp": str(datetime.now())
        }

    except Exception:

        result = {
            "api": api,
            "status": "ERROR",
            "response_time": None,
            "timestamp": str(datetime.now())
        }

    return result


def save_log(result):

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(result)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)


def monitor():

    while True:

        print("\nChecking APIs...")

        for api in apis:

            result = check_api(api)

            print(result)

            save_log(result)

            check_alert(result)

        print("Waiting 5 seconds...")

        time.sleep(5)


if __name__ == "__main__":
    monitor()