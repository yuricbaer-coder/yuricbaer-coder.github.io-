pagar = float(input("Qual o valor da conta? R$ "))
loop = False

while not loop:
    gorjeta = int(input("Avalie nosso atendimento (1 a 5): "))

    if gorjeta > 5 or gorjeta < 1:
        print("ERROR: Nota inválida. Digite entre 1 e 5.")
    elif gorjeta in [1, 2]:
        valor_gorjeta = pagar * 0.05
        print("Obrigado pelos 5% de gorjeta.")
        loop = True
    elif gorjeta == 3:
        valor_gorjeta = pagar * 0.10
        print("Obrigado pelos 10% de gorjeta.")
        loop = True
    elif gorjeta == 4:
        valor_gorjeta = pagar * 0.15
        print("Obrigado pelos 15% de gorjeta.")
        loop = True
    elif gorjeta == 5:
        valor_gorjeta = pagar * 0.20
        print("Obrigado pelos 20% de gorjeta.")
        loop = True


total = pagar + valor_gorjeta
print(f"Total a pagar: R$ {total:.2f}")