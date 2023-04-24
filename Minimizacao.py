import AutomatoFD

class Minimizacao:

    def __init__(self):
        self.estados_equi = []
        self.matrix = [[]]
        self.flagEqui = bool

    def incializaMatrix(self, afd):
        finais = list(afd.finais)
        #criando a matriz de equivalencia
        self.matrix = [[0]*len(afd.estados)]*len(afd.estados)
        #inicialixando a lista com os estados nao utilizados e os estados esquivalentes
        for i in range(0, len(afd.estados)):          
            lista = []
            for j in range(0, len(afd.estados)):
                if(j>=i):
                    lista.append(2)
                else:
                    lista.append(0)
            self.matrix[i] = lista

        #inicializando os finais com nao finais
        for i in range(0, len(afd.estados)):
            for j in range(0, len(afd.estados)):
                    if((i in finais or j in finais) and self.matrix[i][j] != 2):
                        if i in finais and j in finais:
                            self.matrix[i][j] = 0
                        else:
                            self.matrix[i][j] = 1


    def estadosEquivalentes(self, afd, alfabeto):

        estados = list(afd.estados)

        if(self.matrix == [[]]):
            self.incializaMatrix(afd)

        for i in range(0, len(afd.estados)):
            for j in range(0, len(afd.estados)):
                if(self.matrix[i][j]==2 or self.matrix[i][j]==0):
                    break

                for k in range(0, len(alfabeto)):
                    if(afd.transicoes[estados[i], alfabeto[k]] != afd.transicoes[estados[j], alfabeto[k]] and
                     self.matrix[afd.transicoes[estados[i], alfabeto[k]]][afd.transicoes[estados[j], alfabeto[k]]]==1):
                        print(self.matrix)
                        self.matrix[i][j] = 1

        for i in range(0, len(afd.estados)):
            for j in range(0, len(afd.estados)):
                if(self.matrix[i][j]==0):
                    self.estados_equi.append((i,j))

        for i in range(0, len(afd.estados)):
            for j in range(0, len(afd.estados)):
                print(f'[{self.matrix[i][j]:^5}]', end='')
            print()

        return self.estados_equi

        
