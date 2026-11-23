# opening game menu
def main_menu_loop(player_options):
    match player_options:
        case "start":
            print("The forgotten hero slowly comes to....")
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
        case "exit":
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

    while game_running:
        player_options = input("Choose your option: ").strip().lower()
        game_running = main_menu_loop(player_options)


if __name__ == "__main__":
    main()
