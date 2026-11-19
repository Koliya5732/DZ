from dataclasses import dataclass


@dataclass
class Skeleton:
    name: str
    weapon: str
    mood: str
    year: int

    def attack(self):
        print(f"{self.name} атакует противника своим оружием: {self.weapon}!")

    def defend(self):
        print(f"{self.name} поднимает щит и готовится защищаться!")

    def rage(self):
        print(f"{self.name} начинает бить мечом по своему щиту! Похоже, он в ярости!")

    def speak(self):
        print(f"{self.name}: КЛАЦ-КЛАЦ... Я не злой, просто у меня нет нервов!")


def main():
    kostya = Skeleton(
        name="Костя",
        weapon="Меч и щит",
        mood="Неизвестное, предположительно ярость",
        year=2026
    )

    boris = Skeleton(
        name="Борис",
        weapon="Ржавый топор",
        mood="Спокойное",
        year=1998
    )

    kostya.attack()
    kostya.defend()
    kostya.rage()
    kostya.speak()

    print("\n--- Второй скелет ---")

    boris.attack()
    boris.defend()
    boris.rage()
    boris.speak()


if __name__ == "__main__":
    main()

