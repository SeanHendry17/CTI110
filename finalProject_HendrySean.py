#Sean Hendry
#12/11/2025
#Final Projecttt
#A jet-battle game that lets the user create jets, view their stats, and make them attack each other

import random

def create_jet():
    """Creates a new jet with user input."""
    name = input("Enter jet's name: ")

    while True:
        try:
            fuel = int(input(f"Enter {name}'s fuel: "))
            break
        except ValueError:
            print("Fuel must be a NUMBER.")

    while True:
        try:
            damage = int(input(f"Enter {name}'s damage: "))
            break
        except ValueError:
            print("Damage must be a NUMBER.")

    jet = {'name': name, 'fuel': fuel, 'damage': damage}
    print(f"{name} has been created ✈️")
    return jet


def display_jets(jets):
    """Displays all jets."""
    print("\n✈️ --- ALL JETS --- ✈️")
    if len(jets) == 0:
        print("No jets created yet.")
    else:
        for i, jet in enumerate(jets):
            print(f"[{i}] Name: {jet['name']}, Fuel: {jet['fuel']}, Damage: {jet['damage']}")
    print()


def attack(attacker, defender):
    """Performs attack and returns defender's new fuel."""
    damage = random.randint(0, attacker['damage'])
    defender['fuel'] = max(0, defender['fuel'] - damage)  

    print(f"\n{attacker['name']} attacks {defender['name']}! ✈️")
    print(f"Damage dealt: {damage}")
    return defender['fuel']


def safe_index_input(prompt, jets):
    """Ensures user picks a valid jet index."""
    while True:
        try:
            idx = int(input(prompt))
            if 0 <= idx < len(jets):
                return idx
            else:
                print("Index out of range.")
        except ValueError:
            print("Please enter a NUMBER.")


def main():
    """Main game loop."""
    jets = []
    running = True

    while running:
        print("\n====== JET GAME MENU ======")
        print("1. Create a Jet")
        print("2. Display All Jets")
        print("3. Attack")
        print("4. Exit Game")
        print("============================")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            jets.append(create_jet())

        elif choice == "2":
            display_jets(jets)

        elif choice == "3":
            if len(jets) < 2:
                print("You need at least TWO jets to attack!")
            else:
                display_jets(jets)

                attacker_index = safe_index_input("Choose attacker jet index: ", jets)
                defender_index = safe_index_input("Choose defender jet index: ", jets)

                if attacker_index == defender_index:
                    print("A jet cannot attack itself!")
                else:
                    attacker = jets[attacker_index]
                    defender = jets[defender_index]

                    new_fuel = attack(attacker, defender)

                    if new_fuel <= 0:
                        print(f"{defender['name']} has been destroyed! 💥")

        elif choice == "4":
            print("Exiting game... Goodbye! 👋")
            running = False

        else:
            print("Invalid choice. Please choose 1-4.")


if __name__ == "__main__":
    main()