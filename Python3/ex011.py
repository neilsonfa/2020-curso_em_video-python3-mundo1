altura = float(input("Qual é a largura da parede em metros?\n"))
largura = float(input("Qual é a altura da parede em metros?\n"))
area = altura * largura
tinta = area / 2
print("A parede possui {}m² e será necessário {}L de tinta para pintá-la.".format(area, tinta))
print("*"*50)