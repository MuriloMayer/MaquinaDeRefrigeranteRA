
<<<<<<< Updated upstream
=======
## CONTROLE DE USUARIO ##

usuario = int(input("Selecione O Nivel De Acesso (USUARIO = 1) ou (ADMINISTRADOR = 0)  :"))

if usuario == 0:
    senha = int(input("Digite A Senha: "))
    while senha != 12345 :
        print("Senha Incorreta")
        usuario = int(input("Selecione O Nivel De Acesso (USUARIO = 1) ou (ADMINISTRADOR = 0)  :"))
        if usuario == 0:
            senha = int(input("Digite A Senha: "))

>>>>>>> Stashed changes
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



