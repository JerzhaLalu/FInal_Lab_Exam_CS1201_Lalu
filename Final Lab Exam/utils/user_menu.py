from utils.dicegame import *

class User_menu:

    def usermenu():
        user_manager = UserManager()
        while True:
            print("\n1. Register\n2. Login\n3. Exit")
            choice = input("Select an option: ").strip()
            
            if choice == '1':
                user_manager.register()
            elif choice == '2':
                user_manager.log_in()
                if user_manager.username:  
                    print(" - Dice Game Menu - ")
                    print ("[1] Play Dice game")
                    print ("[2] Show Leaderboard")
                    print ("[3] Log Out")

                    choice = input("Enter your choice:")
                    
                    if choice == '1':
                        game = Game(user_manager.username)
                        game.dice_game()
                    elif choice == '2':
                        user_manager.show_top_10_scores()
                        User_menu.usermenu()
                    elif choice == '3':
                        break

            elif choice == '3':
                break
            else:
                print("Invalid choice. Please select again.")