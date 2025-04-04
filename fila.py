class Pilha:
    def __init__(self):
        self.itens = []
    def empilhar(self, item):
        self.itens.append(item)
    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None
    def esta_vazia(self):
        return len(self.itens) == 0

class Fila:
    def __init__(self):
        self.itens = []
    def enfileirar(self, item):
        self.itens.append(item)
    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
        return None
    def esta_vazia(self):
        return len(self.itens) == 0
    def tamanho(self):
        return len(self.itens)
    def mostrar_fila(self):
        return self.itens.copy()

class SistemaAtendimento:
    def __init__(self):
        self.fila = Fila()
        self.historico = Pilha()
    def adicionar_clientes(self, nomes):
        for nome in nomes:
            self.fila.enfileirar(nome)
    def atender_pulando(self, pular=0):
        if self.fila.tamanho() == 0:
            print("Fila vazia. Ninguém para atender.")
            return
        if pular >= self.fila.tamanho():
            print(f"Não é possível pular {pular} pessoas. Fila tem apenas {self.fila.tamanho()} pessoas.")
            return
        for _ in range(pular):
            pessoa_pulada = self.fila.desenfileirar()
            self.fila.enfileirar(pessoa_pulada)
            print(f"Pulou: {pessoa_pulada}")
        cliente_atendido = self.fila.desenfileirar()
        print(f"\n🎯 Atendendo: {cliente_atendido}")
        self.historico.empilhar(cliente_atendido)

    def mostrar_fila(self):
        print("\n📋 Fila atual:")
        for i, nome in enumerate(self.fila.mostrar_fila(), start=1):
            print(f"{i}. {nome}")

    def mostrar_historico(self):
        print("\n📚 Histórico de atendimentos:")
        if self.historico.esta_vazia():
            print("Nenhum atendimento realizado ainda.")
        else:
            while not self.historico.esta_vazia():
                print(f"- {self.historico.desempilhar()}")


sistema = SistemaAtendimento()

clientes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo",
            "Fernanda", "Gustavo", "Helena", "Igor", "Julia"]

sistema.adicionar_clientes(clientes)

while True:
    sistema.mostrar_fila()
    escolha = input("\nDigite quantas pessoas você quer pular (ou 'sair' para encerrar): ")

    if escolha.lower() == 'sair':
        break
    if not escolha.isdigit():
        print("Digite um número válido.")
        continue
    pular = int(escolha)
    sistema.atender_pulando(pular)

print("\nAtendimentos finalizados.")
sistema.mostrar_historico()
