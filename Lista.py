class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None
        self.ant = None

class Lista:
    def __init__(self, aux=None, cabeca=None):
        self.cabeca = cabeca
        self.tamanho = 0
        self.aux = str(aux)
        #'b <-> r <-> u <-> n <-> o'
        if aux == None:
            pass
        else:
            for i in self.aux:
                if self.cabeca:
                    pointer = self.cabeca
                    while pointer.prox:
                        pointer.prox.ant = pointer
                        pointer = pointer.prox
                    pointer.prox = No(i)
                    pointer.prox.ant = pointer
                    self.cabeca.ant = pointer.prox
                else:
                    self.cabeca = No(i)
                self.tamanho += 1


    def indice(self, elem):
        pointer = self.cabeca
        index = 0
        while pointer:
            if pointer.dado == elem:
                return index
            else:
                pointer = pointer.prox
                index += 1
        raise ValueError('Item não está na Lista')
        
    def anexar(self, elem):
        if self.cabeca:
            pointer = self.cabeca
            while pointer.prox:
                pointer.prox.ant = pointer
                pointer = pointer.prox
            pointer.prox = No(elem)
            pointer.prox.ant = pointer
            self.cabeca.ant = pointer.prox
        else:
            self.cabeca = No(elem)
        self.tamanho += 1


    def selecionar(self, indice=None):
        pointer = self.cabeca
        if not indice or indice == 0:
            self.cabeca = pointer.prox
            while pointer.prox:
                pointer = pointer.prox
            self.cabeca.ant = pointer
        else:
            for i in range(indice):
                if pointer:
                    pointer = pointer.prox #[1,2,3,4,5]
            if pointer:
                pointer.ant.prox = pointer.prox
                pointer.prox.ant = pointer.ant
        self.tamanho -= 1

    def inserir(self, indice, elem):
        pointer = self.cabeca
        aux = None
        if indice == 0:
            self.cabeca = No(elem)
            self.cabeca.prox = pointer
            pointer.ant = self.cabeca
            while pointer.prox:
                pointer = pointer.prox
            self.cabeca.ant = pointer
        else:
            for i in range(indice-1):
                if pointer:
                    pointer = pointer.prox
            if pointer:
                aux = pointer.prox
                pointer.prox = No(elem)
                pointer.prox.ant = pointer
                pointer.prox.prox = aux
            else:
                raise IndexError('Indice não existente')

    def concatenar(self, lista):
        pointer = lista.cabeca
        pointer.ant = self.cabeca.ant
        while pointer:
            self.cabeca.ant.prox = pointer
            pointer = pointer.prox
            self.cabeca.ant = self.cabeca.ant.prox   
        self.tamanho += lista.tamanho
        del lista.cabeca      

    def __str__(self):
        self.s = '"'
        pointer = self.cabeca
        if pointer:
            while pointer:
                self.s += str(pointer.dado) + ','
                pointer = pointer.prox
            return self.s[:len(self.s)-1] + '"'
        self.s = ''
        return self.s

            
    def __repr__(self):
        try:
            return 'ListaDupla[(' + self.__str__() + ')]'
        except AttributeError:
            return 'Está faltando o Método'

    def __getitem__(self, indice):
        pointer = self.cabeca
        for i in range(indice):
            if pointer:
                pointer = pointer.prox
        if pointer:
            return pointer.dado
        else:
            raise IndexError('Index fora de alcance')

    def __setitem__(self, indice, elem):
        pointer = self.cabeca
        for i in range(indice):
            if pointer:
                pointer = pointer.prox
        if pointer:
            pointer.dado = elem
        else:
            raise IndexError('Index fora de alcance')
    def __len__(self):
        return self.tamanho

class Ponteiro(Lista):
    def __init__(self, no):
        self.no = no
        self.passo = self.no.cabeca
    
    def __iter__(self):
        self.atual = self.passo
        return self
    
    def __next__(self):
        self.primeiro = self.atual
        if self.atual:
            self.atual = self.atual.prox
            return self.primeiro.dado
        else:
            raise StopIteration