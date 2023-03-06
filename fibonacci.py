#Crie uma função que, dado um número inteiro N, que retorne a lista dos N primeiros números da sequência de Fibonacci (a sequência de Fibonacci começa com o número 1)

def sequencia(n):
    if n == 0:
        return[]
    elif n == 1:
        return[1]
    else:
        fibo = [1, 1]
        while len(fibo) < n:
            proximo_fib = fibo[-1] + fibo[-2]
            fibo.append(proximo_fib)
        return fibo
    
n = 10
resultado = sequencia(n)

print(resultado)
