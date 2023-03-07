#Crie uma função que, dado um número inteiro N, que retorne a lista dos N primeiros números da sequência de Fibonacci (a sequência de Fibonacci começa com o número 1)

def sequencia(n):
    if n == 0:
        return['Sequência se inicia em 1']
    elif n == 1:
        return[1]
    else:
        fibo = [1, 1]
        while len(fibo) < n:
            proximo_fib = fibo[-1] + fibo[-2]
            fibo.append(proximo_fib)
        return fibo

#2) Crie uma classe que represente uma televisão com 5 canais. Deve ser possível:
#    - Alterar os canais em sequência (para frente e para trás)
#    - Alterar os canais por número
#    - Aumentar e diminuir o volume (valor máximo é 100 e mínimo é 0)
#    - Alternar o modo "mudo"

class televisao:
    def __init__(self):
        self.canais = ["Globo", "SBT", "Record", "Band", "RedeTV"]
        self.num_canal = 0
        self.volume = 50
        self.mudo = False

    def mudar_canal(self, direcao):
        if direcao == "para_frente":            
            self.num_canal = (self.num_canal + 1) % len(self.canais)
        elif direcao == "para_tras":
            self.num_canal = (self.num_canal - 1) % len(self.canais)
        print("O canal atual é: ", self.canais[self.num_canal])

    def mudar_canal_numero(self, numero):
        self.num_canal = numero
        if numero >= 1 and numero <= len(self.canais):
            self.num_canal = numero - 1
            print("O canal atual é: ", self.canais[self.num_canal])
        else:
            print("Canal incorreto")

    def aumentar_volume(self):
        self.mudo = False
        if self.volume <= 100:
            self.volume += 1
            print("Volume aumentado para: ",  self.volume)
        else:
            print("Volume está no máximo!")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print("Volume diminuido para:", self.volume)
        else:
            self.mudo = True

    def trocar_mudo(self):
        self.mudo = not self.mudo
        if self.mudo:
            self.volume = 0
            print("Mudo ativado")
        else:
            self.volume = 50
            print("Mudo desativado")