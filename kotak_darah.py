class Bar:
    def __init__(self, entity, length: int = 20, colored: bool = True, color: str = "") -> None:
        self.entity = entity
        self.length = length
        self.full_value = entity.max_health if self.__class__.__name__ == "HealthBar" else entity.max_mana
        self.current_value = entity.health if self.__class__.__name__ == "HealthBar" else entity.mana
        self.colored = colored
        self.color = HealthBar.colors.get(color, HealthBar.colors["default"])

    def update(self) -> None:
        self.current_value = self.entity.health if self.__class__.__name__ == "HealthBar" else self.entity.mana

    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.full_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name} {'Health' if self.__class__.__name__ == 'HealthBar' else 'Mana'}: {self.current_value}/{self.full_value}")
        print(f"{HealthBar.wall}"
              f"{self.color if self.colored else ''}"
              f"{HealthBar.waiting_symbol * remaining_bars}"
              f"{HealthBar.lost_symbol * lost_bars}"
              f"{HealthBar.colors['default'] if self.colored else ''}"
              f"{HealthBar.wall}")

class HealthBar(Bar):
    colors = {"red": "\033[91m", "purple": "\033[95m", "blue": "\033[94m", "green": "\033[92m", "default": "\033[0m"}
    waiting_symbol: str = "█"
    lost_symbol: str = "_"
    wall: str = "|"
    
class ManaBar(Bar):
    pass
