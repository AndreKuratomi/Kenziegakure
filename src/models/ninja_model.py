from src.models.jutsu_model import Jutsu


class Ninja:

    def __init__(self, name: str, clan: str, village: str, ninja_level: str = "Unranked", health_pool: int = 100, chakra_pool: int = 100, concious: bool = True) -> None:
        self.name = name
        self.clan = clan
        self.village = village
        self.ninja_level = ninja_level
        self.jutsu_list = []
        self.health_pool = health_pool
        self.chakra_pool = chakra_pool
        self.concious = concious

    def learn_jutsu(self, jutsu):
        self.jutsu_list.append(jutsu)

        return f"O ninja {self.name} {self.clan} acabou de aprender um novo jutsu: {jutsu.jutsu_name.capitalize()}"

    @staticmethod
    def check_health(ninja_to_check):
        if ninja_to_check.health_pool < 0:
            ninja_to_check.health_pool = 0
            ninja_to_check.concious = False

        return ninja_to_check.concious

    def cast_jutsu(self, jutsu, adversary):
        if adversary.concious is not True:
            return False

        if jutsu in self.jutsu_list and self.chakra_pool >= 100:
            adversary.health_pool -= jutsu.jutsu_damage
            self.chakra_pool -= jutsu.chakra_spend
            return True
        return False

