from main import *

#Teste de sequência fibonacci
def test_sequencia():
    assert sequencia(0) == ['Sequência se inicia em 1']
    assert sequencia(1) == [1]
    assert sequencia(2) == [1, 1]
    assert sequencia(3) == [1, 1, 2]

def test_televisao():
    tv = televisao()

    #Mudar canal para frente
    tv.mudar_canal("para_frente")
    assert tv.num_canal == 1

    #Mudar canal para tras
    tv.mudar_canal("para_tras")
    assert tv.num_canal == 0

    #Mudar canal por numero
    tv.mudar_canal_numero(2)
    assert tv.num_canal == 1

    #Aumentar volume
    tv.aumentar_volume()
    assert tv.volume == 51

    #Diminuir volume
    tv.diminuir_volume()
    assert tv.volume == 50

    #Mudo

    tv.trocar_mudo()
    assert tv.mudo == True

    tv.trocar_mudo()
    assert tv.mudo == False