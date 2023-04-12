
## CONTROLE DE USUARIO ##

usuario = int(input("Selecione O Nivel De Acesso (USUARIO = 1) ou (ADMINISTRADOR = 0)  \n:"))

if usuario == 0:
    senha = int(input("Digite A Senha: "))
    while senha != 12345 :
        usuario = int(input("Selecione O Nivel De Acesso (USUARIO = 1) ou (ADMINISTRADOR = 0)  \n:"))
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

## ADMINISTRADOR ##

if usuario == 0 :
    funcao = int(input(f"Para Verificar A Quantidade De Troco, Digite ( 0 ).\nPara Modificar/Atualizar A Quantidade De Alguma Cedula Ou Moeda, Digite ( 1 ) \n:"))

    if funcao == 0 :
        print(f"Moeda  5¢ = {moeda5}")           
        print(f"Moeda 10¢ = {moeda10}")         
        print(f"Moeda 25¢ = {moeda25}")   
        print(f"Moeda 50¢ = {moeda50}")           
        print(f"Moeda 01¢ = {moeda01}") 
        print(f"Nota = {}\n Nota = {}\n Nota = {}\n Nota = {}\n Nota = {}\n Nota = {}\n")
