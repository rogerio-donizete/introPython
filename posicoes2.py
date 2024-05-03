def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa,marca, motor, combustivel)
#antes d abarra deve ser somente posicional, não pode sernoemado, depois da barra é opcional ser noemado ou posicional

def criar_carro2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa,marca, motor, combustivel)
# tudo depois do asterico é obrigatorio ser nomeado

def criar_carro2( modelo, ano, placa, /,marca,*,motor, combustivel):
    print(modelo, ano, placa,marca, motor, combustivel)
    #antes da barra deve ser somente posicionale depois do asterico é obrigatorio ser nomeado, entre eles é opcionaol.

    # funçoes são objetos de priemria classe, isso que dizer que podem ser passadas como funão, retornadoa por uma funçãpo, serem variavies ou arguemntos.

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, podeserqualquernome):
    resultado = podeserqualquernome(a, b)
    print(f"O resuldado da operação {a} e {b} = {resultado}")

exibir_resultado(10, 15, somar)
exibir_resultado(10, 15, subtrair)

