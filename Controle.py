from Candidatos import *
from Bens import *
from Lista import *
from leitor_CSV import *

class Controle:
    def __init__(self):
        self.listinha = []

    def carregamentoCandidatos(self, pathCandidatos):
        path = pathCandidatos
        arquivo = get_archives(path)
        with open(arquivo[0], 'r', errors='ignore') as path:
            for lines in path:
                if 'DT_GERACAO' in lines:
                    continue
                lines = (lines.replace('"', '').strip()).split(';')
                print(len(lines))
                pessoa = Candidato(lines)
                self.listinha.append(pessoa)
        return self.listinha
    def carregamentoBens(self, pathBens):
        pass
