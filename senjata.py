class Weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, durability: int, value: int, mana_cost: int = 0) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.durability = durability
        self.initial_damage = damage  # Store the initial damage for reference
        self.value = value
        self.mana_cost = mana_cost

    def use(self):
        self.durability -= 1
        if self.durability <= 0:
            self.damage = self.initial_damage // 2
            self.name = f"Broken {self.name.split()[-1]}"  # Rename to "Broken [weapon name]"

# Adjusted durability values for melee weapons
Dagger = Weapon(name="Dagger", weapon_type="Sharp", damage=25, durability=200, value=1)
Spear = Weapon(name="Spear", weapon_type="Sharp", damage=38, durability=150, value=1)
Katana = Weapon(name="Katana", weapon_type="Sharp", damage=45, durability=180, value=1)
Hands = Weapon(name="Hands", weapon_type="Blunt", damage=8, durability=float('inf'), value=1)
Lightning = Weapon(name="Lightning", weapon_type="Magic", damage=35, durability=float('inf'), value=1, mana_cost=20)
FireBall = Weapon(name="Dragon's breath", weapon_type="Magic", damage=20, durability=float('inf'), value=1, mana_cost=10)
Light = Weapon(name="Holy Light", weapon_type="Magic", damage=50, durability=float('inf'), value=1, mana_cost=30)
FireBreath = Weapon(name="Fire Breath", weapon_type="Magic", damage=40, durability=float('inf'), value=1, mana_cost=25)
Claws = Weapon(name="Claws", weapon_type="Sharp", damage=15, durability=float('inf'), value=1)
