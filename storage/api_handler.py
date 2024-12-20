import requests
import logging

logging.basicConfig(level=logging.INFO)


class ApiHandler:
    def __init__(self, base_url="https://opentdb.com/"):
        self.base_url = base_url
        self.session_token = None
        self.session = requests.Session()

    def get_token(self):
        if not self.base_url:
            logging.error("Base URL is not set")
            return None

        url = f"{self.base_url}/api_token.php?command=request"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json()
            if data["response_code"] == 0:
                self.session_token = data["token"]
                return self.session_token
            else:
                logging.warning(f"Failed to get token: {data['response_message']}")
                return None
        except requests.RequestException as e:
            logging.error(f"Error fetching token: {e}")
            return None

    def fetch_questions(self, q_type, amount, category, difficulty):
        if not self.session_token:
            logging.error("Session token is not set")
            return []

        if not q_type or not amount:
            logging.error("Question type and amount are required")
            return []

        params = {
            "type": q_type,
            "amount": amount,
            "token": self.session_token,
        }
        if category:
            params["category"] = category
        if difficulty:
            params["difficulty"] = difficulty

        if category:
            url = f"{self.base_url}/api.php?amount={amount}&category={category}&difficulty={difficulty}"
        else:
            url = f"{self.base_url}/api.php?amount={amount}&difficulty={difficulty}"
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            if data["response_code"] == 0:
                return data["results"]
            else:
                logging.warning(f"Failed to fetch questions")
                return []
        except requests.RequestException as e:
            logging.error(f"Error fetching questions: {e}")
            return []
