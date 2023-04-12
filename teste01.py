
## CONTROLE DE USUARIO ##

usuario = int(input("Selecione O Nivel De Acesso (USUARIO = 1) ou (ADMINISTRADOR = 0)  :"))

if usuario == 0:
    senha = int(input("Digite A Senha: "))
    while senha != 12345 :
        usuario = int(input("Selecione O Nivel De Acesso (USUARIO = 1) ou (ADMINISTRADOR = 0)  :"))
        if usuario == 0:
            senha = int(input("Digite A Senha: "))

## BANCO DE DADOS DE TROCO ##

moeda5 = 5
moeda10 = 5
moeda25 = 5 
moeda50 = 5 
moeda01 = 5

nota2 = 10
nota5 = 5
nota10 = 3
nota20 = 2
nota50 = 0
nota100 = 0
