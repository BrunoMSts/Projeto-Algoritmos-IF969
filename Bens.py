import textwrap

class Bem:

    def __init__(self, codTipoBem, descTipoBem, descDetalhadaBem, valorBem):
        self.__codTipoBem = codTipoBem
        self.__descTipoBem = descTipoBem
        self.__descDetalhadaBem = descDetalhadaBem
        self.__valorBem = valorBem


    def __str__(self):
        formatado = f'''
        {self.getCodigoDoTipoDeBem()} --- {self.getDescricaoDoTipoDeBem()} --- R${self.getValorDoBem()}
        Descrição: {textwrap.shorten(self.getDescricaoDetalhadaDoBem(), width=80)}'''
        return formatado


    def __repr__(self):
        return self.__str__()
  
    def setCodigoDoTipoDeBem(self, novo):
        self.__codTipoBem = novo
    def setDescricaoDoTipoDeBem(self, novo):
        self.__descTipoBem = novo
    def setDescricaoDetalhadaDoBem(self, novo):
        self.__descDetalhadaBem = novo
    def setValorDoBem(self, novo):
        self.__valorBem = novo

    def getCodigoDoTipoDeBem(self): return self.__codTipoBem
    def getDescricaoDoTipoDeBem(self): return self.__descTipoBem
    def getDescricaoDetalhadaDoBem(self): return self.__descDetalhadaBem
    def getValorDoBem(self): return self.__valorBem
