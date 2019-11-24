from Candidatos import *
from Bens import *
from Lista import *
from Leitor import *

class Controle:
    def __init__(self):
        self.candidatos = Lista()
        self.candidatosOrdenados = Lista()
        self.dicFiltrado = {}
        self.candidatosEstado = {}
        self.candidatosNomes = {}
        self.candidatosBens = {}
        self.candidatosData = {}
        self.bensCarregados = False

    def carregaCandidatos(self, arquivo): #APROXIMADAMENTE 40 - 60 SEGUNDOS PRA CARREGAR
        arquivo = ler(arquivo)
        for i in range(1, len(arquivo)):
            if 'DT_GERACAO' not in arquivo[i]:
                candidato = Candidato(arquivo[i][2], arquivo[i][10], arquivo[i][13], arquivo[i][14],
                                      arquivo[i][17], arquivo[i][15], arquivo[i][16], arquivo[i][20],
                                      arquivo[i][18], arquivo[i][27], arquivo[i][29], arquivo[i][28],
                                      arquivo[i][49], arquivo[i][50], arquivo[i][38], arquivo[i][42],
                                      arquivo[i][44], arquivo[i][46], arquivo[i][35], arquivo[i][37],
                                      arquivo[i][25], arquivo[i][23], arquivo[i][55])
                self.candidatosData[arquivo[i][38]] = candidato
                self.candidatosNomes[arquivo[i][17]] = candidato
                self.candidatos.anexar(candidato)
        

    def carregaBens(self, arquivo): #APROXIMADAMENTE 30 SEGUNDOS PRA CARREGAR
        if len(self.candidatos) > 0:
            arquivo = ler(arquivo)
            bens = {}
            for i in range(1, len(arquivo)): 
                bens[arquivo[i][11]] = []

            for i in range(1, len(arquivo)):
                bemCandidato = Bem(arquivo[i][13], arquivo[i][14], arquivo[i][15], arquivo[i][16])
                bens[arquivo[i][11]].append(bemCandidato)

            for candidato in self.candidatos:
                if candidato.getIdDoCandidato() in bens:
                    candidato.setListaDeBens(bens[str(candidato.getIdDoCandidato())])
                    self.candidatosBens[len(candidato.getListaDeBens())] = candidato
            self.bensCarregados = True
            return self.bensCarregados
                
        else:
            raise ValueError('Você precisa carregar os candidatos primeiro')

    def filtrar(self, partido, uf, municipioNascimento, cargo, valorBens, pleito):
        listaAux = []
        for candidato in self.candidatos:
            valor = candidato.getValorTotalDeclarado()
            if (candidato.getSiglaDoPartido() == partido) and (candidato.getSiglaDaUf() == uf) and (candidato.getNomeDoMunicipioDeNascimento() == municipioNascimento) and (candidato.getDescricaoDoCargo() == cargo) and (valor > valorBens) and (candidato.getSituacaoDoCandidatoPosPleito() == pleito):
                listaAux.append(candidato)
        return listaAux

    def OrdemAlfabeticaCrescente(self):
        a = self.candidatosNomes.copy()
        for i in range(len(a)):
            print(a[min(a)])
            a.pop(min(a))


    def OrdemAlfabeticaDecrescente(self):
        a = self.candidatosNomes.copy()
        for i in range(len(a)):
            print(a[max(a)])
            a.pop(max(a))

    def TotalDeBensCrescente(self):
        a = self.candidatosBens.copy()
        for i in range(len(a)):
            print(a[min(a)])
            a.pop(min(a))

    def TotalDeBensDecrescente(self):
        a = self.candidatosBens.copy()
        for i in range(len(a)):
            print(a[max(a)])
            a.pop(max(a))

    def DataDeNascimentoCrescente(self):
        a = self.candidatosData.copy()
        for i in range(len(a)):
            print('Data Nascimento :',min(a),'\n',a[min(a)])
            a.pop(min(a))

    def DataDeNascimentoDecrescente(self):
        a = self.candidatosData.copy()
        for i in range(len(a)):
            print('Data Nascimento :',max(a),'\n',a[max(a)])
            a.pop(max(a))
        
    def separaTudo(self):
        for candidato in self.candidatos:
            if candidato.getSiglaDaUf() not in self.candidatosEstado:
                self.candidatosEstado[candidato.getSiglaDaUf()] = []
            self.candidatosEstado[candidato.getSiglaDaUf()].append(candidato)
        return self.candidatosEstado

    def media(self, parametro): #UF,CARGO,PARTIDO, OCUPAÇÃO ou DATA DE NASCIMENTO
        if self.bensCarregados:
            lista = {}
            sumBens = 0
            media = ''
            for candidato in self.candidatos:
                if parametro == candidato.getSiglaDaUf():
                    if candidato.getIdDoCandidato() not in lista and type(candidato.getListaDeBens()) != str:
                        lista[candidato.getIdDoCandidato()] = []
                    if type(candidato.getListaDeBens()) != str:
                        lista[candidato.getIdDoCandidato()].append(candidato.getListaDeBens())
                        sumBens += len(candidato.getListaDeBens())

                elif parametro == candidato.getDescricaoDoCargo():
                    if candidato.getIdDoCandidato() not in lista and type(candidato.getListaDeBens()) != str:
                        lista[candidato.getIdDoCandidato()] = []
                    if type(candidato.getListaDeBens()) != str:
                        lista[candidato.getIdDoCandidato()].append(candidato.getListaDeBens())
                        sumBens += len(candidato.getListaDeBens())

                elif parametro == candidato.getNomeDoPartido() and type(candidato.getListaDeBens()) != str:
                    if candidato.getIdDoCandidato() not in lista:
                        lista[candidato.getIdDoCandidato()] = []
                    if type(candidato.getListaDeBens()) != str:
                        lista[candidato.getIdDoCandidato()].append(candidato.getListaDeBens())
                        sumBens += len(candidato.getListaDeBens())

                elif parametro == candidato.getDataDeNascimento() and type(candidato.getListaDeBens()) != str:
                    if candidato.getIdDoCandidato() not in lista:
                        lista[candidato.getIdDoCandidato()] = []
                    if type(candidato.getListaDeBens()) != str:
                        lista[candidato.getIdDoCandidato()].append(candidato.getListaDeBens())
                        sumBens += len(candidato.getListaDeBens())

                elif parametro == candidato.getDescricaoDaOcupacao() and type(candidato.getListaDeBens()) != str:
                    if candidato.getIdDoCandidato() not in lista:
                        lista[candidato.getIdDoCandidato()] = []
                    if type(candidato.getListaDeBens()) != str:
                        lista[candidato.getIdDoCandidato()].append(candidato.getListaDeBens())
                        sumBens += len(candidato.getListaDeBens())

            media = sumBens / len(lista)

            return print(f'Média: {media:.2f}')
        raise ValueError('Carregue os Bens dos Candidatos Primeiro')

    def remove(self, criterio):
        for candidato in self.candidatos:
            if candidato.getSituacaoDaCandidatura() == criterio or candidato.getSituacaoDoCandidatoPosPleito() == criterio or candidato.getNomeDoCandidato() == criterio or candidato.getSiglaDaUf() == criterio:
                i = self.candidatos.indice(candidato)
                self.candidatos.selecionar(i)
        return self.candidatos
                
