from typing import Any
import requests


def get_categories() -> dict:
    try:
        response = requests.get("https://opentdb.com/api_category.php")
        response.raise_for_status()
        return response.json().get("trivia_categories", {})
    except requests.RequestException as e:
        print(f"Error fetching categories: {e}")
        return {}


def select_one_topic() -> int | None:
    topics = get_categories()
    if not topics:
        print("No categories available.")
        return None

    for idx, topic in enumerate(topics, start=1):
        print(f"{idx}. {topic['name']}")

    while True:
        try:
            selected_topic = int(input(f"Select topic (1-{len(topics)}): "))
            if 1 <= selected_topic <= len(topics):
                return selected_topic
            else:
                print("Invalid topic number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_topic_id(topic_name: str) -> Any | None:
    topics = get_categories()
    if not topics:
        print("No categories available.")
        return None

    return next((topic["id"] for topic in topics if topic["name"] == topic_name), None)
