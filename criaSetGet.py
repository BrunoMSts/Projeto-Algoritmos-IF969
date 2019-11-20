def criaGetSet(Textao):
  String = ''
  textao = tiraAcento(Textao).split('\n')
  for i in textao:
    String += "def get" + ''.join([x.capitalize() for x in i.split(' ')]) + "(): return self.__\n"
  String += "\n"
  for i in textao:
    String += "def set" + ''.join([x.capitalize() for x in i.split(" ")]) + "(novo): self.__ = novo\n" 
  return String
def tiraAcento(Textao): 
  traducao = Textao.maketrans('çãóúêí', 'caouei')
  return Textao.translate(traducao)
