numero = int(input('Digite um número de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('A unidade é {}.'.format(unidade))
print('A dezena é {}.'.format(dezena))
print('A centena é {}.'.format(centena))
print('O milhar é {}.'.format(milhar))
