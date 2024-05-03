#tupla é uma lista imutavel, lista é represetado por parentese e a tupla por parenteses.

exemplo_tupla =("maça", 2, 2.5, "teste")
frutas=('maça', 'pera', 'uva',) #uma boa prativa é terminar as tuplas com virgula para o intepretador não confundir com priorização de operação matematica.
letras=tuple('python')
numeros=([1,2,3,4]) #passando uma lsita dentro de uma tupla ela é convertida para tupla.
pais=('brasil')

print(isinstance(pais,tuple))

print(frutas[0])
print(frutas[2])
print(frutas[-1])
print(frutas[-2])

matriz = (
    (1, 2, 3),
    ('a', 's', 'd'),
    (4,'f','g')
)
matriz[0] # Pega os valores da primeira linha
matriz[0][0] # Pega o valor da intersecção da primeira linha com a primeira coluna.
matriz[0][-1] # Pega o valor da intersecção da primeira linha com a ultima coluna.
matriz[-1][-1] # Pega o valor da intersecção da ultima linha com a primeira coluna.

#matriz e fatiamento funciaonam igula a lista.

#tupla tem os metodos:
#count
#len
#index