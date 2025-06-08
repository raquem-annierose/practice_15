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
    
    def __init__(self, name="", species="", age=0, favorite_toy=""):
        self.name = name
        self.species = species
        self.age = age
        self.favorite_toy = favorite_toy

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

    @property
    def favorite_toy(self):
        return self._favorite_toy

    @favorite_toy.setter
    def favorite_toy(self, value):
        self._favorite_toy = value.strip().title() if value else ""

    def display_species_availability(self):
        print(Fore.YELLOW + "====== Species Availability ======" + Fore.RESET)
        for species, count in self.SPECIES_AVAILABILITY.items():
            print(f"{species}: {count} available")

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

            species_list = list(self.SPECIES_AVAILABILITY.keys())

            if 1 <= choice <= len(species_list):
                selected_species = species_list[choice - 1]
                if self.SPECIES_AVAILABILITY[selected_species] > 0:
                    self.species = selected_species
                    self.SPECIES_AVAILABILITY[selected_species] -= 1
                    print(
                        Fore.GREEN +
                        f"{self.species} selected! Remaining: "
                        f"{self.SPECIES_AVAILABILITY[self.species]}"
                        + Fore.RESET
                    )
                else:
                    print(
                        Fore.RED +
                        f"Sorry, {selected_species} is out of stock."
                        + Fore.RESET
                    )
            else:
                print(
                    Fore.RED +
                    "Invalid selection. Please try again."
                    + Fore.RESET
                )

        except ValueError:
            print(
                Fore.RED +
                "Invalid input. Please enter a number."
                + Fore.RESET
            )

    def set_name(self):
        """Prompt user to set the pet's name."""
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

    def set_favorite_toy(self):
        self.favorite_toy = input(
            Fore.YELLOW + "Enter your pet's favorite toy: " + Fore.RESET
        )
        print(
            Fore.GREEN +
            f"Favorite toy set to {self.favorite_toy}."
            + Fore.RESET
        )

    def display_details(self):
        print(Fore.YELLOW + "====== Pet Details ======" + Fore.RESET)
        print(f"Name         : {self.name}")
        print(f"Species      : {self.species}")
        print(f"Age          : {self.age}")
        print(f"Favorite Toy : {self.favorite_toy}")

        if self.species:
            print(
                Fore.YELLOW +
                "\n====== Species-Specific Info ======"
                + Fore.RESET
            )
            if self.species == "Dog":
                print("Dogs are loyal companions that need regular walks")
                print(
                    "Recommended vaccinations: "
                    "Rabies, Distemper, Parvovirus"
                )
                print("Lifespan: 10-13 years")
            elif self.species == "Cat":
                print(
                    "Cats are independent pets that enjoy climbing "
                    "and exploring"
                )
                print("Recommended vaccinations: Rabies, FVRCP")
                print("Lifespan: 12-15 years")
            elif self.species == "Bird":
                print(
                    "Birds need spacious cages and social interaction"
                )
                print("Diet: Seeds, fruits, and vegetables")
                print("Lifespan varies greatly by species")
            elif self.species == "Fish":
                print(
                    "Fish need clean water and proper temperature control"
                )
                print("Regular tank maintenance is essential")
                print("Lifespan varies by species")

    def display_menu(self):
        print(Fore.YELLOW + "\n===== Pet Menu =====" + Fore.RESET)
        print("1. Choose Species")
        print("2. Set Name")
        print("3. Set Age")
        print("4. Set Favorite Toy")
        print("5. Display Pet Details")
        print("0. Exit to Main Menu")

    @classmethod
    def menu(cls):
        pet_instance = cls()
        
        choice = -1
        while choice != EXIT_OPTION:
            pet_instance.display_menu()
            try:
                choice = int(
                    input(Fore.YELLOW + "Enter your choice: " + Fore.RESET)
                )
                os.system('cls' if os.name == 'nt' else 'clear')
                match choice:
                    case 1:
                        pet_instance.choose_species()
                    case 2:
                        pet_instance.set_name()
                    case 3:
                        pet_instance.set_age()
                    case 4:
                        pet_instance.set_favorite_toy()
                    case 5:
                        pet_instance.display_details()
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
                os.system('cls' if os.name == 'nt' else 'clear')
            except ValueError:
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