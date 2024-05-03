#for 
texto = 'python'  
for letra in texto:
    texto = texto.replace(letra, letra.upper())
    print(texto)
print(texto)

#for com range
for numero in range(2,51,4):
    print(numero, end="-")

#While

opcao = -1
while opcao != 0:
    opcao = int(input("[1]sacar \n [2]extrato \n [0]sair \n"))

#brake 

while True:
    opcao1 = int(input("[1]sacar \n [2]extrato \n [10]sair \n"))
    if opcao1 == 10:
        break

for numero1 in range(100):
    if(numero1 == 12):
        break
    print(numero1, end="-")
#continue

for numero2 in range(100):
    if numero2 == 12:
        continue
    print(numero2, end=" ")
