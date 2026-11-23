def show_actions_menu(): # actions menu
    print("Choose your next action: ")
    print("'Look': See what's around the room")
    print("'Go': If possible move to the next room")  # if not possible should give hint to requirements
    print("'Status': Show current health and items")
    print("'Help': See the options again")
    print("'Menu': Pull up the main menu")


# a "playing" game state
def play_game():
    playing = True
    show_actions_menu()
    while playing: # TODO finish the in game menu
        action_choice = input("What will you do? ").strip().lower()
        match action_choice:
            case "look":
                print("Look around the room") # TODO create more information in the 'room' class
            case "go":
                print("Finding your way to the next room...") # TODO requirements for moving on to the next room
            case "status":
                print("This is where that inventory status page would go.... if i had one") # TODO make this status page
            case "help":
                show_actions_menu()
            case "menu":
                show_menu()
                playing = False
            case _:
                print("Invalid option")


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
