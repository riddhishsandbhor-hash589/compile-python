import random
import math

class LuckyNumberGame:
    def __init__(self):
        self.level = 1
        self.max_level = 100
        self.score = 0
        self.attempts = 0
        self.max_attempts = 5
        self.lucky_number = 0
        self.game_state = "playing"  # playing, won, lost
        self.hint = ""
        self.range_end = 10
        self.generate_new_number()
    
    def generate_new_number(self):
        """Generate a new lucky number based on current level"""
        self.range_end = 10 + (self.level - 1) * 2
        self.lucky_number = random.randint(1, self.range_end)
        self.attempts = 0
        self.game_state = "playing"
        self.hint = f"Level {self.level}: Guess a number between 1 and {self.range_end}"
    
    def make_guess(self, guess):
        """Process a player's guess"""
        if self.game_state != "playing":
            return
            
        self.attempts += 1
        
        if guess == self.lucky_number:
            self.game_state = "won"
            points = (self.max_attempts - self.attempts + 1) * self.level * 10
            self.score += points
            self.hint = f"Correct! You earned {points} points. Press 'N' for next level."
        elif self.attempts >= self.max_attempts:
            self.game_state = "lost"
            self.hint = f"Game Over! The number was {self.lucky_number}. Press 'R' to restart."
        else:
            if guess < self.lucky_number:
                self.hint = f"Too low! Attempts left: {self.max_attempts - self.attempts}"
            else:
                self.hint = f"Too high! Attempts left: {self.max_attempts - self.attempts}"
    
    def next_level(self):
        """Advance to the next level"""
        if self.game_state == "won" and self.level < self.max_level:
            self.level += 1
            self.generate_new_number()
        elif self.level >= self.max_level:
            self.hint = "Congratulations! You've completed all 100 levels!"
    
    def restart(self):
        """Restart the game from level 1"""
        self.level = 1
        self.score = 0
        self.generate_new_number()

def draw_game_state(game):
    """Draw the current game state"""
    print("\n" + "="*50)
    print(f"LUCKY NUMBER GAME - Level {game.level}/{game.max_level}")
    print("="*50)
    print(f"Score: {game.score}")
    print(f"Attempts: {game.attempts}/{game.max_attempts}")
    print(f"Number Range: 1 - {game.range_end}")
    print("-"*50)
    print(game.hint)
    
    if game.game_state == "playing":
        print("\nEnter your guess (or 'q' to quit):")
    elif game.game_state == "won":
        print("\n[N]ext Level  [R]estart  [Q]uit")
    elif game.game_state == "lost":
        print("\n[R]estart  [Q]uit")

def main():
    """Main game loop"""
    print("Welcome to the Lucky Number Game!")
    print("Guess the number within 5 attempts to advance to the next level.")
    
    game = LuckyNumberGame()
    
    while True:
        draw_game_state(game)
        
        if game.game_state == "playing":
            try:
                user_input = input("> ").strip().lower()
                
                if user_input == 'q':
                    print("Thanks for playing!")
                    break
                    
                guess = int(user_input)
                
                if 1 <= guess <= game.range_end:
                    game.make_guess(guess)
                else:
                    game.hint = f"Please enter a number between 1 and {game.range_end}"
                    
            except ValueError:
                game.hint = "Please enter a valid number!"
                
        else:  # Won or lost state
            user_input = input("> ").strip().lower()
            
            if user_input == 'n' and game.game_state == "won":
                game.next_level()
            elif user_input == 'r':
                game.restart()
            elif user_input == 'q':
                print("Thanks for playing!")
                break
            else:
                if game.game_state == "won":
                    game.hint = "Invalid input. Press 'N' for next level, 'R' to restart, or 'Q' to quit."
                else:
                    game.hint = "Invalid input. Press 'R' to restart or 'Q' to quit."

if __name__ == "__main__":
    main()
