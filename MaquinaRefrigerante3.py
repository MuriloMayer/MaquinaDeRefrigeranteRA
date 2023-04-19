from decimal import Decimal


## CONTROLE DE USUARIO ##

print("Bem-Vindo A Maquina Do Blaze Refris")
usuario = int(input("Selecione O Nivel De Acesso (CONSUMIDOR = 1) ou (ADMINISTRADOR = 0)  \n:"))
while usuario != 0 and usuario != 1 :
    usuario = int(input("Selecione O Nivel De Acesso (CONSUMIDOR = 1) ou (ADMINISTRADOR = 0)  \n:"))

if usuario == 0:
    senha = int(input("Digite A Senha: "))
    while senha != 123 or usuario == 1:
        print("Senha Incorreta")
        usuario = int(input("Selecione O Nivel De Acesso (CONSUMIDOR = 1) ou (ADMINISTRADOR = 0)  \n:"))
        if usuario == 0 :
            senha = int(input("Digite A Senha:"))
        elif usuario == 1 :
            break


## BANCO DE DADOS ## 

preco_refri = 5

moeda5 = 5
valor_moeda5 = 0.05 * moeda5

moeda10 = 5
valor_moeda10 = 0.10 * moeda10

moeda25 = 5 
valor_moeda25 = 0.25 * moeda25

moeda50 = 5 
valor_moeda50 = 0.50 * moeda50

moeda01 = 5
valor_moeda1 = 1 * moeda01

nota2 = 10
valor_nota2 = 2 * nota2

nota5 = 5
valor_nota5 = 5 * nota5

nota10 = 3
valor_nota10 = 10 * nota10


quant_bebidas = 10
valor_moedas = valor_moeda5 + valor_moeda25 + valor_moeda10 + valor_moeda1 + valor_moeda50 
valor_notas = valor_nota2 + valor_nota5 + valor_nota10 
valor_troco_total = valor_moedas + valor_notas 

## ADMINISTRADOR ##

if usuario == 0 :    
    funcao = int(input("Para verificar a quantidade de troco, digite ( 0 ).\nPara adicionar/atualizar a quantidade de alguma cédula ou moeda, digite ( 1 ) \nPara adicionar/atualizar a quantidade de bebidas digite ( 2 ) \n: "))
    while funcao != 0 and funcao != 1 and funcao != 2:
        print("Função invalida")
    if funcao == 1 :
        nota_ou_cedula = int(input("Digite ( 1 ) para mudar quantidade de cédulas \nDigite ( 2 ) se quer mudar a quantidade de moedas\n: "))
        if nota_ou_cedula == 1:
            valor_cedula = int(input("Digite o valor de cédula que você quer mudar: "))
            while valor_cedula != 2 and valor_cedula != 5 and valor_cedula != 10  :
                print("Valor de cédula inválido")
                valor_cedula = int(input("Digite o valor de cédula que você quer mudar: "))    
            if valor_cedula == 2:
                nota2 = int(input(f"Existem {nota2} cédulas em estoque\nDigite a nova quantidade de cédulas\n: "))
                print(nota2)
            elif valor_cedula == 5:
                nota5= int(input(f"Existem {nota5} cédulas em estoque\nDigite a nova quantidade de cédulas\n: "))
            elif valor_cedula == 10 :
                nota10 = int(input(f"Existem {nota10} cédulas em estoque\nDigite a nova quantidade de cédulas\n: "))

        elif nota_ou_cedula == 2:
            valor_moeda = float(input("Digite o valor de moeda que você quer mudar: "))
            while valor_moeda != 0.05 and valor_moeda != 0.10 and valor_moeda != 0.25 and valor_moeda != 0.50 and valor_moeda != 1 :
                print("Valor de moeda inválido")
                valor_moeda = float(input("Digite o valor de moeda que você quer mudar: "))

            if valor_moeda == 0.05:
                    moeda5 = float(input(f"Existem {moeda5} moedas em estoque\nDigite a nova quantidade de moedas\n: "))
            elif valor_moeda == 0.10:
                    moeda10 = float(input(f"Existem {moeda10} moedas em estoque\nDigite a nova quantidade de moedas\n: "))
            elif valor_moeda == 0.25:
                    moeda25 = float(input(f"Existem {moeda25} moedas em estoque\nDigite a nova quantidade de moedas\n: "))
            elif valor_moeda == 0.50:
                    moeda50 = float(input(f"Existem {moeda50} moedas em estoque\nDigite a nova quantidade de moedas\n: "))
            elif valor_moeda == 1:
                    moeda01 = int(input(f"Existem {moeda01} moedas em estoque\nDigite a nova quantidade de moedas\n: "))

    
                
    elif funcao == 2 :
        quant_bebidas = int(input(f"Existem {quant_bebidas} bebidas em estoque\nDigite a nova quantidade de bebidas\n: "))
                       

    elif funcao == 0 :
        print(f"Moeda 5$ = {moeda5}\nMoeda 10$ = {moeda10}\nMoeda 25$ = {moeda25}\nMoeda 50$ = {moeda50}\nMoeda 1$ = {moeda01}\n")
        print(f"Nota 2$ = {nota2}\n Nota 5$ = {nota5}\n Nota 10$= {nota10}\n ")
        print(f"Valor total de moedas {valor_moedas}$\n Valor total de cédulas {valor_notas}$\nValor total {valor_troco_total}$")



