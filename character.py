from senjata import Hands, Claws, FireBreath, Lightning
from kotak_darah import HealthBar, ManaBar
import random

class Character:
    def __init__(self, name: str, health: int, mana: int) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.mana = mana
        self.max_mana = mana
        self.weapon = Hands
        self.health_bar = HealthBar(self, color="green")
        self.mana_bar = ManaBar(self, color="blue")

    def attack(self, target) -> None:
        if self.weapon.weapon_type == "Magic" and self.mana < self.weapon.mana_cost:
            print(f"Not enough mana to use {self.weapon.name}")
            return
        
        if self.weapon.weapon_type == "Magic":
            self.mana -= self.weapon.mana_cost

        self.weapon.use()
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        self.health_bar.update()
        self.mana_bar.update()
        print(f"{self.name} deals {self.weapon.damage} damage to {target.name} with {self.weapon.name}")

    def use_weapon(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} is using {self.weapon.name}!")

    def regenerate_mana(self) -> None:
        regen_amount = int(self.max_mana * 0.1)
        self.mana = min(self.mana + regen_amount, self.max_mana)
        self.mana_bar.update()
        print(f"{self.name} regenerates {regen_amount} mana.")

class Adventurer(Character):
    def __init__(self, name: str, health: int, mana: int) -> None:
        super().__init__(name, health, mana)

class Dragon(Character):
    def __init__(self, name: str, health: int, mana: int) -> None:
        super().__init__(name, health, mana)
        self.weapons = [Claws, FireBreath]
        self.weapon = self.weapons[0]
        self.health_bar = HealthBar(self, color="red")
        self.mana_bar = ManaBar(self, color="blue")

    def attack(self, target) -> None:
        self.weapon = random.choice(self.weapons)
        super().attack(target)
