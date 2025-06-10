import os
from colorama import init, Fore, Style, Back

init(autoreset=True)

EXIT_OPTION = 0
class Pet:
    SPECIES_AVAILABILITY = {
        "Dog": 5,
        "Cat": 3,
        "Bird": 2,
        "Fish": 4
    }
    
    def __init__(self, name="", species="", age=0):
        self.name = name
        self.species = species
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.strip().title() if value else ""

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        self._species = value.strip().title() if value else ""

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = max(0, int(value))

    def display_species_availability(self):
        print(Fore.YELLOW + "====== Species Availability ======" + Fore.RESET)

        for number, (species, count) in enumerate(
            self.SPECIES_AVAILABILITY.items(), start=1
        ):
            print(f"{number}. {species}: {count} available")

    def choose_species(self):
        self.display_species_availability()

        try:
            choice = int(
                input(
                    Fore.YELLOW +
                    "Select a species by number: " +
                    Fore.RESET
                )
            )
        except ValueError:
            print(
                Fore.RED +
                "Invalid input. Please enter a number." +
                Fore.RESET
            )
            return

        species_list = list(self.SPECIES_AVAILABILITY.keys())

        if choice < 1 or choice > len(species_list):
            print(
                Fore.RED +
                "Invalid selection. Please try again." +
                Fore.RESET
            )
            return

        selected_species = species_list[choice - 1]
        available_count = self.SPECIES_AVAILABILITY[selected_species]

        if available_count <= 0:
            print(
                Fore.RED +
                f"Sorry, {selected_species} is out of stock." +
                Fore.RESET
            )
            return

        self.species = selected_species
        self.SPECIES_AVAILABILITY[selected_species] -= 1
        print(
            Fore.GREEN +
            f"{self.species} selected! Remaining: "
            f"{self.SPECIES_AVAILABILITY[self.species]}"
            + Fore.RESET
        )

    def set_name(self):
        self.name = input(
            Fore.YELLOW + f"Enter your {self.species}'s name: " + Fore.RESET
        )
        print(Fore.GREEN + f"Name set to {self.name}." + Fore.RESET)

    def set_age(self):
        try:
            new_age = int(
                input(Fore.YELLOW + "Enter your pet's age: " + Fore.RESET)
            )
            self.age = new_age
            print(Fore.GREEN + f"Age set to {self.age}." + Fore.RESET)
        except ValueError:
            print(
                Fore.RED +
                "Invalid input. Please enter a number."
                + Fore.RESET
            )

    def display_details(self):
        print(Fore.YELLOW + "====== Pet Details ======" + Fore.RESET)
        print(f"Name         : {self.name}")
        print(f"Species      : {self.species}")
        print(f"Age          : {self.age}")

    def play_with_pet(self):
        if not self.name or not self.species:
            print(Fore.RED + "You need to create a pet first!" + Fore.RESET)
            return

        print(Fore.YELLOW + f"=== Playing with {self.name} ===" + Fore.RESET)
        play_options = {
            "Dog": ["fetch", "tug-of-war", "hide and seek"],
            "Cat": ["laser pointer", "feather toy", "catnip mouse"],
            "Bird": ["mirror play", "swing", "puzzle toys"],
            "Fish": ["follow your finger", "decorations", "bubbles"]
        }

        activities = play_options.get(self.species)
        if not activities:
            print(
                Fore.RED +
                f"No play activities for {self.species} yet." +
                Fore.RESET
            )
            return

        print(f"Choose an activity to do with {self.name}:")
        for idx, activity in enumerate(activities, 1):
            print(f"{idx}. {activity}")

        try:
            choice = int(
                input(Fore.YELLOW + "Select activity: " + Fore.RESET)
            )
        except ValueError:
            print(Fore.RED + "Please enter a number." + Fore.RESET)
            return

        if 1 <= choice <= len(activities):
            selected = activities[choice - 1]
            print(
                Fore.GREEN +
                f"You played {selected} with {self.name}!" +
                Fore.RESET
            )
            print(f"{self.name} looks happy!")
        else:
            print(Fore.RED + "Invalid selection." + Fore.RESET)

    def display_menu(self):
        print(Fore.YELLOW + "\n===== Pet Menu =====" + Fore.RESET)
        print("1. Choose Species")
        print("2. Set Name")
        print("3. Set Age")
        print("4. Display Pet Details")
        print("5. Play with Pet")
        print("0. Exit to Main Menu")

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @classmethod
    def menu(cls):
        pet = cls()
        
        choice = -1
        while choice != EXIT_OPTION:
            pet.clear_screen() 
            pet.display_menu()
            try:
                choice = int(
                    input(Fore.YELLOW + "Enter your choice: " + Fore.RESET)
                )
                pet.clear_screen()  
                match choice:
                    case 1:
                        pet.choose_species()
                    case 2:
                        pet.set_name()
                    case 3:
                        pet.set_age()
                    case 4:
                        pet.display_details()
                    case 5:
                        pet.play_with_pet()
                    case 0:
                        print(
                            Fore.GREEN +
                            "Returning to main menu..."
                            + Fore.RESET
                        )
                        continue
                    case _:
                        print(
                            Fore.RED +
                            "Invalid choice. Please try again."
                            + Fore.RESET
                        )
                input(
                    Fore.YELLOW +
                    "Press Enter to continue..." +
                    Fore.RESET
                )
               
            except ValueError:
                pet.clear_screen() 
                print(
                    Fore.RED +
                    "Invalid input. Please enter a number."
                    + Fore.RESET
                )
                input(
                    Fore.YELLOW +
                    "Press Enter to continue..." +
                    Fore.RESET
                )