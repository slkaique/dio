menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 2

while True:
    opcao = input(menu).strip().lower()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: ").replace(",", "."))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("⚠️ Operação falhou! O valor informado deve ser positivo.")
        except ValueError:
            print("⚠️ Valor inválido! Informe um número, como 100 ou 100.50.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: ").replace(",", "."))

            if valor <= 0:
                print("⚠️ Operação falhou! O valor do saque deve ser positivo.")
            elif valor > saldo:
                print("⚠️ Operação falhou! Saldo insuficiente.")
            elif valor > limite:
                print(f"⚠️ Operação falhou! O valor máximo por saque é R$ {limite:.2f}.")
            elif numero_saques >= LIMITE_SAQUES:
                print(f"⚠️ Operação falhou! Limite de {LIMITE_SAQUES} saques diários atingido.")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        except ValueError:
            print("⚠️ Valor inválido! Informe um número, como 100 ou 100.50.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==============================\n")

    elif opcao == "q":
        print("✅ Operação finalizada. Obrigado por utilizar nosso sistema!")
        break

    else:
        print("⚠️ Opção inválida! Por favor, selecione uma das opções do menu.")
