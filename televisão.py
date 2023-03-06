#2) Crie uma classe que represente uma televisão com 5 canais. Deve ser possível:
#    - Alterar os canais em sequência (para frente e para trás)
#    - Alterar os canais por número
#    - Aumentar e diminuir o volume (valor máximo é 100 e mínimo é 0)
#    - Alternar o modo "mudo"

class televisao:
    def init(tipo):
        tipo.canais = ["Globo", "SBT", "Record", "Band", "RedeTV"]
        tipo.num_canal = 0
        tipo.volume = 50
        tipo.mudo = False

    def mudar_canal(tipo, direcao):
        if direcao == "para_frente":
            tipo.num_canal = (tipo.canais + 1) % len(tipo.canais)
        elif direcao == "para_tras":
            tipo.num_canal = (tipo.canais - 1) % len(tipo.canais)
        print("O canal atual é: ", tipo.canais[tipo.num_canal])

    def mudar_canal_numero(tipo, numero):
        tipo.num_canal = numero
        if numero >= 1 and numero <= len(tipo.canais):
            tipo.num_canal = numero - 1
            print("O canal atual é: ", tipo.canais[tipo.num_canal])
        else:
            print("Canal incorreto")
    def aumentar_volume(tipo):
        if tipo.aumentar_volume <= 100:
            tipo.volume += 1
            print("Volume:",  tipo.volume)
        else:
            print("Volume está no máximo!")
    def diminuir_volume(tipo):
        if tipo.diminuir_volume > 0:
            tipo.volume -= 1
            print("Volume:", tipo.volume)
    def trocar_mudo(tipo):
        if tipo.mudo == False:
            print("Mudo está desabilidato")
        else:
            print("Mudo está ativado")
        if tipo.volume == 0:
            print("Mudo está ativado")
        else:
            print("Volume: ", tipo.volume)

