
CHOICES = [
    ("Emprestar Um Livro", 1),
    ("Devolver Um Livro", 2),
    ("Consultar Livros", 3),
    ("Consultar Livros Emprestados", 4),
    ("Encerrar Programa", 5)
]

SetChoices = []

class Choice:
    def __init__(self, name, id):
        self.Name = name
        self.Id = id

class Library:
    def __init__(self):
        self.Livros = 10
        self.Emprestados = 0

    def Emprestar(self):
        self.Livros -= 1; self.Emprestados += 1

    def Devolver(self):
        self.Livros += 1; self.Emprestados -= 1

    def ConsultaLivros(self):
        print(f"Livros disponíveis: {self.Livros}")

    def ConsultaEmprestimo(self):
            print(f"Livros emprestados: {self.Emprestados}")


for index in range(len(CHOICES)):
    choice = Choice(CHOICES[index][0], CHOICES[index][1])
    SetChoices.append(choice)

Biblioteca = Library()
Running = True
WaitingDecision = False

while Running:
    if WaitingDecision: break
    WaitingDecision = True
    print("\n===== BIBLIOTECA ESCOLAR =====")
    for index in range(len(SetChoices)):
        print(f"{SetChoices[index].Id} - {SetChoices[index].Name}")
    try:
        escolha = int(input("Digite a opção desejada: "))
    except ValueError:
        print(f"Erro: Valor digitado não suportado\nReiniciando o programa..."); WaitingDecision = False; continue
    if escolha <= 0 or escolha > len(SetChoices): print("Erro: Valor digitado não é uma opção configurada\nReiniciando o programa..."); WaitingDecision = False; continue
    if escolha == 1: Biblioteca.Emprestar(); WaitingDecision = False
    elif escolha == 2: Biblioteca.Devolver(); WaitingDecision = False
    elif escolha == 3: Biblioteca.ConsultaLivros(); WaitingDecision = False
    elif escolha == 4: Biblioteca.ConsultaEmprestimo(); WaitingDecision = False
    elif escolha == 5:
        print("Encerrando o programa...")
        Running = False
        break

    