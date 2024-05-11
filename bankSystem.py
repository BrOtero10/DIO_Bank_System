menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu).lower()

    if opcao == "d":
        valor_depositado = float(input("Digite o valor a ser depositado: "))
        if valor_depositado <= 0:
            print("\nValor inválido. Por favor, entre com um valor positivo.")
        else:
            saldo += valor_depositado
            extrato += f"\n\nDepósito: R${valor_depositado:.2f}\nSaldo: R${saldo:.2f}"
            print(f"\nValor de R${valor_depositado:.2f} depositado com sucesso!")

    elif opcao == "s":
        if numero_saques < 3:
            saque = float(input("Digite o valor do saque: "))
            if saque > 500 :
                print("\nValor inálido. O limite do valor de saque é R$500,00")
            elif saque <= 0:
                print("\nValor inválido. Por favor, entre com um valor positivo.")
            elif saque > saldo:
                print("\nSaldo insuficiente.")
            else:
                saldo -= saque
                numero_saques += 1
                extrato += f"\n\nSaque: R${saque:.2f}\nSaldo: R${saldo:.2f}"
                print(f"\nSaque de R${saque:.2f} realizado!")
        else:
            print("\nNúmero diário máximo de saques atingido.")
    elif opcao == "e":
        print(extrato)
    elif opcao == "q":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")