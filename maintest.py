from main import *

#Teste de sequência fibonacci
def test_sequencia():
    assert sequencia(0) == ['Sequência se inicia em 1']
    assert sequencia(1) == [1]
    assert sequencia(2) == [1, 1]
    assert sequencia(3) == [1, 1, 2]

def test_televisao():
    tv = televisao

    #Mudar canal para frente

    # televisao.mudar_canal("para_frente")
    # tv.mudar_canal("para_frente")
    # assert tv.num_canal == 1  

    tv.mudar_canal("para_frente")
    assert tv.num_canal == 1