from math import sqrt

quatidade_numeros = int(input('digite a quatidade de numeros: '))
xy = float(input('informe o valor de xy: '))
x = float(input('informe o valor de x: '))
y = float(input('informe o valor de y: '))
quadradox = float(input('informe o quadrado de x: '))
quadradoy = float(input('informe o quadrado de y: '))

primeira_parte = xy - (x * y / quatidade_numeros ) # xy - (x *y / n)
segunda_parte = quadradox - (x * x / quatidade_numeros) #x*x - (x*x / n)
terceira_parte = quadradoy - (y * y / quatidade_numeros) #y*y - (y*y / n)
quarta_parte = segunda_parte * terceira_parte
raiz = sqrt(quarta_parte)
quinta_parte= primeira_parte / raiz #resultado


print('Resultado de xy - (x *y / n) : {:.2f}  '.format(primeira_parte))
print('Resultado de x*x - (x*x / n): {:.2f} '.format(segunda_parte))
print('Resultado de xy - (x *y / n): {:.2f} '.format(terceira_parte))
print('Resultad de xy - (x *y / n) * xy - (x *y / n) : {:.2f} '.format(quarta_parte))
print('Resultado final: {:.2f} '.format(quinta_parte))

print('-' * 50)
if quinta_parte >0 and quinta_parte <1:
    print('Correlação não perfeita positiva')
elif quinta_parte <0 and quinta_parte> -1:
    print('Correlação não perfeita negativa')
elif quinta_parte ==1:
    print('Correlação perfeita positiva')
elif quinta_parte == -1:
    print('Correlação perfeita negativa')
print('-' * 50)

#print('terceira parte: ', terceira_parte)