## CONSUMIDOR ##


if usuario == 1 :
    print(f'O preço do refrigerante é {preco_refri}')
    qtd_refri = int(input("Selecione a quantidade de refrigerantes você deseja: "))
    while qtd_refri > quant_bebidas :
        print(f"Temos somente {quant_bebidas} em estoque")
        qtd_refri = int(input("Selecione a quantidade de refrigerantes você deseja: "))
    valor_final = qtd_refri * preco_refri
    print("O preço final é R$", valor_final)

    valor_pago = 0
    print("Só aceitamos notas de 2, 5 e 10")
    print("Só aceitamos moedas de 0.05, 0.25 e 1 real")

    # while valor_pago < valor_final :
    #     print(f"Valor insuficiente, o preço final é de {valor_final}")
    #     valor_pago = valor_pago + float(input("Insira o pagamento restante"))


    notas_inseridas = 1

    while valor_pago < valor_final:
        nota_inserida = Decimal(input(f'Insira o valor da {notas_inseridas} nota ou moeda (Se for moeda, inserir o número com o decimal, por exemplo: 0.50): '))

        while nota_inserida == 20 or nota_inserida == 50 or nota_inserida == 50 or nota_inserida == 100 or nota_inserida == 200:
            print("Não trabalhamos com esse valor")
            nota_inserida = Decimal(input(f'Insira o valor da {notas_inseridas} nota ou moeda (Se for moeda, inserir o número com o decimal, por exemplo: 0.50): '))

        if nota_inserida == 2:
            nota2 += 1
        elif nota_inserida == 5:
            nota5 +=1 
        elif nota_inserida == 10:
            nota10 +=1 
        elif nota_inserida == 0.05:
            moeda5 +=1 
        elif nota_inserida == 0.10:
            moeda10 +=1 
        elif nota_inserida == 0.25:
            moeda25 +=1 
        elif nota_inserida == 0.50:
            moeda50 +=1 
        elif nota_inserida == 1:
            moeda01 +=1 
    
        notas_inseridas += 1
        valor_pago = valor_pago + nota_inserida
    

## TROCO ##


    troco = float(valor_pago - valor_final)
    if troco == 0: 
        print("Compra Finalizada, Blaze Refris Agradece A Preferencia")

    valor10 = int(troco / 10)
    if valor10 > 0 :
        if valor10 > 1 :
            print(f"{valor10} Notas De R$10")
        else: 
            print(f"{valor10} Notas De R$10")
    troco -= valor10 * 10

    valor5 = int(troco / 5)
    if valor5 > 0 :
        if valor5 > 1 :
            print(f"{valor5} Notas De R$5")
        else: 
            print(f"{valor5} Notas De R$5")
    troco -= valor5 * 5

    valor2 = int(troco / 2)
    if valor2 > 0 :
        if valor2 > 1 :
            print(f"{valor2} Notas De R$2")
        else: 
            print(f"{valor2} Notas De R$2")
    troco -= valor2 * 2



    valorM01 = int(troco / 1)
    if valorM01  > 0 :
        if valorM01 > 1 :
            print(f"{valorM01} Moedas De ¢1.0")
        else: 
            print(f"{valorM01} Moedas De ¢1.0")
    troco -= valorM01 * 1.0
  

    valorM25 = int(troco / 0.25)
    if valorM25  > 0 :
        if valorM25 > 1 :
            print(f"{valorM25} Moedas De ¢0.25")
        else: 
            print(f"{valorM25} Moedas De ¢0.25")
    troco -= valorM25 * 0.25

    valorM5 = float(round(troco / 0.05))
    if valorM5  > 0 :
        if valorM5 > 1 :
            print(f"{valorM5} Moedas De ¢0.05")
        else: 
            print(f"{valorM5} Moeda De ¢0.05")


