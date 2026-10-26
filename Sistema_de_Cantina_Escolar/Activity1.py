
EscolhasConfig = [# Configuração das escolhas
    ["Suco", 5.00, 1],
    ["Salgado", 7.00, 2],
    ["Sanduíche", 10.00, 3],
    ["Finalizar", None, 4],
]

Todas_Escolhas = []
wait_decision = False
running = True

# Inicialização das escolhas
class Escolhas:
    def __init__(self, name, price, id):
        self.Name = name
        self.Price = price or None
        self.ID = id
        self.Quantity = 0

for valor in EscolhasConfig:
    config = Escolhas(valor[0], valor[1], valor[2])
    Todas_Escolhas.append(config)

# Main Loop da loja
while running:
    if wait_decision: break
    print("\nMenu:")
    for i in range(len(Todas_Escolhas)):
        print(f"{Todas_Escolhas[i].ID} - {Todas_Escolhas[i].Name} - Preço: R${Todas_Escolhas[i].Price}" if Todas_Escolhas[i].Price != None else f"{Todas_Escolhas[i].ID} - {Todas_Escolhas[i].Name}")
    wait_decision = True
    try:
        selection = int(input("Digite o número da opção desejada: "))
    except ValueError:
        print("Erro: Valor não suportado foi digitado. Tente novamente")
        wait_decision = False;
        continue
    if selection <= 0 or selection > len(Todas_Escolhas): print("Erro: Escolha não existe ou não está cadastrada. Tente novamente."); wait_decision = False; continue
    if selection < 4:
        quantidade = int(input("Digite quantos produtos deseja comprar: "))
        Todas_Escolhas[selection - 1].Quantity += quantidade
        wait_decision = False
    else:
        print("Finalizando a compra...")
        total_price = 0
        for produto in Todas_Escolhas: # len(Todas_Escolhas)-1 para incluir apenas os produtos.
            total_price += (produto.Price * produto.Quantity if produto.Price != None else 0)
        print(f">>> Valor total da compra: R${total_price}")
        wait_decision = False