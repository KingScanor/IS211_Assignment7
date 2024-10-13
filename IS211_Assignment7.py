# Assignment 7
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self. is_turn = False
        self.turn_total = 0

    def roll_die(self, die):
        roll = die.roll()
        if roll == 1:
            print(f"Turn Over! {self.name} rolled a 1.\n")
            self.reset_turn()
            return False
        else:
            self.turn_total += roll
            print (f"\n1"
                   f"\n{self.name} rolled a {roll}. Turn Total: {self.turn_total}, Total Score: {self.score}\n")
            return True

    def hold(self):
        self.score += self.turn_total
        print (f"{self.name} holds. Total Score: {self.score}\n")
        self.reset_turn()

    def reset_turn(self):
        self.turn_total = 0
        self.is_turn = False

class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class Game:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player (player1_name)
        self.player2 = Player (player2_name)
        self.current_player = self.player1
        self.current_player.is_turn = True
        self.die = Die()

    def start_game(self):
        while self.player1.score < 100 and self.player2.score < 100:
            self.play_turn()

    def play_turn(self):
        print(f"\n{self.current_player.name}'s turn:")
        while self.current_player.is_turn:
            decision = input("Roll (1) or Hold (2)?").lower()
            if decision == '1':
                if not self.current_player.roll_die(self.die):
                    self.switch_turn()
            elif decision == '2':
                self.current_player.hold()
                self.switch_turn()
            else:
                print("Invalid input, Please type '1' for Roll or '2' for Hold.")

            if self.player1.score >= 100 or self.player2.score >= 100:
                self.check_winner()
                return

    def switch_turn(self):
        self.current_player.is_turn = False
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        self.current_player.is_turn = True
        self.display_scores()
        self.display_current_player()

    def display_scores(self):
        print (f"\nScores - {self.player1.name}: {self.player1.score}, {self.player2.name}: {self.player2.score}\n")

    def display_current_player(self):
        print (f"\n{self.current_player.name}'s turn:")

    def check_winner(self):
        if self.player1.score >= 100:
            print (f"\nCongratulations to the winner,{self.player1.name}.")
        elif self.player2.score >= 100:
            print(f"\nCongratulations to the winner,{self.player2.name}.")

if __name__ == "__main__":
    game = Game("Player 1","Player 2")
    game.start_game()






