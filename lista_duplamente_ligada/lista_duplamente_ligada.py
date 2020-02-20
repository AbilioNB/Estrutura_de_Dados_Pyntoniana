class Celula:
    def __init__(self,conteudo):
        self.conteudo = conteudo
        self.proximo = None
        self.anterior = None

class ListaDuplamenteLigada:
    def __init__(self):
        self._inicio = None
        self._fim = None
        self._quantidade = 0


    @property
    def inicio(self):
        return self._inicio

    @property
    def fim(self):
        return self._fim

    @property
    def quantidade(self):
        return self._quantidade


    #Inserindo um primeiro elemento
    def inserir_lista_vazia(self,conteudo):
        celula = Celula(conteudo)
        self._inicio = celula
        self._fim = celula
        self._quantidade += 1


    #Agora vamos definir uma função para validar a posição buscada
    def validar_posicao(self,posicao):
        if 0 <= posicao < self.quantidade:
            return True
        raise NameError("Posição não encontrada")

    #Aqui localizamos a celula baseada na localização e retornamos
    def localziar_celula(self,posicao):
        self.validar_posicao(posicao)
        atual = self.inicio
        for aux in range(0,posicao):
            atual = atual.proximo
        return atual

    #Aqui retornamos a celula que foi buscada pelo meio da posição
    def retornar_celula(self,posicao):
        celula = self.retornar_celula(posicao)
        return celula.conteudo

