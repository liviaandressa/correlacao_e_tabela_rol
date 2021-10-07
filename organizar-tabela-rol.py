'''O programa abaixo organiza os numeros da tabela ROL de forma crescente'''

numero = int(input('Digite um número e [0] para encerrar:'))
lista=[numero]

while numero != 0:
    numero = int(input('Digite um número e [0] para encerrar:'))
    lista.append(numero)
print('\033[31m ESSA MERDA ORGANIZADA FICA ASSIM:\033[0;0m \n',sorted(lista))