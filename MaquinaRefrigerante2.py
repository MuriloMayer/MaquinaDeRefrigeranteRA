## CONTROLE DE USUARIO ##
print("Bem-Vindo A Maquina Do Blaze Refris")
usuario = int(input("Selecione O Nivel De Acesso (CONSUMIDOR = 1) ou (ADMINISTRADOR = 0)  \n:"))

if usuario == 0:
    senha = int(input("Digite A Senha: "))
    while senha != 123 :
        usuario = int(input("Selecione O Nivel De Acesso (CONSUMIDOR = 1) ou (ADMINISTRADOR = 0)  \n:"))
        print("Senha Incorreta")
        usuario = int(input("Selecione O Nivel De Acesso (CONSUMIDOR = 1) ou (ADMINISTRADOR = 0)  :"))
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



quantBebidas = 10

valorMoedas = valorMoeda5 + valorMoeda25 + valorMoeda10 + valorMoeda1 + valorMoeda50 
valorNotas = valorNota2 + valorNota5 + valorNota10 
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
            while valorCedula != 2 and valorCedula != 5 and valorCedula != 10  :
                print("Valor De Cedula Invalido")
                valorCedula = int(input("Digite o valor de cédula que você quer mudar: "))    
            if valorCedula == 2:
                nota2 = int(input(f"Existem {nota2}Cedulas Em Estoque\nDigite A Nova Quantidade De Cedulas\n: "))
            elif valorCedula == 5:
                nota5= int(input(f"Existem {nota5}Cedulas Em Estoque\nDigite A Nova Quantidade De Cedulas\n: "))
            elif valorCedula == 10 :
                nota10 = int(input(f"Existem {nota10}Cedulas Em Estoque\nDigite A Nova Quantidade De Cedulas\n: "))



            
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
        print(f"Nota 2$ = {nota2}\n Nota 5$ = {nota5}\n Nota 10$= {nota10}\n ")
        print(f"Valor Total De Moedas {valorMoedas}$\n Valor Total De Cedulas {valorNotas}$\nValor Total {valorTrocoTotal}$")



## CONSUMIDOR ##


if usuario == 1 :
    qtdRefri = int(input("Selecione a quantidade de refrigerantes você deseja: "))
    while qtdRefri > quantBebidas :
        print(f"Temos Somente {quantBebidas} Em Estoque")
        qtdRefri = int(input("Selecione a quantidade de refrigerantes você deseja: "))
    valorFinal = qtdRefri * precoRefri
    print("O preço final é R$", valorFinal)

    valorPago = float(input("Insira o valor a ser pago: "))
    while valorPago < valorFinal :
        print(f"Valor Insuficiente, O Preco Final é De {valorFinal}")
        valorPago = valorPago + float(input("Insira O Pagamento Restante"))

## TROCO ##

    troco = valorPago - valorFinal
    print("Seu Troco É De:")
    valor10 = int(troco // 10)
    if valor10 > 0 :
        if valor10 > 1 :
            print(f"{valor10} Notas De R$10")
        else: 
            print(f"{valor10} Notas De R$10")
    troco -= valor10 * 10

    valor5 = int(troco // 5)
    if valor5 > 0 :
        if valor5 > 1 :
            print(f"{valor5} Notas De R$5")
        else: 
            print(f"{valor5} Notas De R$5")
    troco -= valor5 * 5

    valor2 = int(troco // 2)
    if valor2 > 0 :
        if valor2 > 1 :
            print(f"{valor2} Notas De R$2")
        else: 
            print(f"{valor2} Notas De R$2")
    troco -= valor2 * 2

    valorM5 = int(troco // 0.5)
    if valorM5  > 0 :
        if valorM5 > 1 :
            print(f"{valorM5} Moedas De ¢0.5")
        else: 
            print(f"{valorM5} Moeda De ¢0.5")
    troco -= valorM5 * 0.5
  
    valorM25 = int(troco // 0.25)
    if valorM25  > 0 :
        if valorM25 > 1 :
            print(f"{valorM25} Moedas De ¢0.25")
        else: 
            print(f"{valorM25} Moedas De ¢0.25")
    troco -= valorM25 * 0.25

    valorM01 = troco // 1
    if valorM01  > 0 :
        if valorM01 > 1 :
            print(f"{valorM01} Moedas De ¢1.0")
        else: 
            print(f"{valorM01} Moedas De ¢1.0")
    troco -= valorM01 * 1.0



