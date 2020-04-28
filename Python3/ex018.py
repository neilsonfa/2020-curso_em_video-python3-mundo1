from math import sin, cos, tan, radians
angulo = int(input('Informe o ângulo:\n'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno do ângulo é {:.6f}, o cosneno é {:.6f}, e a tangente é {:.6f}.\n'.format(seno, cosseno, tangente))