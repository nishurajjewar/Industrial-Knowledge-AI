import json
import os
from collections import Counter

LOG_FILE = "logs/query_log.json"


def get_analytics():

    os.makedirs("logs", exist_ok=True)

    if not os.path.exists(LOG_FILE):
        return {
            "total_queries": 0,
            "top_topics": []
        }

    with open(LOG_FILE, "r") as file:
        queries = json.load(file)

    questions = [item["question"] for item in queries]

    counter = Counter(questions)

    top_topics = []

    for question, count in counter.most_common(5):
        top_topics.append({
            "question": question,
            "count": count
        })

    return {
        "total_queries": len(questions),
        "top_topics": top_topics
    }