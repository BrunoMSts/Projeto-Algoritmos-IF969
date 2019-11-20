from Bens import *
from Lista import *

class Candidato(Bem):
    def __init__(self, anoEleicao, siglaUf, codigoCargo,
                 descricaoCargo, nomeCandidato, idCandidato, numeroUrna,
                 numCpf, nomeUrna, numPartido, nomePartido,
                 siglaPartido, codOcupacaoCandidato, descOcupacao, dataNascimento,
                 sexoCandidato, grauInstrucao, estadoCivil, ufNascimento,
                 nomeMunicipioNascimento, situacaoCandidatoPosPleito, situacaoCandidatura, listaBens):
        self.__anoEleicao = anoEleicao
        self.__siglaUf = siglaUf
        self.__codigoCargo = codigoCargo
        self.__descricaoCargo = descricaoCargo
        self.__nomeCandidato = nomeCandidato
        self.__idCandidato = idCandidato
        self.__numeroUrna = numeroUrna
        self.__numCpf = numCpf
        self.__nomeUrna = nomeUrna
        self.__numPartido = numPartido
        self.__nomePartido = nomePartido
        self.__siglaPartido = siglaPartido
        self.__codOcupacaoCandidato = codOcupacaoCandidato
        self.__descOcupacao = descOcupacao
        self.__dataNascimento = dataNascimento
        self.__sexoCandidato = sexoCandidato
        self.__grauInstrucao = grauInstrucao
        self.__estadoCivil = estadoCivil
        self.__ufNascimento = ufNascimento
        self.__nomeMunicipioNascimento = nomeMunicipioNascimento
        self.__situacaoCandidatoPosPleito = situacaoCandidatoPosPleito
        self.__situacaoCandidatura = situacaoCandidatura
        self.__listaBens = listaBens

    def incluirBem(self, objBem):
        objeto = objBem

        return objeto.getValorDoBem()
    
    def comparaCandidatos(self):
        pass

    def exibeBens(self):
        pass

    def setAnoDaEleicao(self, novo): 
        self.__anoEleicao = novo
    def setSiglaDaUf(self, novo): 
        self.__siglaUf = novo
    def setCodigoDoCargo(self, novo): 
        self.__codigoCargo = novo
    def setDescricaoDoCargo(self, novo): 
        self.__descricaoCargo = novo
    def setNomeDoCandidato(self, novo): 
        self.__nomeCandidato = novo
    def setIdDoCandidato(self, novo): 
        self.__idCandidato = novo
    def setNumeroNaUrna(self, novo): 
        self.__numeroUrna = novo
    def setCpf(self, novo): 
        self.__numCpf = novo
    def setNomeNaUrna(self, novo): 
        self.__nomeUrna = novo
    def setNumeroDoPartido(self, novo): 
        self.__numPartido = novo
    def setNomeDoPartido(self, novo): 
        self.__nomePartido = novo
    def setSiglaDoPartido(self, novo): 
        self.__siglaPartido = novo
    def setCodigoDeOcupacaoDoCandidato(self, novo): 
        self.__codOcupacaoCandidato = novo
    def setDescricaoDaOcupacao(self, novo): 
        self.__descOcupacao = novo
    def setDataDeNascimento(self, novo): 
        self.__dataNascimento = novo
    def setSexoDoCandidato(self, novo): 
        self.__sexoCandidato = novo
    def setGrauDeInstrucao(self, novo): 
        self.__grauInstrucao = novo
    def setEstadoCivil(self, novo): 
        self.__estadoCivil = novo
    def setUfNascimento(self, novo): 
        self.__ufNascimento = novo
    def setNomeDoMunicipioDeNascimento(self, novo): 
        self.__nomeMunicipioNascimento = novo
    def setSituacaoDoCandidatoPosPleito(self, novo): 
        self.__situacaoCandidatoPosPleito = novo
    def setSituacaoDaCandidatura(self, novo): 
        self.__situacaoCandidatura = novo
    def setListaDeBens(self, novo): 
        self.__listaBens = novo

    def getAnoDaEleicao(self): return self.__anoEleicao
    def getSiglaDaUf(self): return self.__siglaUf
    def getCodigoDoCargo(self): return self.__codigoCargo
    def getDescricaoDoCargo(self): return self.__descricaoCargo
    def getNomeDoCandidato(self): return self.__nomeCandidato
    def getIdDoCandidato(self): return self.__idCandidato
    def getNumeroNaUrna(self): return self.__numeroUrna
    def getCpf(self): return self.__numCpf
    def getNomeNaUrna(self): return self.__nomeUrna
    def getNumeroDoPartido(self): return self.__numPartido
    def getNomeDoPartido(self): return self.__nomePartido
    def getSiglaDoPartido(self): return self.__siglaPartido
    def getCodigoDeOcupacaoDoCandidato(self): return self.__codOcupacaoCandidato
    def getDescricaoDaOcupacao(self): return self.__descOcupacao
    def getDataDeNascimento(self): return self.__dataNascimento
    def getSexoDoCandidato(self): return self.__sexoCandidato
    def getGrauDeInstrucao(self): return self.__grauInstrucao
    def getEstadoCivil(self): return self.__estadoCivil
    def getUfNascimento(self): return self.__ufNascimento
    def getNomeDoMunicipioDeNascimento(self): return self.__nomeMunicipioNascimento
    def getSituacaoDoCandidatoPosPleito(self): return self.__situacaoCandidatoPosPleito
    def getSituacaoDaCandidatura(self): return self.__situacaoCandidatura
    def getListaDeBens(self): return self.__listaBens

    def __str__(self):
        '''Nome da Urna -- Número da Urna -- Sigla do partido
            Cargo disputado (UF) Município Nascimento (UF)
            Resumo dos bens:
            - Total declarado: (valor formatado como R$)
            - Total por tipo de bem (imprimir Tipo: valor formatado em R$)
            Você deve também implementar os métodos de comparação entre candidatos. A
            comparação deve ser feita com base no nome completo do candidato. Dois candidatos
            serão iguais somente se tiverem o mesmo nome e o mesmo CPF.'''
        formatado = f'''{self.getNomeNaUrna()}---{self.getNumeroNaUrna()}---{self.getSiglaDoPartido()}
{self.getDescricaoDoCargo()} ({self.getSiglaDaUf()}) {self.getNomeDoMunicipioDeNascimento()} {self.getUfNascimento()}
Resumo dos bens:
    - Total declarado: 
    - Total por tipo de bem:
'''
        return formatado

    def __repr__(self):
        pass
    