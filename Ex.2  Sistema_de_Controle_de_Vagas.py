
CHOICES = [
    ("Registrar entrada de aluno", 1),
    ("Registrar saída de aluno", 2),
    ("Consultar alunos presentes", 3),
    ("Consultar vagas disponíveis", 4),
    ("Encerrar sistema", 5)
]

SetChoices = []

class Choice:
    def __init__(self, name, id):
        self.Name = name
        self.Id = id

class  Lab:
    def __init__(self):
        self.Vagas = 20
        self.Alunos = 0

    def Entrada(self):
        if self.Vagas > 0:self.Vagas -= 1; self.Alunos += 1; return True
        else: return False

    def Saida(self):
        if self.Alunos> 0: self.Vagas += 1; self.Alunos -= 1; return True
        else: return False

    def AlunosPresentes(self):
        print(f"Há {self.Alunos} aluno(s) no laboratório")

    def VagasRestantes(self):
            print(f"Há {self.Vagas} vaga(s) restante(s) no laboratório")


for index in range(len(CHOICES)):
    choice = Choice(CHOICES[index][0], CHOICES[index][1])
    SetChoices.append(choice)

Laboratorio = Lab()
Running = True
WaitingDecision = False

while Running:
    if WaitingDecision: break
    WaitingDecision = True
    print("\n===== LABORATÓRIO DE INFORMÁTICA =====")
    for index in range(len(SetChoices)):
        print(f"{SetChoices[index].Id} - {SetChoices[index].Name}")
    try:
        escolha = int(input("Digite a opção desejada: "))
    except ValueError:
        print(f"Erro: Valor digitado não suportado\nReiniciando o programa..."); WaitingDecision = False; continue
    if escolha <= 0 or escolha > len(SetChoices): print("Erro: Valor digitado não é uma opção configurada\nReiniciando o programa..."); WaitingDecision = False; continue
    if escolha == 1: 
        if Laboratorio.Entrada(): print("Entrada cadastrada!");
        else: print("Erro: Não há vagas disponíveis no laboratório")
        WaitingDecision = False
    elif escolha == 2:
        if Laboratorio.Saida(): print("Saída cadastrada!")
        else: print("Erro: Não há alunos cadastrados no laboratório")
        WaitingDecision = False
    elif escolha == 3: Laboratorio.AlunosPresentes(); WaitingDecision = False
    elif escolha == 4: Laboratorio.VagasRestantes(); WaitingDecision = False
    elif escolha == 5:
        print("Encerrando o programa...")
        Running = False
        break

    