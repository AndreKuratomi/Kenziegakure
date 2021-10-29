class Jutsu():
    jutsu_ranks = ("D", "C", "B", "A", "S", )

    def __init__(self, jutsu_name: str, jutsu_type: str, jutsu_level: str, jutsu_damage: int, chakra_spend: int) -> None:
        self.jutsu_name = jutsu_name
        self.jutsu_type = jutsu_type
        self.jutsu_level = jutsu_level.upper()
        if self.jutsu_level not in self.jutsu_ranks:
            self.jutsu_level = "Unranked"
        self.jutsu_damage = jutsu_damage
        self.chakra_spend = chakra_spend
        if self.chakra_spend <= 0:
            self.chakra_spend = 100
        else:
            self.chakra_spend = chakra_spend


rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)
naruto = Jutsu('Naruto', 'Terra', 'z', 20, 0)
alguem = Jutsu('Alguem', 'Terra', 'm', 20, 10)
print(rasengan.__dict__)
print(naruto.__dict__)
print(alguem.__dict__)
