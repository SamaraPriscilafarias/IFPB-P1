idade = int(input("Digite sua idade: "))
soma = 0
contador = 0

while idade >= 0:
    soma += idade
    contador += 1
    idade=int(input("Digite sua idade: "))

    if idade < 0:
        break
media = soma / contador
print(f"{media:.2f}")