saldo = 0

extrato = [f"\nSeu saldo inicial é de: R$ {saldo:.2f}\n"]

limite_saque = 500

limite_saque_restante = 3

def menu():
    print("Selecione uma opção:")
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = int(input())

    if opcao == 1:
        sacar()
    elif opcao == 2:
        depositar()
    elif opcao == 3:
        mostrar_extrato()
    elif opcao == 4:
        print("Obrigado por utilizar o Python Bank!")
        quit()
    else :
        print("Opcão inválida")
        

def sacar():
    global saldo, extrato, limite_saque_restante

    if limite_saque_restante <= 0:
        print("Você atingiu o limite de saques diários.")
        return
    
    saque = float(input("Qual o valor que deseja sacar? "))
    if saque > limite_saque:
        print("Limite de saque excedido")
    elif saque > saldo:
        print("Saldo insuficiente")
    elif saque <= 0:
        print("Valor inválido")
    else:
        saldo -= saque
        limite_saque_restante -= 1
        extrato.append(f"\nSaque de: R$ {saque:.2f}\n Seu novo saldo é de: R${saldo:.2f}\n")
        print(f"Seu novo saldo é de: R${saldo:.2f}")
        
def depositar():
    global saldo, extrato

    deposito = float(input("Qual o valor que deseja depositar? "))
    if deposito <= 0:
        print("Valor inválido")
    else:
        saldo += deposito
        extrato.append(f"\nDeposito de: R$ {deposito:.2f}\n Seu novo saldo é de: R$ {saldo:.2f}\n")
        print(f"Seu novo saldo é de: R$ {saldo:.2f}")

def mostrar_extrato():
    global extrato

    print("Seu extrato: ")
    for i in extrato:
        print(i)

while True:
    menu()
