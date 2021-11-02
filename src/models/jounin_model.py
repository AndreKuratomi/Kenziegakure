from src.models.ninja_model import Ninja


class Jounin(Ninja):

    ninja_level = "Jounin"

    def __init__(self, name: str, clan: str, village: str, proficiency: dict, in_this_mission: bool = False) -> None:

        super().__init__(name, clan, village, ninja_level=self.ninja_level)
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
            return f'O ninja {self.name} {self.clan} saiu em missão'

        return f'O ninja {self.name} {self.clan} já está em uma missão'

    def return_from_mission(self):
        if self.is_in_mission is True:
            self.is_in_mission = False
            return f'O ninja {self.name} {self.clan} retornou em segurança da missão'
            
        return f'O ninja {self.name} {self.clan} não está em nenhuma missão no momento'

