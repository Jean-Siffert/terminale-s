from math import exp
from os import system
system('cls')

def f(x): return float((1)/(1+exp(1-x)))

x_minimum = 0
x_maximum = 1
n_maximum = 15
zero_en_plus = 20
j = [] # majorants
i = [] # minorants

for n in range(1,n_maximum):
    ecart_entre_zone = (1)/(2**(n-1))
    nombre_de_zone = 2**(n-1)
    somme_aires_minorants = 0
    somme_aires_majorants = 0
    for indice_zone in range(0, nombre_de_zone):
        abscisse_minorant = (indice_zone*ecart_entre_zone)
        abscisse_majorant = ((indice_zone+1)*ecart_entre_zone)
        somme_aires_majorants += f(abscisse_majorant)*((x_maximum-x_minimum)/nombre_de_zone)
        somme_aires_minorants += f(abscisse_minorant)*((x_maximum-x_minimum)/nombre_de_zone)
    i.append(somme_aires_minorants)
    j.append(somme_aires_majorants)

print('Minorants \t\t Majorants \t\t Différences')
print('---------------------------------------------------------------------')
for indice in range(0,len(i)):
    print('{} \t {} \t {}'.format(str(i[indice]).zfill(zero_en_plus),str(j[indice]).zfill(zero_en_plus),(j[indice]-i[indice])))
