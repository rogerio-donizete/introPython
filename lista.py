frutas = ['maça', 'laranja', 'uva', 'banana']
frutas[-1]#  banana - pega o ultimo valor
frutas[0]# maça - pega o primerio valor


matriz = [
    [1, 2, 3],
    ['a', 's', 'd'],
    [4,'f','g']
]
matriz[0] # Pega os valores da primeira linha
matriz[0][0] # Pega o valor da intersecção da primeira linha com a primeira coluna.
matriz[0][-1] # Pega o valor da intersecção da primeira linha com a ultima coluna.
matriz[-1][-1] # Pega o valor da intersecção da ultima linha com a primeira coluna.

#fatiamento
curso='python'
print(curso[1])
print(curso[:6])
print(curso[3:])
print(curso[3:6])
print(curso[1:5:2])
print(curso[:])
print(curso[::-1])

#enumerate
carros = ['gol', "celta", 'palio']

for indice, carro in enumerate(carros):
    print(f'{indice}:{carro}')

#comprehion list
numeros = [1, 30, 21, 2, 9, 65, 34]
pares=[]
#usando for
for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)
#usando o coprehetion list
pares2 =[numero0 for numero0 in numeros if numero0 % 2 == 0] 
#lista    retorno     iteração  iteração  filtro(opcional)

ao_quadrado=[numero ** 2 for numero in numeros]

print(pares)
print(pares2)