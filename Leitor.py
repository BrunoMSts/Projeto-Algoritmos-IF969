def ler(archive):
    lista = []
    arquivo = open(archive+'.csv', 'r', errors='ignore')
    lista += arquivo.readlines()
    arquivo.close()
    arquivo = [x.strip().replace('"', "").split(";") for x in lista]
    return arquivo