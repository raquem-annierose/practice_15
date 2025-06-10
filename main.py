import os
from colorama import init, Fore, Style, Back
from polytech import raquem

init(autoreset=True)

EXIT_OPTION = 6
UNSET_OPTION = -1
DISPLAY_WIDTH = 28
MENU_TITLE = "PolyTech Menu System"
MIN_OPTION = 1
MAX_OPTION = 5

MENU_OPTIONS = {
    1: "Annie Rose S. Raquem",
    2: "Option 2",
    3: "Option 3",
    4: "Option 4",
    5: "Option 5",
    6: "Exit"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def center_text(text, width):
    if len(text) >= width:
        return text[:width]
    
    left_padding = (width - len(text)) // 2
    right_padding = width - len(text) - left_padding
    
    return ' ' * left_padding + text + ' ' * right_padding

def display_header():
    print(Back.YELLOW + " " * DISPLAY_WIDTH)
    centered_title = center_text(MENU_TITLE, DISPLAY_WIDTH - 2)
    print(
        Back.YELLOW + " " + Back.RESET +
        Fore.YELLOW + Style.BRIGHT + centered_title +
        Back.YELLOW + " " + Back.RESET
    )
    print(Fore.YELLOW + "=" * DISPLAY_WIDTH)
    print(Back.YELLOW + " " * DISPLAY_WIDTH)

def display_menu():
    display_header()
    
    for key in sorted(MENU_OPTIONS):
        menu_text = f"{key}. {MENU_OPTIONS[key]}"
        centered_text = center_text(menu_text, DISPLAY_WIDTH)

        if key == EXIT_OPTION:
            print(Fore.RED + centered_text + Style.RESET_ALL)
        else:
            number_part = f"{key}. "
            menu_item = MENU_OPTIONS[key]
            centered = center_text(f"{number_part}{menu_item}", DISPLAY_WIDTH)
            start = centered.find(number_part)
            end = start + len(number_part)
            print(
                centered[:start] +
                Fore.YELLOW + centered[start:end] +
                Style.RESET_ALL + centered[end:]
            )

    print(Fore.YELLOW + Style.BRIGHT + "=" * DISPLAY_WIDTH)

def get_user_choice():
    try:
        return int(input(Style.BRIGHT + "Enter choice: " + Style.RESET_ALL))
    except ValueError:
        return UNSET_OPTION

def exit_program():
    print(
        Back.RED + Fore.YELLOW + " EXITING PROGRAM " +
        Back.RESET + Fore.YELLOW + " Thank you for using the system."
    )

def handle_invalid_choice():
    print(
        Back.YELLOW + Fore.BLACK + " INVALID CHOICE " +
        Back.RESET + Fore.YELLOW +
        " Please select a valid option from the menu."
    )

def display_get_choice(choice):
    if MIN_OPTION <= choice <= MAX_OPTION:
        clear_screen()
    
    match choice:
        case 1:
            raquem.Pet.menu()  # Call the class method directly
        case 2:
            # TODO(Victorio) Put your module here.
            pass
        case 3:
            # TODO(Niones) Put your module here.
            pass
        case 4:
            # TODO(Capilitan) Put your module here.
            pass
        case 5:
            # TODO(Villarta) Put your module here.
            pass
        case _:
            handle_invalid_choice()

def main():
    while True:
        clear_screen()
        display_menu()
        choice = get_user_choice()
        
        if choice == EXIT_OPTION:
            exit_program()
            break
            
        if choice < MIN_OPTION or choice > MAX_OPTION:
            handle_invalid_choice()
            input(Fore.YELLOW + Style.BRIGHT + "Press Enter to continue...")
            continue
            
        display_get_choice(choice)
        input(Fore.YELLOW + Style.BRIGHT + "Press Enter to continue...")

main()