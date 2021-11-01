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
        return f"O ninja {self.name} {self.clan} acabou de aprender um novo jutsu: {self.village.capitalize()}"

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
        # elif adversary.health_pool >= 100 and self.chakra_pool >= 100:
        return False


naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')
print(naruto.__dict__)

rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)
alguem = Jutsu('Alguem', 'Terra', 'm', 20, 10)

naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')
oturan = Ninja('Naruto', 'Uzumaki', 'donoha')

ser = oturan.learn_jutsu(rasengan)
res = naruto.learn_jutsu(alguem)
naruto.health_pool = 100
ers = Ninja.check_health(naruto)
print(ser)
print(res)
print(ers)

# > 'O ninja Naruto Uzumaki acabou de aprender um novo jutsu: Rasengan'

rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)
naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')

naruto.learn_jutsu(rasengan)

sasuke = Ninja('Sasuke', 'Uchiha', 'Konoha')

res = naruto.cast_jutsu(rasengan, sasuke)
print(res)
