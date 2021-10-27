from ..helpers.jutsu_attributes import rasengan, chidori
from pytest import fail
from src.models.jutsu_model import Jutsu


def test_jutsu_class_attribute(cria_jutsu_rasengan):
    try:
        result = Jutsu.jutsu_ranks
    except AttributeError:
        fail('Verifique se o atributo de classe jutsu_ranks foi criado corretamente')

    expected = ('D', 'C', 'B', 'A', 'S',)

    assert result == expected, 'Verifique se o atributo de classe ' + \
        'jutsu_ranks foi criado corretamente'


def test_jutsu_attributes_rasengan(cria_jutsu_rasengan):
    assert cria_jutsu_rasengan.jutsu_name == rasengan['jutsu_name'], \
        f'Verifique se o atributo jutsu_name da classe Jutsu' + \
        f' está sendo criado corretamente.'

    assert cria_jutsu_rasengan.jutsu_type == rasengan['jutsu_type'], \
        f'Verifique se o atributo jutsu_type da classe Jutsu' + \
        f' está sendo criado corretamente.'

    assert cria_jutsu_rasengan.jutsu_level == 'A', \
        f'Verifique se o atributo jutsu_level da classe Jutsu' + \
        f' está sendo criado corretamente.'

    assert cria_jutsu_rasengan.jutsu_damage == 20, \
        f'Verifique se o atributo jutsu_damage da classe Jutsu' + \
        f' está sendo criado corretamente.'

    assert cria_jutsu_rasengan.chakra_spend == 15, \
        f'Verifique se o atributo chakra_spend da classe Jutsu' + \
        f' está sendo criado corretamente.'


def test_jutsu_attributes_chidori(cria_jutsu_chidori):
    assert cria_jutsu_chidori.jutsu_name == chidori['jutsu_name'], \
        f'Verifique se o atributo jutsu_name da classe Jutsu' + \
        f' está sendo criado corretamente.'

    assert cria_jutsu_chidori.jutsu_type == chidori['jutsu_type'], \
        f'Verifique se o atributo jutsu_type da classe Jutsu' + \
        f' está sendo criado corretamente.'

    assert cria_jutsu_chidori.jutsu_level == 'Unranked', \
        f'Verifique se o atributo jutsu_level da classe Jutsu' + \
        f' está sendo criado corretamente.'

    assert cria_jutsu_chidori.jutsu_type == chidori['jutsu_type'], \
        f'Verifique se o atributo jutsu_type da classe Jutsu' + \
        f' está sendo criado corretamente.'

    assert cria_jutsu_chidori.jutsu_damage == 25, \
        f'Verifique se o atributo jutsu_damage da classe Jutsu' + \
        f' está sendo criado corretamente.'

    assert cria_jutsu_chidori.chakra_spend == 100, \
        f'Verifique se o atributo chakra_spend da classe Jutsu' + \
        f' está sendo criado corretamente.'
