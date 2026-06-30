import json
import os

LOG_FILE = "logs/query_log.json"


def log_query(question):

    os.makedirs("logs", exist_ok=True)

    if os.path.exists(LOG_FILE):

        with open(LOG_FILE, "r") as file:
            data = json.load(file)

    else:

        data = []

    data.append({
        "question": question
    })

    with open(LOG_FILE, "w") as file:
        json.dump(data, file, indent=4)