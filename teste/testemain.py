# n = 2
# if n == 0:
#     retur
# elif n == 1:
#     print(1)
# else:
#     fibo = [1, 1]
#     while len(fibo) < n:
#         proximo_fib = fibo[-1] + fibo[-2]
#         fibo.append(proximo_fib)

# print(fibo)

# def sequencia(n):
#     if n == 0:
#         return['Sequência se inicia em 1']
#     elif n == 1:
#         return[1]
#     else:
#         fibo = [1, 1]
#         while len(fibo) < n:
#             proximo_fib = fibo[-1] + fibo[-2]
#             fibo.append(proximo_fib)
#         return fibo
# n = 0

# print(sequencia(n))

class Televisao:
    def __init__(self):
        self.canais = ["Globo", "SBT", "Record", "Band", "RedeTV"]
        self.canal_atual = 0
        self.volume = 50
        self.mudo = False

    def mudar_canal(self, direcao):
        if direcao == "para_frente":
            self.canal_atual = (self.canal_atual + 1) % len(self.canais)
        elif direcao == "para_tras":
            self.canal_atual = (self.canal_atual - 1) % len(self.canais)

        print("Canal atual:", self.canais[self.canal_atual])

    def mudar_canal_por_numero(self, numero):
        if numero >= 1 and numero <= len(self.canais):
            self.canal_atual = numero - 1
            print("Canal atual:", self.canais[self.canal_atual])
        else:
            print("Canal inválido.")

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print("Volume:", self.volume)

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print("Volume:", self.volume)

    def alternar_mudo(self):
        if self.mudo:
            self.mudo = False
            print("Mudo desativado.")
        else:
            self.mudo = True
            print("Mudo ativado.")

        if self.mudo:
            print("Volume: 0")
        else:
            print("Volume:", self.volume)

