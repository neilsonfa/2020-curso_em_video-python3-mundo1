diaria = int(input("Quantas diárias foram usada?\n"))
km = int(input("Qual a quantidade de quilometros rodados?\n"))
print("O valor da locação é R${:.2f}.".format((diaria * 60) + (km * 0.15)))