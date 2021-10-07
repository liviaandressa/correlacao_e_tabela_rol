def espaco():
    print('-' * 50)

#********************************** CALCULO PARA X ********************************************
print('\033[31m  VAMOS CALCULAR OS VALORES DE X \033[0;0m')


numx = float(input("Digite o valor de X [0 para terminar]: "))
somax = 0
lista_quadrados = []
listax= []

while numx != 0:
    somax = somax + numx            #soma total de todos os números digitados
    quadrado = numx * numx          #qualculo do quadrado de cada número
    lista_quadrados.append(quadrado)
    listax.append(numx)
    numx = float(input("Digite o valor de X [0 para terminar]: "))

espaco()
print("A soma dos números de [X] foi: ", somax)
print('Lista com o quadrado dos números digitados: ', lista_quadrados)
print('soma do quadrado dos números quadrados: ', sum(lista_quadrados))
espaco()

#********************************** CALCULO PARA Y ********************************************

print('\033[31m AGORA VAMOS CALCULAR OS DE  Y \033[0;0m')

numy = float(input("Digite o valor de Y [0 para terminar]: "))
somay = 0
lista_quadrados = []
listay = []

while numy != 0:
    somay = somay + numy            #soma total de todos os números digitados
    quadrado = numy * numy          #qualculo do quadrado de cada número
    lista_quadrados.append(quadrado)
    listay.append(numy)
    numy = float(input("Digite o valor de y [0 para terminar]: "))


multiplicacao = [x*y for x,y in zip(listax,listay)] #Multiplica x por y

espaco()
print("A soma dos números de [Y] foi: ", somay)
print('Lista com o quadrado dos números digitados: ', lista_quadrados)
print('soma do quadrado dos números : ', sum(lista_quadrados))
espaco()

print('Lista da Multiplicação de X e Y:', multiplicacao)
print('Soma total da multiplicação: ', sum(multiplicacao))

