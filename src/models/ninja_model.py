from jutsu_model import Jutsu


class Ninja:

    def __init__(self, name: str, clan: str, village: str, ninja_level: str = "Unranked", jutsu_list: list = [], health_pool: int = 100, chakra_pool: int = 100, concious: bool = True) -> None:
        self.name = name
        self.clan = clan
        self.village = village
        self.ninja_level = ninja_level
        self.jutsu_list = jutsu_list
        self.health_pool = health_pool
        self.chakra_pool = chakra_pool
        self.concious = concious

    def learn_jutsu(self, jutsu):
        self.jutsu_list.append(jutsu)
        return f"O ninja {self.name} {self.clan} acabou de aprender um novo jutsu: {self.village}"

    @staticmethod
    def check_health(ninja_to_check):
        if ninja_to_check.health_pool < 0:
            ninja_to_check.health_pool = 0
            ninja_to_check.concious = False
        return ninja_to_check.concious

    def cast_jutsu(self, jutsu, adversary):
        if adversary.concious is False:
            return False
        if jutsu in self.jutsu_list and self.chakra_pool >= 0:
            adversary.health_pool = jutsu.jutsu_damage
            self.chakra_pool -= jutsu.chakra_spend
            return True


naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')
print(naruto.__dict__)

rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)
alguem = Jutsu('Alguem', 'Terra', 'm', 20, 10)

naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')
oturan = Ninja('Naruto', 'Uzumaki', 'donoha')

ser = oturan.learn_jutsu(alguem)
res = naruto.learn_jutsu(rasengan)
print(ser)
print(res)

rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)
naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')

naruto.learn_jutsu(rasengan)

sasuke = Ninja('Sasuke', 'Uchiha', 'Konoha')

res5 = naruto.cast_jutsu(rasengan, sasuke)
print(res5)
