from estrutura_de_dados.lista_duplamente_ligada.lista_duplamente_ligada import *

class restaurante:
    def __init__(self,nome,endereco):
        self.nome = nome
        self.endereco = endereco


    def __repr__(self):
        return print("Nome:{}\n Endereco :{}".format(self.nome,self.endereco))






def main():

        restaurante1 = restaurante("Madeiros","Reoublica do libado,200")
        restaurante2 = restaurante("Skillus","Av Agamenom Magalhaes,300")
        restaurante3 = restaurante("Macunaima","Praça da Liberdade,400")
        restaurante4 = restaurante("Galletus","Avenida Recife,550")


        lista_dup = ListaDuplamenteLigada()
        print(lista_dup.quantidade)
        lista_dup.inserir_lista_vazia(restaurante1)
        print(lista_dup.quantidade)






main()