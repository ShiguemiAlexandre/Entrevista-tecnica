import pytest
from testemain import *
# Testes para o item 2

def test_televisao():
    tv = Televisao()

    # Teste de mudança de canal para frente
    tv.mudar_canal("para_frente")
    assert tv.canal_atual == 1

    # Teste de mudança de canal para trás
    tv.mudar_canal("para_tras")
    assert tv.canal_atual == 0

    # Teste de mudança de canal por número
    tv.mudar_canal_por_numero(3)
    assert tv.canal_atual == 2

    # Teste de mudança de canal inválido
    tv.mudar_canal_por_numero(6)
    assert tv.canal_atual == 2

    # Teste de aumento de volume
    tv.aumentar_volume()
    assert tv.volume == 51

    # Teste de diminuição de volume
    tv.diminuir_volume()
    assert tv.volume == 50

    # Teste de mudo ativado
    tv.alternar_mudo()
    assert tv.mudo == True
    assert tv.volume == 0

    # Teste de mudo desativado
    tv.alternar_mudo()
    assert tv.mudo == False
    assert tv.volume == 50