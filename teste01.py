
## CONTROLE DE USUARIO ##

usuario = int(input("Selecione O Nivel De Acesso (USUARIO = 1) ou (ADMINISTRADOR = 0)  \n:"))

if usuario == 0:
    senha = int(input("Digite A Senha: "))
    while senha != 12345 :
        usuario = int(input("Selecione O Nivel De Acesso (USUARIO = 1) ou (ADMINISTRADOR = 0)  \n:"))
        print("Senha Incorreta")
        usuario = int(input("Selecione O Nivel De Acesso (USUARIO = 1) ou (ADMINISTRADOR = 0)  :"))
        if usuario == 0:
            senha = int(input("Digite A Senha: "))


## BANCO DE DADOS ##

precoRefri = 5

moeda5 = 5
valorMoeda5 = 0.05 * moeda5

moeda10 = 5
valorMoeda10 = 0.10 * moeda10

moeda25 = 5 
valorMoeda25 = 0.25 * moeda25

moeda50 = 5 
valorMoeda50 = 0.50 * moeda50

moeda01 = 5
valorMoeda1 = 1 * moeda01


nota2 = 10
valorNota2 = 2 * nota2

nota5 = 5
valorNota5 = 5 * nota5

nota10 = 3
valorNota10 = 10 * nota10

nota20 = 2
valorNota20 = 20 * nota20

## ADMINISTRADOR ##

if usuario == 0 :
    funcao = int(input(f"Para Verificar A Quantidade De Troco, Digite ( 0 ).\nPara Modificar/Atualizar A Quantidade De Alguma Cedula Ou Moeda, Digite ( 1 ) \n:"))

    if funcao == 0 :
        print(f"Moeda  5¢ = {moeda5}")           
        print(f"Moeda 10¢ = {moeda10}")         
        print(f"Moeda 25¢ = {moeda25}")   
        print(f"Moeda 50¢ = {moeda50}")           
        print(f"Moeda 01¢ = {moeda01}") 
        print(f"Nota 2$ = {nota2}\n Nota 5$ = {nota5}\n Nota 10$= {nota10}\n Nota 20$ = {nota20}\n")

valorMoedas = valorMoeda5 + valorMoeda25 + valorMoeda10 + valorMoeda1 + valorMoeda50 
valorNotas = valorNota2 + valorNota5 + valorNota10 + valorNota20
valorTrocoTotal = valorMoedas + valorNotas

## USUARIO ##


if usuario == 1 :
    qtdRefri = int(input("Selecione a quantidade de refrigerantes você deseja: "))
    precoFinal = qtdRefri * precoRefri
    print("O preço final é R$", precoFinal)

    valorPago = float(input("Por favor, insira o valor a ser pago: "))
        
    while valorPago < precoFinal:
        print("Valor insuficiente")
        print("O preço final é R$", precoFinal)
        valorPago = float(input("Por favor, insira o valor a ser pago: "))

    if valorPago > precoFinal:
        troco = valorPago - precoFinal

        if valorTrocoTotal < troco:
            print("Não há troco suficiente para essa compra")
            continuarCompra = int(input("Aperte 1 se quiser continuar com a compra, ou 2 se quiser encerrar a compra: "))
            if continuarCompra == 1:
                print("Continuar")
            else:
                print("Compra encerrada")

        valorTrocoTotal = valorTrocoTotal - troco
        print("Compra confirmada, retire seu refrigerante")
        print("O valor do troco é R$", troco)
    else:
        print("Compra confirmada, retire seu refrigerante")
