from storage.helper_functions import get_categories, select_one_topic, get_topic_id


class Player:
    def __init__(self, player_name: str):
        self._player_name = player_name
        self.score = 0
        self.is_setup = False
        self.difficulty = "medium"
        self.topic = None

    @property
    def player_name(self) -> str:
        return self._player_name

    @player_name.setter
    def player_name(self, value: str):
        if not (3 <= len(value) <= 20):
            raise ValueError("Name must be between 3 and 20 characters")
        self._player_name = value

    def select_difficulty(self) -> None:
        while True:
            try:
                difficulty_choice = int(
                    input("Select difficulty (1. Easy, 2. Medium, 3. Hard): ")
                )
                if 1 <= difficulty_choice <= 3:
                    self.difficulty = ["easy", "medium", "hard"][difficulty_choice - 1]
                    break
            except ValueError:
                pass

    def select_topic(self) -> None:
        while True:
            try:
                self.topic = select_one_topic()
                break
            except KeyError:
                pass

    def setup_player(self) -> None:
        print(f"Welcome to the Trivia Game, {self.player_name}!")
        self.select_difficulty()
        if (
            input("Do you want to select a topic? Default is random (y/n): ").lower()
            == "y"
        ):
            self.select_topic()
        self.is_setup = True

    def update_score(self, new_score: int) -> None:
        self.score += new_score

    def __str__(self) -> str:
        return f"{self.player_name}: {self.score}"
