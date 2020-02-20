#Nesse arquivo definimos as funções utilizados la na rota do nosso entregador
import datetime
#Representa uma celula da nossa lista
class Celula:
    def __init__(self,conteudo):
        self.conteudo = conteudo
        self.proximo = None



# Aqui temos a definição da propria lista

class ListaLigada:
    def __init__(self):
        self._inicio = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio

    @property
    def quantidade(self):
        return self._quantidade



    #Vamos começar inserindo no inicio da lista
    def inserir_no_inicio(self,conteudo):
        #Definimos uma primeira celula
        celula = Celula(conteudo)
        #Informamos que nao existe outra depois
        celula.proximo = self._inicio
        #Definimos que a celula definida é a primeira da lista
        self._inicio = celula
        #Atualizamos a quantidade
        self._quantidade += 1

    #Inseri na Nzima posição
    def inserir_n_posicao(self,posicao,conteudo):
        if posicao == 0:
            self.inserir_no_inicio(conteudo)
            return
        celula = Celula(conteudo)
        esquerda = self._celula(posicao-1)
        celula.proximo = esquerda.proximo
        esquerda.proximo = celula
        self._quantidade +=1
    #Função particular da celula para retornar o proximo
    def _celula(self,posicao):
        self._validar_posicao(posicao)
        atual = self.inicio
        for aux in range(0,posicao):
            atual = atual.proximo
        return atual

    #Função para validar se aquela posição está presente
    def _validar_posicao(self,posicao):
        if 0 <= posicao < self.quantidade:
            return True
        raise NameError("Posição {} invalida".format(posicao))
        #raise é utilizado para lançar execções

    #Função que imprimi a lista de entregas
    def imprimir(self):
        celula_atual = self.inicio
        for aux in range(0,self.quantidade):
            print(celula_atual.conteudo)
            celula_atual = celula_atual.proximo

    #Remove o primeiro elemento
    def remover_do_inicio(self):
        removido = self.inicio
        self._inicio = removido.proximo
        removido.proximo = None
        self._quantidade -= 1
    #Remove o item da Nzima posição
    def remover_de_n_posicao(self,posicao):
        if posicao == 0:
            return self.remover_do_inicio()
        esquerda = self._celula(posicao-1)
        removido = esquerda.proximo
        esquerda.proximo = removido.proximo
        removido.proximo = None
        self._quantidade -= 1
    #Identifica o item baseado em sua posição
    def pos_item(self,posicao):
        self._validar_posicao(posicao)
        celula = self._celula(posicao)
        return  celula.conteudo