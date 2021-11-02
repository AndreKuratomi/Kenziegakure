def test_ninja_learn_jutsu_return(cria_ninja_naruto, cria_jutsu_rasengan):
    print(cria_ninja_naruto.jutsu_list)
    result = cria_ninja_naruto.learn_jutsu(cria_jutsu_rasengan)
    print(cria_ninja_naruto.jutsu_list)
    expected = 'O ninja Naruto Uzumaki acabou de aprender um novo jutsu: Rasengan'

    assert result == expected, \
        'Verifique se a string retornada está no formato EXATO ' + \
        'ao citado no enunciado'


def test_ninja_learn_jutsu_has_added_succefully(
    cria_ninja_naruto,
    cria_jutsu_rasengan,
    cria_jutsu_chidori
):

    cria_ninja_naruto.learn_jutsu(cria_jutsu_chidori)
    cria_ninja_naruto.learn_jutsu(cria_jutsu_rasengan)

    result = sorted([cria_jutsu_rasengan, cria_jutsu_chidori],
                    key=lambda x: x.jutsu_name)

    for i, jutsu in enumerate(sorted(cria_ninja_naruto.jutsu_list,
                                     key=lambda x: x.jutsu_name)):
        assert jutsu == result[i], \
            'Verifique se o método learn_jutsu está adicionando jutsus corretamente'
