## CONTROLE DE USUARIO ##
print("Bem-Vindo A Maquina Do Blaze Refris")
usuario = int(input("Selecione O Nivel De Acesso (USUARIO = 1) ou (ADMINISTRADOR = 0)  \n:"))

if usuario == 0:
    senha = int(input("Digite A Senha: "))
    while senha != 123 :
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

quantBebidas = 10

valorMoedas = valorMoeda5 + valorMoeda25 + valorMoeda10 + valorMoeda1 + valorMoeda50 
valorNotas = valorNota2 + valorNota5 + valorNota10 + valorNota20
valorTrocoTotal = valorMoedas + valorNotas 

## ADMINISTRADOR ##

if usuario == 0 :    
    funcao = int(input("Para Verificar A Quantidade De Troco, Digite ( 0 ).\nPara Adicionar/Atualizar A Quantidade De Alguma Cedula Ou Moeda, Digite ( 1 ) \nPara Adicionar/Atualizar A Quantidade De Bebidas Digite ( 2 ) \n: "))
    while funcao != 0 and funcao != 1 and funcao != 2:
        print("Função Invalida")
    if funcao == 1 :
        notaOuCedula = int(input("Digite ( 1 ) para mudar quantidade de cédulas \nDigite ( 2 ) se quer mudar a quantidade de moedas\n: "))
        if notaOuCedula == 1:
            valorCedula = int(input("Digite o valor de cédula que você quer mudar: "))
            while valorCedula != 2 and valorCedula != 5 and valorCedula != 10 and valorCedula != 20 :
                print("Valor De Cedula Invalido")
                valorCedula = int(input("Digite o valor de cédula que você quer mudar: "))    
            if valorCedula == 2:
                nota2 = int(input(f"Existem {nota2}Cedulas Em Estoque\nDigite A Nova Quantidade De Cedulas\n: "))
            elif valorCedula == 5:
                nota5= int(input(f"Existem {nota5}Cedulas Em Estoque\nDigite A Nova Quantidade De Cedulas\n: "))
            elif valorCedula == 10 :
                nota10 = int(input(f"Existem {nota10}Cedulas Em Estoque\nDigite A Nova Quantidade De Cedulas\n: "))
            elif valorCedula == 20 :
                nota20 = int(input(f"Existem {nota20}Cedulas Em Estoque\nDigite A Nova Quantidade De Cedulas\n: "))


            
        elif notaOuCedula == 2:
            valorMoeda = int(input("Digite o valor de moeda que você quer mudar: "))
            while valorMoeda != 5 and valorMoeda != 10 and valorMoeda != 25 and valorMoeda != 50 and valorMoeda != 1 :
                print("Valor De Moeda Invalido")

                if valorMoeda == 5:
                    moeda5 = int(input(f"Existem {moeda5}Moedas Em Estoque\nDigite A Nova Quantidade De Moedas\n: "))
                elif valorMoeda == 10:
                    moeda10 = int(input(f"Existem {moeda10}Moedas Em Estoque\nDigite A Nova Quantidade De Moedas\n: "))
                elif valorMoeda == 25:
                    moeda25 = int(input(f"Existem {moeda25}Moedas Em Estoque\nDigite A Nova Quantidade De Moedas\n: "))
                elif valorMoeda == 50:
                    moeda50 = int(input(f"Existem {moeda50}Moedas Em Estoque\nDigite A Nova Quantidade De Moedas\n: "))
                elif valorMoeda == 1:
                    moeda01 = int(input(f"Existem {moeda01}Moedas Em Estoque\nDigite A Nova Quantidade De Moedas\n: "))
    elif funcao == 2 :
        quantBebidas = int(input(f"Existem {quantBebidas} Bebidas Em Estoque\nDigite A Nova Quantidade De Bebidas\n: "))
                       

    elif funcao == 0 :
        print(f"Moeda 5¢ = {moeda5}\nMoeda 10¢ = {moeda10}\nMoeda 25¢ = {moeda25}\nMoeda 50¢ = {moeda50}\nMoeda 1$ = {moeda01}\n")
        print(f"Nota 2$ = {nota2}\n Nota 5$ = {nota5}\n Nota 10$= {nota10}\n Nota 20$ = {nota20}\n")
        print(f"Valor Total De Moedas {valorMoedas}$\n Valor Total De Cedulas {valorNotas}$\nValor Total {valorTrocoTotal}$")



## USUARIO ##


if usuario == 1 :
    qtdRefri = int(input("Selecione a quantidade de refrigerantes você deseja: "))
    while qtdRefri > quantBebidas :
        print(f"Temos Somente {quantBebidas} Em Estoque")
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
