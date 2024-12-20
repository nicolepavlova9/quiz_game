from storage.api_handler import ApiHandler
from models.player import Player
from models.question import Question
from storage.helper_functions import get_topic_id


class Game:
    def __init__(self):
        self.api_handler = ApiHandler()
        self.player = None
        self.questions = []
        self.score = 0

    def start_game(self):
        if not self.player:
            self.player = Player(input("Hello, what is your name?: "))

        if not self.player.is_setup:
            self.player.setup_player()

        self.api_handler.get_token()
        questions_data = self.api_handler.fetch_questions(
            q_type="multiple",
            amount=10,
            category=get_topic_id(self.player.topic),
            difficulty=self.player.difficulty,
        )

        self.questions = [
            Question(question["question"], question["correct_answer"])
            for question in questions_data
        ]

        for question in self.questions:
            print(question.question)
            user_answer = input("Your answer: ")

            if user_answer.lower() == question.correct_answer.lower():
                self.score += 1
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is {question.correct_answer}.")

        print(f"Your final score is: {self.score}/{len(self.questions)}")
