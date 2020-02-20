from estrutura_de_dados.lista_ligada.lista_ligada import *


#Aqui vamos definir a classe das  lanchonetes que nosso entregador tem que passar
class Lanchonete:
    def __init__(self,nome,endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return "{} \n {}".format(self.nome,self.endereco)




def main():

    lanchonete1 = Lanchonete("Pizza Hut","Rua Floriano peixto , 256")
    lanchonete2 = Lanchonete("MacDonalds","Rua Desembargador Mario Covas , 446")
    lanchonete3 = Lanchonete("Habbi's","Rua da Lama  , 786")
    lanchonete4 = Lanchonete("Don Pablitto","Rua da Gloria  , 151")
    lanchonete5 = Lanchonete("Bob's","Rua da Pena  , 312")
    lanchonete6 = Lanchonete("Self ","Rua Epaminondas  , 515")

    #Criamos a lista
    lista = ListaLigada()



    #Inserindo o primeiro elemento
    lista.inserir_no_inicio(lanchonete1)
    lista.inserir_no_inicio(lanchonete2)
    print(lista.quantidade)

    lista.imprimir()
    #lista.remover_do_inicio()
    #lista.imprimir()
    lista.remover_de_n_posicao(0)
    lista.imprimir()




main()