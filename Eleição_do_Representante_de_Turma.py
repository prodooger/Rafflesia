import math

voto_config = [
    ["Ana", 1],
    ["Bruno", 2],
    ["Carlos", 3],
    ["branco", 4],
    ["resultado", 5],
    ["encerrar", 6],
]

items = []
wait_decision = False
running = True
bigger_name = ""
bigger = -math.inf
tie = False
tie_names = []
eleito = True

class registro:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.votos = 0
        self.porcentagem = 0

for valor in voto_config:
    config = registro(valor[0], valor[1])
    items.append(config)

while running:
    if wait_decision: break
    print("\nMenu da votação - Opções:")
    for i in range(len(items)):
        print(f"{items[i].id} - {items[i].name}")
    wait_decision = True
    try:
        selection = int(input("Digite o número da opção desejada: "))
    except ValueError:
        print("Erro: Valor não suportado foi digitado. Tente novamente")
        wait_decision = False;
        continue
    if selection <= 0 or selection > len(items): print("Erro: Escolha não existe ou não está cadastrada. Tente novamente."); wait_decision = False; continue
    if selection <= 4:
        items[selection - 1].votos += 1
        wait_decision = False
        continue
    elif selection == 5:
        print(f"> RESULTADO PARCIAL <\n{items[0].name} - Votos: {items[0].votos}\n{items[1].name} - Votos: {items[1].votos}\n{items[2].name} - Votos: {items[2].votos}\nEm {items[3].name} - Votos: {items[3].votos}")
        wait_decision = False
        continue
    elif selection == 6:
        print("Encerrando a votação...")
        votos_total = 0
        votos_reais = 0
        for index in range(len(items)):
            votos_total += items[index].votos
            if items[index].name != "branco":
                votos_reais += items[index].votos
        for index in range(len(items)):
            if items[index].id <= 3:
                items[index].porcentagem = math.ceil(((items[index].votos / votos_reais) * 100)) if votos_reais > 0 else 0
                if items[index].votos > bigger:
                    bigger = items[index].votos
                    bigger_name = items[index].name
                elif items[index].votos == bigger:
                    tie = True
            elif items[index].id == 4:
                items[index].porcentagem = math.ceil(((items[index].votos / votos_total) * 100)) if votos_total > 0 else 0
        print(f"\n>>> RESULTADOS FINAIS DA VOTAÇÃO <<<\n--{items[0].name}: {items[0].votos} votos - {items[0].porcentagem}%\n--{items[1].name}: {items[1].votos} votos - {items[1].porcentagem}%\n--{items[2].name}: {items[2].votos} votos - {items[2].porcentagem}%\n--Em {items[3].name}: {items[3].votos} votos - {items[3].porcentagem}%")
        if tie:
            if items[0].votos == items[1].votos and items[1].votos == items[2].votos:
                tie_names.append(items[0].name)
                tie_names.append(items[1].name)
                tie_names.append(items[2].name)
            elif items[1].votos == items[2].votos:
                tie_names.append(items[1].name)
                tie_names.append(items[2].name)
            elif items[0].votos == items[2].votos:
                tie_names.append(items[0].name)
                tie_names.append(items[2].name)
            elif items[0].votos == items[1].votos:
                tie_names.append(items[0].name)
                tie_names.append(items[1].name)
            print(f"Houve um empate entre os candidatos!")
            for index in range(len(tie_names)):
                print(f"{tie_names[index]}")
            print("Empataram.")
            for index in range(len(tie_names)):
                if tie_names[index] == bigger_name:
                    print(f"Votos totais da eleição: {votos_total}")
                    print("Como os candidatos com mais votos empataram, ninguém foi eleito...")
                    eleito = False
            if eleito:
                print(f"Votos totais da eleição: {votos_total}")
                print(f"Vencedor da eleição: {bigger_name}")
        else:
            print(f"Votos totais da eleição: {votos_total}")
            print(f"Vencedor da eleição: {bigger_name}")
        break