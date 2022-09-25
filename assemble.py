from operator import indexOf


arquivo = open("mips2.asm")
def find(str, ch):
    indice = 0
    while indice < len(str):
        if str[indice] == ch:
            return indice
        indice = indice + 1
    return -1
for line in arquivo:    
    for word in line.split():  
        print(word)
        if find(word,":") < 0:
             
        if word == " ": 
            break
print (LinhasSalvas[0]) 
print (LinhasSalvas[1])
   