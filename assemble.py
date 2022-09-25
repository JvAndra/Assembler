file1 = open("./Nova Pasta/mips2.asm")
arquivo = file1.readlines()
def find(str, ch):
    indice = 0
    while indice < len(str):
        if str[indice] == ch:
            return indice
        indice = indice + 1
    return -1
LinhasSalvas = []
Linha = 0
for line in arquivo:
    Linha = Linha + 1    
    for word in line.split():  
        print(word)
        x = 0
        if find(word,":") > 0:
            x = Linha
            LinhasSalvas.append(x)
        if word == " ": 
            break
print (LinhasSalvas[0]) 
print (LinhasSalvas[1])
   