import os
import random
from datetime import datetime



class Game:
    def __init__(self, username):
        self.username = username
        self.total_score = 0
        self.stage = 1
        self.score_manager = ScoreManager()

    def dice_game(self):
        while True:
            self.rounds = 3
            self.round_counter = 0
            self.round_count = 1

            self.cpu_score = 0
            self.user_score = 0

            print(f"Welcome to Dice Game, {self.username}!\n")
            print(f"\n ------ Stage {self.stage} ------")
        
            while self.round_counter < self.rounds:
                print(f"\n -- Round {self.round_count} -- ")
                
                self.cpu_random_number = random.randint(1, 6)
                print(f"CPU Generated random number: {self.cpu_random_number} ")
                
                self.user_random_number = random.randint(1, 6)
                print(f"User Generated random number: {self.user_random_number} ")

                if self.cpu_random_number == self.user_random_number:
                    print("You tied.")

                    print (f"CPU score:{self.cpu_score} ")
                    print (f"User score:{self.user_score} ")

                    self.round_count += 1
                    self.round_counter += 0
                    
                elif self.cpu_random_number > self.user_random_number:
                    self.cpu_score += 1
                    self.round_count +=1
                    self.round_counter +=1

                    print(f"CPU score: {self.cpu_score}")
                    print(f"User score: {self.user_score}")

                else:
                    self.user_score += 1
                    self.total_score += 1
                    self.round_count +=1
                    self.round_counter +=1

                    print(f"CPU score: {self.cpu_score}")
                    print(f"User score: {self.user_score}")

            if self.cpu_score > self.user_score:
                print(f"\nYour total score is {self.total_score}")
                print(f"\nCPU wins! Better luck next time.")
                choice = input(f"\nPlay again? [1] Yes  [2] No : ")

                if choice != '1':
                    print(f"\nThank you for playing!")
                    print(f"Total score: {self.total_score}")
                    print(f"Stage: {self.stage}")
                    self.save_score()

                    self.total_score = 0
                    self.stage = 1
                    break

                else:
                    print(f"Total score: {self.total_score}")
                    print(f"Stage: {self.stage}")
                    self.save_score()

                    self.total_score = 0
                    self.stage = 1

            elif self.cpu_score < self.user_score:
                self.total_score += 3
                self.stage += 1
                print(f"\nYour total score is {self.total_score}")
                print(f"\nUser wins! You can proceed to the next stage.")
                choice = input(f"\nPlay again? [1] Yes  [2] No : ")
                
                if choice != '1':
                    print(f"\nThank you for playing!")
                    print(f"Total score: {self.total_score}")
                    print(f"Stage: {self.stage}")
                    self.save_score()

                    self.total_score = 0
                    self.stage = 1
                    break

                else:
                    print(f"Total score: {self.total_score}")
                    print(f"Stage: {self.stage}")
                    self.save_score()

                    

        return self.total_score, self.stage

    def save_score(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.score_manager.save_score(self.username, self.total_score, self.stage, current_datetime)

class ScoreManager:
    def __init__(self, data_folder="data", score_file_name="scores.txt"):
        self.data_folder = data_folder
        self.score_file = os.path.join(self.data_folder, score_file_name)
        self.create_data_folder()

    def create_data_folder(self):
        
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

    def save_score(self, username, score, stage, date):
        
        try:
            with open(self.score_file, "a") as file:
                file.write(f"{username} , {score} , {stage} , {date}\n")
            print(f"Score for {username} saved successfully.")
        except IOError:
            print("Error: Unable to save the score.")

    def load_scores(self):
        
        if os.path.exists(self.score_file):
            try:
                with open(self.score_file, "r") as file:
                    scores = file.readlines()
                    return [line.strip().split(',') for line in scores]
            except IOError:
                print("Error: Unable to read the scores.")
        else:
            print("Score file does not exist.")
        return []

    def get_top_10_scores(self):
        scores = self.load_scores()
        scores = [(user, int(score), int(stage), date) for user, score, stage, date in scores]
        scores.sort(key=lambda x: x[1], reverse=True)  
        return scores[:10]
    
    
class UserManager:

    def register(self):
        db = open("accounts.txt", "r")
        
        print(f"\n --- User Registration --- \n")
        
        self.username = input(f"Enter your username: ").strip()
        
        d = []
        f = []

        for i in db:
            a, b = i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
        
        if self.username in d:
            print(f"\nUsername already exists, try another one.")
            self.register()

        if len(self.username) < 4:
            print(f"\nUsername must be 4 characters long. Try again.")
            self.register()

        while True:
            try:                                        
                self.password = input("Enter your password: ").strip()
                
                if len(self.password) < 8:
                    print(f"\nPassword must be 8 characters long. Try again")
                    continue

                self.repeat_password = input("Re-enter password: ").strip()

                if self.password == self.repeat_password:
                    
                    db = open("accounts.txt", "a")
                    db.write(self.username + "," + self.password + "\n") 

                    print(f"\nSign up successful!\n") 

                    break

                else:
                    print("Passwords do not match. Try again.")
            except ValueError as e:
                print(e)

    def log_in(self):
        try:
            with open("accounts.txt", "r") as db:
                print(f"\n --- User Login --- \n")

                while True:
                    self.username = input("Enter your username: ").strip()

                    if not self.username:
                        print("Username cannot be empty. Please try again.")
                        continue

                    self.password = input("Enter password: ").strip()

                    found = False
                    for line in db:
                        user, pwd = line.strip().split(',')
                        if self.username == user and self.password == pwd:
                            print(f"\nLog In Successful!")
                            found = True
                            break

                    if found:
                        break
                    else:
                        print(f"\nUsername or password is incorrect. Try again.")
                        db.seek(0)  

        except FileNotFoundError:
            print("Database file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def show_top_10_scores(self):
        score_manager = ScoreManager()
        top_scores = score_manager.get_top_10_scores()
        print("\n\t\t--- Top 10 Scores ---\n")
        print(f"RANK\t USERNAME\t SCORE\t STAGE\t DATE ACHIEVED")
        for rank, (user, score, stage, date) in enumerate(top_scores, start=1):
            
            print(f" {rank}\t {user}\t\t   {score}\t   {stage}\t {date}")

      

    

