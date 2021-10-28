# Cole seu código aqui
class Jutsu():
# jutsu_ranks : Uma tupla de strings que recebe os possiveis ranks de um jutsu ("D", "C", "B", "A", "S",).
    jutsu_ranks = ("D", "C", "B", "A", "S", )

    def __init__(self, jutsu_name: str, jutsu_type: str, jutsu_level: str, jutsu_damage: int, chakra_spend: int):
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




# Etapa 1
# Defina as seguinte classes, observando a chamada das instâncias (quando houver) de exemplo para interpretar 
# quais atributos fazem parte do construtor e quais são diretamente inicializados pela classe.

# Classe Jutsu

# jutsu_level : Uma string que recebe o level do jutsu, se o level passado 
# não estiver compreendido em jutsu_ranks, deverá então receber "Unranked". 
# Por padrão, deverão ser consideradas tanto letras maiúsculas como 
# minúsculas na comparação;

# Dica!
# A letra "Z" não entra no grupo jutsu_ranks, logo o atributo seria inicializado 
# como "Unranked";
# A letra "a" entra no grupo jutsu_ranks, mesmo sendo minúscula, mas a inicialização 
# do atributo seria com a versão maiúscula "A".

# chakra_spend : Um inteiro positivo que recebe a quantidade de chakra gasta 
# pelo jutsu. Se o inteiro passado for negativo ou zero, inicializar o atributo 
# com o valor 100.

# Exemplo de criação de uma instância da classe Jutsu :
# > {
#      'jutsu_name': 'Rasengan',
#      'jutsu_type': 'Vento',
#      'jutsu_level': 'A',
#      'jutsu_damage': 20,
#      'chakra_spend': 100
#   }

# Dica!
# Utilize o magic method __dict__ para printar todos os atributos da instância e verificar se tudo foi criado 
# corretamente. Isso o ajudará na realização dos testes iniciais.