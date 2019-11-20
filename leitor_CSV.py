import os

diretorio_bem_candidatos= r'C:\Users\HOME\Desktop\Programação\Projeto Algoritmos\bem_candidato_2014'
diretorio_consulta_cand = r'C:\Users\HOME\Desktop\Programação\Projeto Algoritmos\consulta_cand_2014'
datas = {'AC':{}, 'AL':{}, 'AM':{}, 'AP':{}, 'BA':{},
               'BR':{}, 'BRASIL':{}, 'CE':{}, 'DF':{}, 'ES':{},
               'GO':{}, 'MA':{}, 'MG':{}, 'MS':{}, 'MT':{}, 'PA':{},
               'PB':{}, 'PE':{}, 'PI':{}, 'PR':{}, 'RJ':{}, 'RN':{}, 'RO':{},
               'RR':{}, 'RS':{}, 'SC':{}, 'SE':{}, 'SP':{}, 'TO':{}}
def get_archives(directory):
    archives = []
    for root, directories, files in os.walk(directory):
        for filename in files:
                archives.append(os.path.join(root,filename))
    return archives[:len(archives)-1]

def get_lines(archive):
    a = open(archive, 'r')
    lines = [x for x in range(len(a.readlines()))]
    a.close()
    return lines

def tratarStr(lista):
    newLista = []
    for a in lista:
        newLista.append(a.replace('"', '').strip())
    return newLista
        
        
def read_archives():
    archives = get_archives(diretorio_bem_candidatos)
    colunms = open(archives[0], 'r').readline().split(';')
    datasAux = {}
    cont = 0
    for a in datas.keys():
        for i in colunms:
            index = colunms.index(i)
            colunms.pop(index)
            colunms.insert(index, i.replace('"','').strip())
            datasAux[colunms[index]] = []
        datas[a] = datasAux

    for i in range(len(archives)): #IMPLEMENTAR O CÓDIGO QUE COLOCA OS VALORES EM CADA COLUNA DE CADA ESTADO
        lines = get_lines(archives[i])
        for j in lines:
            b = open(archives[i], 'r')
            arrayData = b.readlines()[j].split(';')
            arrayData = tratarStr(arrayData)
            break
        break
            

    return datas
