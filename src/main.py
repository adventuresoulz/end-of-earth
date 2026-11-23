# a "playing" game state
def play_game():
    playing = True
    while playing: # TODO create an in game playing menu
        print("you are playing")


# menu options
def show_menu():
    print("Menu Options: Type in your command")
    print("Type 'start' to begin your adventure")
    print("Type 'continue' to resume your adventure")
    print("Type 'save' to save your adventure")
    print("Type 'quit' to exit")
    print("Type 'help' to see the help menu")


# opening game menu
def main_menu_loop(player_options):
    match player_options:
        case "start":
            print("The forgotten hero slowly comes to....")
            play_game()
            return True
        case "continue":
            print("The journey continues...")
            return True
        case "save":
            print("Game saved")
            return True
        case "help":
            print("This help menu")
            return True
        case "exit" | "quit":
            print("Game exited")
            return False
        case _:
            print("Invalid option")
            return True


def main():

    print("Welcome to End of Earth!")
    print("This game was made by Anthony")
    print("A text based fantasy adventure set in a far away land where the lost hero awakens\nIn a strange unknown location")

    game_running = True

    show_menu()

    while game_running:
        player_options = input("Choose your option: ").strip().lower()
        game_running = main_menu_loop(player_options)


if __name__ == "__main__":
    main()
