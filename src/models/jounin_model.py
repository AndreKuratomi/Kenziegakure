from src.models.ninja_model import Ninja


class Jounin(Ninja):
    #?
    super().__init__(ninja_level)
    ninja_level = "Jounin"

    def __init__(self, name: str, clan: str, village: str, proficiency: dict = {'taijutsu': int, 'ninjutsu': int, 'genjutsu': int}, in_this_mission: bool = False):
        super().__init__(name, clan, village)
        self.proficiency = proficiency
        self.is_in_mission = in_this_mission

    def list_best_proficiency(self):
        prof = self.proficiency
        maior = prof["taijutsu"]

        for habilidade in prof:
            if prof[habilidade] > maior:
                maior = prof[habilidade]
        for qual in prof:
            if prof[qual] == maior:
                maior = qual

        return f'{self.name} demonstra maior proficiência em {maior}'

    def start_mission(self):
        if self.is_in_mission is False:
            self.is_in_mission = True
            return f'O ninja {self.name} {self.clan} já está em uma missão'
        return f'O ninja {self.name} {self.clan} saiu em missão'

    def return_from_mission(self):
        if self.is_in_mission is True:
            self.is_in_mission = False
            return f'O ninja {self.name} {self.clan} não está em nenhuma missão no momento'
        return f'O ninja {self.name} {self.clan} retornou em segurança da missão'


# Atributo de classe:
# ninja_level : Uma string que recebe o valor "Jounin".

kakashi_proficiency = {'taijutsu': 7, 'ninjutsu': 8, 'genjutsu': 4}
kakashi = Jounin('Kakashi', 'Hatake', 'Konoha', kakashi_proficiency)
print(kakashi.__dict__)

res0 = kakashi.list_best_proficiency()
print(res0)

res1 = kakashi.start_mission()
print(res1)

res2 = kakashi.start_mission()
print(res2)

res3 = kakashi.return_from_mission()
print(res3)

res4 = kakashi.return_from_mission()
print(res4)   
