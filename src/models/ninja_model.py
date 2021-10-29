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
        return f"O ninja {self.name} {self.clan} acabou de aprender um novo jutsu: {self.village.capitalize()}"


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

# > 'O ninja Naruto Uzumaki acabou de aprender um novo jutsu: Rasengan'
