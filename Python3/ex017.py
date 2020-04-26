from math import pow, sqrt
cateto_oposto = float(input('Qual é o tamanho do cateto oposto?\n'))
cateto_adjacente = float(input('Qual é o tamanha do cateto adjacente?\n'))
hipotenusa = pow(cateto_oposto, 2) + pow(cateto_adjacente, 2)
print('O tamanho da hipotenusa é {}.'.format(sqrt(hipotenusa)))