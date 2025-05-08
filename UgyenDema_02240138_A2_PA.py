

import random
from UgyenDema_02240138_A2_PB import PokemonOrganizer

# Main Application


def main():
    system = GameCollection()
    
    while True:
        print("\n==== Game Hub ====")
        print("1. Number Guesser")
        print("2. RPS Challenge")
        print("3. Trivia Quiz")
        print("4. Pokemon Manager")
        print("5. View Scores")
        print("0. Exit")
        
        choice = input("Select game (0-5): ")
        
        if choice == '1':
            game = NumberGuesser()
            system.scores['number_guesser'] += game.start_game()
        elif choice == '2':
            game = RPSChallenge()
            system.scores['rps_battles'] += game.play_round()
        elif choice == '3':
            game = TriviaChallenge()
            system.scores['quiz_challenge'] += game.start_quiz()
        elif choice == '4':
            while True:
                print("\n==== Pokemon Manager ====")
                print("1. Add New Pokemon")
                print("2. View Collection")
                print("3. Reset Collection")
                print("4. Return to Main")
                
                sub_choice = input("Select option (1-4): ")
                
                if sub_choice == '1':
                    system.pokemon_manager.add_pokemon()
                    system.scores['pokemon_tracker'] = len(system.pokemon_manager.collected)
                elif sub_choice == '2':
                    system.pokemon_manager.show_collection()
                elif sub_choice == '3':
                    system.pokemon_manager.reset_collection()
                    system.scores['pokemon_tracker'] = 0
                elif sub_choice == '4':
                    break
                else:
                    print("Invalid selection")
        elif choice == '5':
            system.show_scores()
        elif choice == '0':
            print("Thanks for playing!")
            break
        else:
            print("Invalid selection")


# Game Collection System



class GameCollection:
    def __init__(self):
        self.scores = {
            'number_guesser': 0,
            'rps_battles': 0,
            'quiz_challenge': 0,
            'pokemon_tracker': 0
        }
        self.pokemon_manager = PokemonOrganizer()

    def show_scores(self):
        print("\n=== Current Scores ===")
        for game, score in self.scores.items():
            print(f"{game.replace('_', ' ').title()}: {score}")
        print(f"Total Score: {sum(self.scores.values())}")


# Number Guessing Game


class NumberGuesser:
    def __init__(self):
        self.range_start = 1
        self.range_end = 50
        self.max_attempts = 7
        
    def start_game(self):
        target = random.randint(self.range_start, self.range_end)
        print(f"\nGuess the number between {self.range_start}-{self.range_end}")
        
        for attempt in range(1, self.max_attempts + 1):
            try:
                guess = int(input(f"Attempt {attempt}/{self.max_attempts}: "))
            except ValueError:
                print("Please enter a valid number")
                continue
                
            if guess == target:
                points = self.max_attempts - attempt + 1
                print(f"Correct! Earned {points} points")
                return points
            print("Too high!" if guess > target else "Too low!")
            
        print(f"Game Over! Number was {target}")
        return 0

# Rock-Paper-Scissors Game


class RPSChallenge:
    CHOICES = ['rock', 'paper', 'scissors']
    
    def __init__(self):
        self.wins = 0
        self.rounds = 5
        
    def play_round(self):
        print("\nFirst to 3 wins! (Best of 5)")
        while self.wins < 3 and (self.rounds - self.wins) > 0:
            user = input("Choose (rock/paper/scissors): ").lower()
            if user not in self.CHOICES:
                print("Invalid choice")
                continue
                
            computer = random.choice(self.CHOICES)
            print(f"Computer chose: {computer}")
            
            if user == computer:
                print("Tie!")
            elif (user == 'rock' and computer == 'scissors') or \
                 (user == 'paper' and computer == 'rock') or \
                 (user == 'scissors' and computer == 'paper'):
                self.wins += 1
                print("You win this round!")
            else:
                print("Computer wins this round!")
                
        return self.wins


# Trivia Challenge


class TriviaChallenge:
    def __init__(self):
        self.questions = {
'Programming Methodology': [
("Which of the following is NOT a characteristic of a good programming methodology?", ['Complexity', 'Modularity', 'Maintainability', 'Scalability'], 0),
                ("What is the primary purpose of structured programming?", ['Making code shorter', 'Improving code readability', 'Reducing errors', 'Enhancing performance'], 1)

            ],
            'Python': [
("Which data type is mutable in Python?", ['Tuple', 'List', 'String', 'Dictionary'], 2)
            ]
        }
        
    def start_quiz(self):
        total = 0
        print("\nAvailable Categories:")
        for idx, cat in enumerate(self.questions.keys(), 1):
            print(f"{idx}. {cat}")
            
        try:
            choice = int(input("Select category (1-2): ")) - 1
            category = list(self.questions.keys())[choice]
        except (ValueError, IndexError):
            print("Invalid selection")
            return 0
            
        print(f"\n{category} Quiz:")
        for q_num, (question, options, ans) in enumerate(self.questions[category], 1):
            print(f"\nQ{q_num}: {question}")
            for i, opt in enumerate(options, 1):
                print(f"{i}. {opt}")
                
            while True:
                try:
                    user_ans = int(input("Your answer (1-4): ")) - 1
                    if 0 <= user_ans < 4:
                        break
                except ValueError:
                    print("Invalid input")
                    
            if user_ans == ans:
                print("Correct!")
                total += 1
            else:
                print(f"Wrong! Answer: {options[ans]}")
                
        print(f"\nFinal Score: {total}/{len(self.questions[category])}")
        return total




if __name__ == "__main__":
    main()