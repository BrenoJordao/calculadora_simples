print("=-"*30)#parede divisória para deixar bonito
ce1 = int(input("Digite um número "))#começo de equação 1 (primeiro valor)
print("=-"*30)#parede divisória para deixar bonito
ce2 = int(input("Digite outro "))    #começo de equação 2 (segundo valor)
print("=-"*30)#parede divisória para deixar bonito
ce3 = str(input("Você quer a soma, subtração, multiplicação ou divisao?(responda com +,-,* ou /) " ))#começo de equação 3 (qual aritimética)

print("=-"*30)#parede divisória para deixar bonito
if ce3 == "+":#se a aritimética escolhida for soma:
    r1 = (ce1 + ce2)#resultado 1 = começo de equação 1 + começo de equação 2
    print("A soma de {} com {} é igual a {}".format(ce1,ce2,r1))#fim da equação1

elif ce3 == "-":#se a aritimética escolhida for subtração:
    r2 = (ce1 - ce2)#resultado 2 = começo de equação 1 - começo de equação 2
    print("A subtração de {} com {} é igual a {}".format(ce1,ce2,r2))#fim da equação 2

elif ce3 == "*":#se a aritimética escolhida for multiplicação:
    r3 = (ce1 * ce2)#resultado 3 = começo de equação 1 vezes começo de equação 2
    print("A multiplicação de {} com {} é igual a {}".format(ce1,ce2,r3))#fim da equação 3

elif ce3 == "/":#se a aritimética escolhida for divisão:
    r4 = (ce1 / ce2)#resultado 4 = começo de equação 1 divdido por começo de equação 2
    print("A divisão de {} com {} é igual a {}".format(ce1,ce2,r4))#fim da equação 4

print("=-"*30)#parede divisória para deixar bonito