if __name__ == '__main__':
    print('''
    Melhor fazer tudo direto do terminal do python é mais rápido para verificar as funções
    Os candidatos levam em média 80 segundos para serem carregados
    Carregar os bens leva em torno de 30 - 40 segundos
    O print leva em torno de 2:30 - 3:30 minutos pra iniciar
                                                
                                            ----- Funções -----
            importar o modulo controle :                 from Controle import *
            iniciar o modulo controle :                  c = Controle()
            carregando candidatos :                      c.carregaCandidatos('candidatos')
            carregando os bens :                         c.carregaBens('bens')

            Buscar candidato pelo indice :               c.candidatos[indice]
            Ver bens de um candidato :                   c.candidatos[indice].getListaDeBens() #FUNÇÕES get DO ARQUIVO CANDIDATO FUNCIONAM AQ, ASSIM COMO AS FUNÇÕES get dos Bens
            Criar um Objeto bem pra poder ser incluido : objetoBem = Bem(codTipoBem, descTipoBem, descDetalhadaBem, valorBem)
            Incluir um bem :                             c.canditatos[indice].incluirBem(objetoBem)
            Imprime candidatos em ordem Alfabética :     c.OrdemAlfabeticaCrescente() / c.OrdemAlfabeticaDecrescente()
            Imprime candidatos por total de bens :       c.TotalDeBensCrescente() / c.TotalDeBensDecrescente()
            Imprime candidatos Data de Nascimento :      c.DataDeNascimentoCrescente() / c.DataDeNascimentoDecrescente()
            Filtrar um candidato :                       c.filtrar(partido, uf, municipioNascimento, cargo, valorBens, pleito)
            Separa Candidatos por Estado :               c.separaTudo()
            tira a media de determinado parametro :      c.media() #PARAMETRO: UF ou DESCRIÇÃO DO CARGO ou DATA DE NASCIMENTO ou NOME DO PARTIDO ou OCUPAÇÃO
            remover um candidato :                       c.remove() #PARAMETRO: NOME DO CANDIDATO, UF, SITUAÇÃO POS PLEITO ou SITUAÇÃO CANDIDATURA 


            possui varias outras funções no entanto coloquei as mais importantes para acelerar a correção

    ''')
