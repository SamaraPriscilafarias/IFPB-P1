alcool = 0
gasolina = 0
diesel = 0

while True:
    codigo = int(input())

    if codigo == 1:
        alcool += 1
    elif codigo == 2:
        gasolina += 1
    elif codigo == 3:
        diesel += 1
    elif codigo == 4:
        break
    else:
        print("Código inválido! Digite 1 (Álcool), 2 (Gasolina), 3 (Diesel) ou 4 (Fim).")

print("MUITO OBRIGADO")
print("Álcool:", alcool)
print("Gasolina:", gasolina)
print("Diesel:", diesel)
