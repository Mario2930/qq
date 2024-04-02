"""minutos = int(input("Quantos minutos você utilizou neste mês:"))
if minutos < 200:
    preco = 0.2*minutos
else:
    if minutos <= 400:
        preco = 0.18 * minutos
    else:
        preco = 0.15 * minutos
print("Você vai pagar este mês R$ %.2f"%preco)"""

"""
ctg = int(input("Digite a categoria do produto:"))
if ctg == 1:
    prc = 10
elif ctg == 2:
    prc = 18
elif ctg == 3:
    prc = 23
elif ctg == 4:
    prc = 26
elif ctg == 5:
    prc = 31
else:
    print("Not fund")
    prc=0
print("preço do produto é R$ %0.2f"%prc)"""
print("O seu pacote é o Tchau Pré-pago Prezão 15GB"
      "por R$29,99/mês.\n")
pln = input("Você utilizou todo o seu pacote (sim/não):")
pc_ad = 0
if pln == "sim":
    opc = input("Quer plano adicional?(s/n)\n")

    if opc == "sim":
        pc_ad = int(input("Quantidade de pacote de Franquia adicional de 300MB ="))

vl_mns = 29.99  + pc_ad * 7.99
print(f"O valor mensal do plano é R$ {vl_mns:.2f}.\n")

teste= input("tecle enter pra sair\n")
"""EXERCICIO 5"""

"""EXERCICIO 6"""

"""EXERCICIO 7"""

"""EXERCICIO 8"""

"""EXERCICIO 9"""
