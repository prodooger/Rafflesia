
CHOICES = [
    ("Consultar saldo", 1),
    ("Realizar depósito", 2),
    ("Realizar saque", 3),
    ("Consultar quantidade de operações", 4),
    ("Encerrar", 5)
]

SetChoices = []

class Choice:
    def __init__(self, name, id):
        self.Name = name
        self.Id = id

class Clientes:
    def __init__(self):
        self.Saldo = 500.00
        self.Saques = 0
        self.Depositos = 0

    def Depositar(self):
        try: quantidade = float(input("Digite o valor que deseja depositar"))
        except ValueError: print("Erro: Valor não suportado. Dica: Use '.' ao ínves da vírgula para decimais"); return
        if quantidade > 0: self.Saldo += quantidade; self.Depositos += 1
        else: print("Depósito não efetuado: A quantidade desejada é nula ou negativa")

    def Sacar(self):
        try: quantidade = float(input("Digite o valor que deseja sacar"))
        except ValueError: print("Erro: Valor não suportado. Dica: Use '.' ao ínves da vírgula para decimais"); return
        if quantidade < self.Saldo and quantidade > 0: self.Saldo -= quantidade; self.Saques += 1
        else: print("Saque não efetuado: A quantidade desejada ultrapassa o saldo, é nula ou negativa")

    def ConsultarSaldo(self):
        print(f"Saldo disponível: {self.Saldo}")

    def ConsultarOperations(self):
            print(f"Saques realizados: {self.Saques}\nDepósitos realizados: {self.Depositos}")


for index in range(len(CHOICES)):
    choice = Choice(CHOICES[index][0], CHOICES[index][1])
    SetChoices.append(choice)

Cliente = Clientes()
Running = True
WaitingDecision = False

while Running:
    if WaitingDecision: break
    WaitingDecision = True
    print("\n===== CAIXA ELETRÔNICO =====")
    for index in range(len(SetChoices)):
        print(f"{SetChoices[index].Id} - {SetChoices[index].Name}")
    try:
        escolha = int(input("Digite a opção desejada: "))
    except ValueError:
        print(f"Erro: Valor digitado não suportado\nReiniciando o programa..."); WaitingDecision = False; continue
    if escolha <= 0 or escolha > len(SetChoices): print("Erro: Valor digitado não é uma opção configurada\nReiniciando o programa..."); WaitingDecision = False; continue
    if escolha == 1: Cliente.ConsultarSaldo(); WaitingDecision = False
    elif escolha == 2: Cliente.Depositar(); WaitingDecision = False
    elif escolha == 3: Cliente.Sacar(); WaitingDecision = False
    elif escolha == 4: Cliente.ConsultarOperations(); WaitingDecision = False
    elif escolha == 5:
        print("Encerrando o programa...")
        Running = False
        break

    