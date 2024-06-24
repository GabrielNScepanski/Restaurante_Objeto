class Restaurante:
    def _init_(self, nome, tipo_Prato):
        self.nome = nome
        self.tipo_Prato = tipo_Prato
        self.avaliacoes = []
        self.ativo = True

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def exibir_avaliacoes(self):
        if not self.avaliacoes:
            print("Sem avaliações.")
        for avaliacao in self.avaliacoes:
            print(avaliacao)

    def ativar(self):
        self.ativo = True

    def desativar(self):
        self.ativo = False

    def _str_(self):
        estado = "Ativo" if self.ativo else "Inativo"
        return f"Restaurante: {self.nome} - Tipo de Prato: {self.tipo_Prato} - Estado: {estado}"