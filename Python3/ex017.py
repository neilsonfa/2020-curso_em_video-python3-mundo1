from math import hypot
cateto_oposto = float(input('Qual é o tamanho do cateto oposto?\n'))
cateto_adjacente = float(input('Qual é o tamanha do cateto adjacente?\n'))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print('O tamanho da hipotenusa é {:.4f}.'.format(hipotenusa))