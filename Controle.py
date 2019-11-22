from Candidatos import *
from Bens import *
from Lista import *
from Leitor import *

class Controle:
    def __init__(self):
        self.candidatos = Lista()
        self.candidatosOrdenados = Lista()
        self.dicFiltrado = {}

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
                

        else: raise ValueError('Você precisa carregar os candidatos primeiro')

    def filtrar(self, partido, uf, municipioNascimento, cargo, valorBens, pleito):
        listaAux = []
        for candidato in self.candidatos:
            valor = candidato.getValorTotalDeclarado()
            if (candidato.getSiglaDoPartido() == partido) and (candidato.getSiglaDaUf() == uf) and (candidato.getNomeDoMunicipioDeNascimento() == municipioNascimento) and (candidato.getDescricaoDoCargo() == cargo) and (valor > valorBens) and (candidato.getSituacaoDoCandidatoPosPleito() == pleito):
                listaAux.append(candidato)
        return listaAux

    def comparaOrdemAlfabeticaCrescente(self):
        listaNomes = []
        for candidato in self.candidatos:
            listaNomes.append(candidato.getNomeDoCandidato())
        listaNomes.sort()
        return listaNomes

    def comparaOrdemAlfabeticaDecrescente(self):
        listaNomes = []
        for candidato in self.candidatos:
            listaNomes.append(candidato.getNomeDoCandidato())
        listaNomes.sort(reverse=True)
        return listaNomes

    def comparaTotalDeBensCrescente(self):
        listaAux =self.comparaOrdemAlfabeticaCrescente()
        for i in range(len(self.candidatos)):
            if len(self.candidatos[i].getListaDeBens()) < len(self.candidatos[i+1].getListaDeBens()):
                listaAux.inserir(i, listaAux[i+1])
            else:
                listaAux.inserir(i, listaAux[i])
        return listaAux

    def comparaTotalDeBensDecrescente(self):
        listaAux = self.comparaOrdemAlfabeticaCrescente()
        for i in range(len(listaAux)-1):
            if len(listaAux[i].getListaDeBens()) < len(listaAux[i+1].getListaDeBens()):
                listaAux.inserir(i, listaAux[i])
            else:
                listaAux.inserir(i, listaAux[i+1])
        return listaAux

    def comparaPartidoENomeCrescente(self):
        listaAux = self.comparaTotalDeBensCrescente()
        for i in range(len(listaAux)-1):
            if listaAux[i].getSiglaDoPartido()[0] < listaAux[i+1].getSiglaDoPartido[0]:
                listaAux.inserir(i, listaAux[i])
            else:
                listaAux.inserir(i, listaAux[i+1])
        return listaAux

    def comparaPartidoENomeDecrescente(self):
        listaAux = self.comparaTotalDeBensCrescente()
        for i in range(len(listaAux)-1):
            if listaAux[i+1].getSiglaDoPartido()[0] > listaAux[i].getSiglaDoPartido[0]:
                listaAux.inserir(i, listaAux[i+1])
            else:
                listaAux.inserir(i, listaAux[i])
        return listaAux

    def comparaDataDeNascimentoCrescente(self):
        listaAux = self.comparaPartidoENomeCrescente()
        for i in range(len(listaAux)-1):
            if listaAux[i].getDataDeNascimento() > listaAux[i+1].getDataDeNascimento():
                listaAux.inserir(i, listaAux[i+1])
            else:
                listaAux.inserir(i,listaAux[i])
        return listaAux

    def comparaDataDeNascimentoDecrescente(self):
        listaAux = self.comparaPartidoENomeCrescente()
        for i in range(len(listaAux)-1):
            if listaAux[i].getDataDeNascimento() < listaAux[i+1].getDataDeNascimento():
                listaAux.inserir(i, listaAux[i])
            else:
                listaAux.inserir(i,listaAux[i+1])
        return listaAux
        

    def media(self, parametro): #UF,CARGO,PARTIDO, OCUPAÇÃO ou DATA DE NASCIMENTO
        listaMedia = self.separaTudo()
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

    def remove(self, criterio):
        for candidato in self.candidatos:
            if candidato.getSituacaoDaCandidatura() == criterio or candidato.getSituacaoDoCandidatoPosPleito() == criterio:
                i = self.candidatos.indice(candidato)
                self.candidatos.selecionar(i)
        return self.candidatos
                
         