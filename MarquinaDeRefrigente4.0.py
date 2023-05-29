from decimal import Decimal

def calcular_troco(valor_troco, nota):
    valor = int(valor_troco / nota)
    if valor > 0:
        if valor > 1:
            print(f'{valor} - {nota} $')
        else:
            print(f'{valor} - {nota} $')
    valor_troco -= valor * nota
    return valor_troco

def gerar_codigo_pix(chave_pix, valor, nome_recebedor, cidade_recebedor):
    dados_pix = f"SPD*1.0*{chave_pix}*{nome_recebedor}*{cidade_recebedor}**{valor}**"
    return dados_pix


## CONTROLE DE USUARIO ##

print("Bem-Vindo A Maquina Do Blaze Refris")
usuario = int(input("Selecione O Nivel De Acesso (CONSUMIDOR = 1) ou (ADMINISTRADOR = 0)\nSe Desejar Sair, Digite (3)  \n:"))
while usuario != 0 and usuario != 1 or usuario == 3:
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
    pagamento = int(input("Se Desejar Pagar Com PIX Digite (1)\nSe Desejar Pagar Com Dinheiro Digite (2)"))
    valor_pago = 0
    print("Aceitamos\nNotas De 2, 5 e 10\nMoedas De 0.05, 0.25, e 1 Real")

    # while valor_pago < valor_final :
    #     print(f"Valor insuficiente, o preço final é de {valor_final}")
    #     valor_pago = valor_pago + float(input("Insira o pagamento restante"))

    notas_inseridas = 1


    if pagamento == 2 :
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
        else: 
            troco = calcular_troco(troco, 10)
            troco = calcular_troco(troco, 5)
            troco = calcular_troco(troco, 2)
            troco = calcular_troco(troco, 1)
            troco = calcular_troco(troco, 0.25)
            troco = calcular_troco(troco, 0.1)

## PIX ##

    elif pagamento == 1 :
        print("Pagamento Em Pix Selecionado.")

        chave_pix = "123123123123"
        valor = valor_final
        nome_recebedor = "BlazeRefrigerante"
        cidade_recebedor = "Curitiba/Pr"


        codigo_pix = gerar_codigo_pix(chave_pix, valor, nome_recebedor, cidade_recebedor)
        print(codigo_pix,"\nEfetue O Pagamento Com A Chave Acima")

        telefone = input("Digite O Seu Telefone No Formato (+55 DDD 9999-9999)")


## Matriz Dados Pix ##

    
