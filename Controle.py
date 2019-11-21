from Candidatos import *
from Bens import *
from Lista import *
from Leitor import *

class Controle:
    def __init__(self):
        self.candidatos = Lista()
        self.candidatosPorEstado = {}
        self.dicFiltrado = {}

    def carregaCandidatos(self, arquivo): #APROXIMADAMENTE 1 MINUTO PRA CARREGAR
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
                bemCandidato = Bem(arquivo[i][13], arquivo[i][14], arquivo[i][15], arquivo[i][16])
                bens[arquivo[i][11]] = bemCandidato

            for candidato in self.candidatos:
                if candidato.getIdDoCandidato() in bens:
                    candidato.setListaDeBens(bens[str(candidato.getIdDoCandidato())])

        else: raise ValueError('Você precisa carregar os candidatos primeiro')

    def filtraCandidatos(self, filtro, valor=0): #IMPLEMENTAR O VALOR AINDA, É NECESSARIO FORMATAR O VALOR...
        self.dicFiltrado[filtro] = []
        for candidato in self.candidatos:
            if type(candidato.getListaDeBens()) != str:
                filtros = [candidato.getNomeDoPartido(), candidato.getSiglaDaUf(),
                        candidato.getNomeDoMunicipioDeNascimento(), candidato.getCodigoDoCargo()]
                valorBem = candidato.getListaDeBens().getValorDoBem()
                if filtro in filtros:
                    self.dicFiltrado[filtro].append(candidato)

        return self.dicFiltrado

    def separaTudo(self): #SEPARA TUDO DE UMA VEZ, POR ESTADO!
        for candidato in self.candidatos:
            if candidato.getSiglaDaUf() in self.candidatosPorEstado:
                self.candidatosPorEstado[candidato.getSiglaDaUf()].append(candidato)
            else:
                self.candidatosPorEstado[candidato.getSiglaDaUf()] = []
        

    def comparaCandidatos(self, nome1, nome2):
        nomesCandidatos = {}
        for candidato in self.candidatos:
            nomesCandidatos[candidato.getNomeDoCandidato()] = candidato.getCpf()
        
        if (nome1.upper() in nomesCandidatos) and (nome2.upper() in nomesCandidatos):
            if nomesCandidatos[nome1.upper()] == nomesCandidatos[nome2.upper()]:
                return True
            return False

    def media(self, parametro):
        listaMedia = []
        total = 0
        for candidato in self.candidatos:
            if parametro == candidato.getSiglaDaUf():
                listaMedia.append(candidato)
                total += 1
            elif parametro == candidato.getDescricaoDoCargo():
                listaMedia.append(candidato)
                total += 1
            elif parametro == candidato.getNomeDoPartido():
                listaMedia.append(candidato)
                total += 1
            elif parametro == candidato.getDataDeNascimento():
                listaMedia.append(candidato)
                total += 1
            elif paramtero == candidato.getDescricaoDaOcupacao():
                listaMedia.append(candidato)
                total += 1
        
        return 'Média', len(listaMedia) // total #IMPORTANTE VERIFICAR SE A LISTA DE BENS È UMA LISTA ENCADEADA
        
