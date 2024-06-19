import os
import random
from character import Adventurer, Dragon
from senjata import FireBreath, Dagger, Spear, Katana, Lightning, FireBall, Light

def game_over_message():
    message = "🎉Congratulations!🎉\nYou have cleared the dungeon!!"
    width = 40  # Adjust the width as needed

    print("\n" + "=" * width)
    for line in message.splitlines():
        print(line.center(width))
    print("=" * width)

def choose_weapon():
    weapons = [Dagger, Spear, Katana]
    while True:
        print("Choose your weapon:")
        for i, weapon in enumerate(weapons, 1):
            print(f"{i}. {weapon.name} (Type: {weapon.weapon_type}, Damage: {weapon.damage}, Durability: {weapon.durability})")
        
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(weapons):
                return weapons[choice - 1]
            else:
                print("Invalid choice. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_magic():
    magic_spells = [Lightning, FireBall, Light]
    while True:
        print("Choose your magic spell:")
        for i, spell in enumerate(magic_spells, 1):
            print(f"{i}. {spell.name} (Type: {spell.weapon_type}, Damage: {spell.damage}, Mana Cost: {spell.mana_cost})")

        try:
            print("=================================================")
            choice = int(input("Enter the number of your choice: "))
            print("=================================================")
            if 1 <= choice <= len(magic_spells):
                return magic_spells[choice - 1]
            else:
                print("Invalid choice. Please choose a valid number.")
                print("=================================================")
        except ValueError:
            print("=================================================")
            print("Invalid input. Please enter a number.")
            print("=================================================")

def battle(adventurer, enemy):
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        # adventurer's turn
        print(f"{adventurer.name} turn:")
        adventurer.health_bar.draw()
        adventurer.mana_bar.draw()
        print("=================================================")
        attack_type = input("Choose your attack type: 1. Melee 2. Magic: ")
        if attack_type == '2':
            print("=================================================")
            magic_spell = choose_magic()
            adventurer.use_weapon(magic_spell)
        else:
            print("=================================================")
            adventurer.use_weapon(adventurer.melee_weapon)

        adventurer.attack(enemy)
        if enemy.health == 0:
            print("=================================================")
            print(f"\n{enemy.name} has been defeated!")
            print("\n=================================================")
            break

        # Regenerate mana for adventurer
        adventurer.regenerate_mana()

        # Enemy's turn
        print("_________________________________________________")
        print(f"\n{enemy.name}'s turn:")
        enemy.attack(adventurer)
        if adventurer.health == 0:
            print("=================================================")
            print(f"\n💀{adventurer.name} has been defeated!💀")
            print("\n=================================================")
            while True:
                choice = input("\nType 'y' to play again or 'n' to quit: ").lower()
                if choice == 'y':
                    input("\nGood luck")
                    os.system("cls" if os.name == "nt" else "clear")
                    game()
                    return
                elif choice == 'n':
                    print("\n=================================================")
                    print("\nU died shamelessly to some winged reptile on the dungeon!")
                    print("\n=================================================")
                    return
                else:
                    print("Invalid input. Please type 'y' or 'n'.")
            return False

        # Regenerate mana for enemy
        enemy.regenerate_mana()

        print("=================================================")

        # Update health and mana bars
        adventurer.health_bar.draw()
        adventurer.mana_bar.draw()
        enemy.health_bar.draw()
        enemy.mana_bar.draw()

        print("=================================================")

        # Check for exit
        choice = input("Press Enter to continue or type 'exit' to quit: ")
        if choice.lower() == 'exit':
            print("=================================================")
            print("Fleeing the dungeon. puny adventurer!")
            print("=================================================")
            return False
    return True

def game():
    adventurer_name = input("Enter the name of your character: ")
    adventurer = Adventurer(name=adventurer_name, health=300, mana=100)

    # Story
    os.system("cls" if os.name == "nt" else "clear")
    print("============================================================================================================")
    print("You have been reincarnated in a foreign land, where swords and magic exist,")
    print("but the strange thing is that you don't remember how you got there or where you came from.")
    print(f"All you remember is just your name, {adventurer_name}...")

    print("You decide to go to the nearest town and find an adventure guild to help you figure everything out.")
    print("After registering as an adventurer and given a basic sword,")
    print("you decide to explore a nearby dungeon, hoping to gain some popularity and answers.")

    print("However, as you approach the dungeon entrance, you are ambushed by bandits and nearly lose your life.")
    print("You manage to enter the dungeon, but not without sustaining major injuries from the bandit attack.")
    print("As you desperately contemplate how to survive, a mysterious notification sound suddenly echoes around you...")

    #Enhanced notification moment
    print("\n\033[1m!!CONGRATULATIONS, YOU HAVE BEEN CHOSEN AS A PLAYER!!\033[0m")
    print("A mystical system appears before your eyes and offers you the ability to wield both sword and magic.")
    print("Determined to uncover the truth, you cautiously proceed deeper into the dungeon.")
    print("============================================================================================================")

    input("Press Enter to continue...")

    adventurer.melee_weapon = choose_weapon()
    adventurer.use_weapon(adventurer.melee_weapon)

    enemies = [
        Dragon(name="Dragon", health=300, mana=50),
        Dragon(name="Ancient Dragon", health=450, mana=100)
    ]

    for i, enemy in enumerate(enemies):
        print(f"Stage {i + 1}: Fight against {enemy.name}")
        if not battle(adventurer, enemy):
            return

        if i < len(enemies) - 1:
            # Regenerate adventurer's health by 80% of current health
            adventurer.health = min(int(adventurer.health * 1.8), adventurer.max_health)
            adventurer.health_bar.update()
            print(f"\n{adventurer.name} has regenerated health to {adventurer.health}/{adventurer.max_health}")
            print("\n=================================================")

            while True:
                choice = input("\nDo you want to advance to the next stage? (y/n): ").lower()
                if choice == 'y':
                    break
                elif choice == 'n':
                    print("Exiting the dungen. weakling!")
                    return
                else:
                    print("Invalid input. Please type 'y' or 'n'.")

    game_over_message()

    while True:
        choice = input("\nType 'y' to play again or 'n' to quit: ").lower()
        if choice == 'y':
            os.system("cls" if os.name == "nt" else "clear")
            game()
            return
        elif choice == 'n':
            print("Exiting the dungeon. Goodluck!")
            return
        else:
            print("Invalid input. Please type 'y' or 'n'.")

if __name__ == "__main__":
    game()
