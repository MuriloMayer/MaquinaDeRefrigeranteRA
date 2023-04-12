
## CONTROLE DE USUARIO ##

usuario = int(input("Selecione O Nivel De Acesso (USUARIO = 1) ou (ADMINISTRADOR = 0)  :"))

if usuario == 0:
    senha = int(input("Digite A Senha: "))
    while senha != 12345 :
        print("Senha Incorreta")
        usuario = int(input("Selecione O Nivel De Acesso (USUARIO = 1) ou (ADMINISTRADOR = 0)  :"))
        if usuario == 0:
            senha = int(input("Digite A Senha: "))

## BANCO DE DADOS DE TROCO ##

moeda5 = 5
valorMoeda5 = 0.05 * 5

moeda10 = 5
valorMoeda10 = 0.10 * 5

moeda25 = 5 
valorMoeda25 = 0.25 * 5

moeda50 = 5 
valorMoeda50 = 0.50 * 5

moeda01 = 5
valorMoeda1 = 1 * 5


nota2 = 10
valorNota2 = 2 * 10

nota5 = 5
valorNota5 = 5 * 15

nota10 = 3
valorNota10 = 10 * 3

nota20 = 2
valorNota20 = 20 * 2

valorMoedas = valorMoeda5 + valorMoeda25 + valorMoeda10 + valorMoeda1 + valorMoeda50 
valorNotas = valorNota2 + valorNota5 + valorNota10 + valorNota20

valorTrocoTotal = valorMoedas + valorNotas

## CONTROLE DE USUARIO ##

usuario = int(input("Selecione O Nivel De Acesso (USUARIO = 1) ou (ADMINISTRADOR = 0)  :"))

precoRefri = 5

if usuario == 0:
    senha = int(input("Digite A Senha: "))
    while senha != 12345 :
        print("senha incorreta")
        usuario = int(input("Selecione O Nivel De Acesso (USUARIO = 1) ou (ADMINISTRADOR = 0)  :"))
        if usuario == 0:
            senha = int(input("Digite A Senha: "))

else:
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