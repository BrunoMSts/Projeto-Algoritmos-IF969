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

    def filtrar(self, partido, uf, municipioNascimento, cargo, valorBens, pleito): #IMPLEMENTAR O VALOR AINDA, É NECESSARIO FORMATAR O VALOR...
        listaAux = []
        for candidato in self.candidatos:
            valor = candidato.getValorTotalDeclarado()
            if (candidato.getSiglaDoPartido() == partido) and (candidato.getSiglaDaUf() == uf) and (candidato.getNomeDoMunicipioDeNascimento() == municipioNascimento) and (candidato.getDescricaoDoCargo() == cargo) and (valor > valorBens) and (candidato.getSituacaoDoCandidatoPosPleito() == pleito):
                listaAux.append(candidato)
        return listaAux

    def comparaOrdemAlfabeticaCrescente(self):
        listaAux = Lista()
        for i in range(len(self.candidatos)-1):
            if self.candidatos[i].getNomeDoCandidato().split()[0][0] < self.candidatos[i+1].getNomeDoCandidato().split()[0][0]:
                if self.candidatos[i].getNomeDoCandidato().split()[1][0] < self.candidatos[i+1].getNomeDoCandidato().split()[1][0]:
                    listaAux.anexar(self.candidatos[i])
                listaAux.anexar(self.candidatos[i])
        return listaAux

    def comparaOrdemAlfabeticaDecrescente(self):
        listaAux = Lista()
        for i in range(len(self.candidatos)-1):
            if self.candidatos[i+1].getNomeDoCandidato().split()[0][0] > self.candidatos[i].getNomeDoCandidato().split()[0][0]:
                if self.candidatos[i+1].getNomeDoCandidato().split()[1][0] > self.candidatos[i].getNomeDoCandidato().split()[1][0]:
                    listaAux.anexar(self.candidatos[i+1])
                listaAux.anexar(self.candidatos[i+1])
        return listaAux

    def comparaTotalDeBensCrescente(self):
        listaAux = comparaOrdemAlfabeticaCrescente(self)
        for i in range(len(listaAux)-1):
            pass

    def comparaTotalDeBensDecrescente(self):
        pass

    def comparaPartidoENomeCrescente(self):
        pass

    def comparaPartidoENomeDecrescente(self):
        pass

    def comparaDataDeNascimentoCrescente(self):
        pass

    def comparaDataDeNascimentoDecrescente(self):
        pass

        

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

    def incluirBem(self, objBem, candidato):
        if type(candidato.getListaDeBens) == str:
            candidato.setListaDeBens() = []
        candidato.getListaDeBens().anexar(objBem)

    def remove(self, criterio):
        for candidato in self.candidatos:
            if candidato.getSituacaoDaCandidatura() == criterio or candidato.getSituacaoDoCandidatoPosPleito() == criterio:
                i = self.candidatos.indice(candidato)
                self.candidatos.selecionar(i)
        return self.candidatos
                
         