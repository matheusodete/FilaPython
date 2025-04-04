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

    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        return None

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
        self.pilha_undo = Pilha()

    def adicionar_clientes(self, nomes):
        if not nomes:
            print("⚠ Nenhum cliente foi adicionado à fila.")
            return

        for nome in nomes:
            self.fila.enfileirar(nome)
        print("\n✅ Clientes adicionados à fila!")

    def atender_pulando(self, pular=0):
        if self.fila.esta_vazia():
            print("⚠ A fila está vazia. Não há clientes para atender.")
            return
        if pular >= self.fila.tamanho():
            print(f"❌ Não é possível pular {pular} pessoas. A fila tem apenas {self.fila.tamanho()} pessoas.")
            return
        for _ in range(pular):
            pessoa_pulada = self.fila.desenfileirar()
            self.fila.enfileirar(pessoa_pulada)
            print(f"⏭ Pulou: {pessoa_pulada}")

        cliente_atendido = self.fila.desenfileirar()
        print(f"\n🎯 Atendendo: {cliente_atendido}")

        self.historico.empilhar(cliente_atendido)
        self.pilha_undo.empilhar(cliente_atendido)

    def desfazer_atendimento(self):
        if self.pilha_undo.esta_vazia():
            print("❌ Nenhum atendimento para desfazer.")
            return

        cliente_ultimo = self.pilha_undo.desempilhar()
        print(f"🔄 Desfazendo atendimento de: {cliente_ultimo}")

        self.fila.itens.insert(0, cliente_ultimo)
        print(f"✅ {cliente_ultimo} foi recolocado no início da fila.")

    def mostrar_fila(self):
        print("\n📋 Fila atual:")
        fila_atual = self.fila.mostrar_fila()
        if not fila_atual:
            print("🚫 A fila está vazia.")
        else:
            for i, nome in enumerate(fila_atual, start=1):
                print(f"{i}. {nome}")

    def mostrar_historico(self):
        print("\n📚 Histórico de atendimentos:")
        if self.historico.esta_vazia():
            print("Nenhum atendimento realizado ainda.")
        else:
            historico_temp = []
            while not self.historico.esta_vazia():
                cliente = self.historico.desempilhar()
                historico_temp.append(cliente)
                print(f"- {cliente}")
            for cliente in reversed(historico_temp):
                self.historico.empilhar(cliente)

sistema = SistemaAtendimento()

clientes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo",
            "Fernanda", "Gustavo", "Helena", "Igor", "Julia"]
sistema.adicionar_clientes(clientes)

while True:
    sistema.mostrar_fila()
    escolha = input("\nDigite quantas pessoas deseja pular, 'desfazer' para reverter o último atendimento, ou 'sair' para encerrar: ")

    if escolha.lower() == 'sair':
        break
    if escolha.lower() == 'desfazer':
        sistema.desfazer_atendimento()
        continue
    if not escolha.isdigit():
        print("❌ Digite um número válido ou 'desfazer'.")
        continue
    pular = int(escolha)
    sistema.atender_pulando(pular)

print("\n✅ Atendimento finalizado.")
sistema.mostrar_historico()
