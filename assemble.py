registradores = ["$zero","$at", "$v0", "$v1", "$a0", "$a1", "$a2", "$a3" ,"$t0" , "$t1" , "$t2", "$t3", "$t4",
 "$t5", "$t6", "$t7", "$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7", "t8", "$t9", "$k0", "$k1", "$gp", "$sp", "$fp", "$ra"]

registradores_num = ["0","1", "2", "3", "4", "5", "6" ,"7" , "8" , "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
 "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"] 

R = ["add", "addu", "sub", "subu", "mult", "multu", "div", "divu", "mfhi",
 "mflo", "and", "or","slt","sltu", "sll", "srl","jr","mul"]

funcR = ["32", "33", "34", "35", "24", "25", "26", "27", "16", "18", "36", "37",
 "42", "43", "00", "02","08","02"]

I = ["addi", "addiu", "lw","sw","lui", "ori", "andi","slti", "sltiu", "beq", "bne"]

opI = ["0x08", "0x09", "0x23","0x2b","0x0f","0x0d", "0x0c","0x0a", "0x0b", "0x04", "0x05"]

J = ["j", "jal"]

opJ = ["0x02", "0x03"]

def turnBin(int):
    int = format(int,"b")
    return int

def lenBin(str):
    aux = str
    if (len(aux) < 5):
        aux = aux.zfill(5)
    return aux

file1 = open("./Nova pasta/mips2.asm","r")
linhas = file1.readlines()
quantidadeLinhas = len(linhas) 
arquivo = open("./Nova pasta/mips2.asm","r")

for i in range(quantidadeLinhas):
    label = "1"
    codeLinha = arquivo.readline()
    listar = codeLinha.split()

    for controle in range(17):
        if(listar[0] == R[controle]):
            instrução = "R"
            instruRCont = controle
            label = 0
    
    for controle in range(10):
        if(listar[0] == I[controle]):
            instrução = "I"
            instruICont = controle
            label = 0

    for controle in range(1):
        if(listar[0] == J[controle]):
            instrução = "J"
            instruJCont = controle
            label = 0
           
    
    if (label == "1"):
        label = str(listar[0])
        varCont = label.find(":")
        if(varCont == -1):
            break
        else:
            num = quantidadeLinhas
            num = bin(num)
            continue

    if(instrução == "R"):
        type = listar[0]
        listar.pop(0)
        listar = str(listar).strip("[]")
        listar = listar.strip("'")
        listar = listar.replace("'","")
        listar = listar.split(",")  
        
        print(R[instruRCont])
        print(listar[0])
        print(listar[1])
        print(listar[2])

        if (R[instruRCont] == "add"):
            Op = "000000"
            rs = format(int(registradores_num[registradores.index(listar[1])]),"b")
            rs = lenBin(rs)
            rt = format(int(registradores_num[registradores.index(listar[2])]),"b")
            rt = lenBin(rt)
            rd = format(int(registradores_num[registradores.index(listar[0])]),"b")
            rd = lenBin(rd)
            sa = "00000"
            function = funcR[R.index("add")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "addu"):
            Op = "000000"
            rs = format(int(registradores_num[registradores.index(listar[1])]),"b")
            rs = lenBin(rs)
            rt = format(int(registradores_num[registradores.index(listar[2])]),"b")
            rt = lenBin(rt)
            rd = format(int(registradores_num[registradores.index(listar[0])]),"b")
            rd = lenBin(rd)
            sa = "00000"
            function = funcR[R.index("addu")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "sub"):
            Op = "000000"
            rs = format(int(registradores_num[registradores.index(listar[1])]),"b")
            rs = lenBin(rs)
            rt = format(int(registradores_num[registradores.index(listar[2])]),"b")
            rt = lenBin(rt)
            rd = format(int(registradores_num[registradores.index(listar[0])]),"b")
            rd = lenBin(rd)
            sa = "00000"
            function = funcR[R.index("sub")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "subu"):
            Op = "000000"
            rs = format(int(registradores_num[registradores.index(listar[1])]),"b")
            rs = lenBin(rs)
            rt = format(int(registradores_num[registradores.index(listar[2])]),"b")
            rt = lenBin(rt)
            rd = format(int(registradores_num[registradores.index(listar[0])]),"b")
            rd = lenBin(rd)
            sa = "00000"
            function = funcR[R.index("subu")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "mul"):
            Op = "011100"
            rs = format(int(registradores_num[registradores.index(listar[1])]),"b")
            rs = lenBin(rs)
            rt = format(int(registradores_num[registradores.index(listar[2])]),"b")
            rt = lenBin(rt)
            rd = format(int(registradores_num[registradores.index(listar[0])]),"b")
            rd = lenBin(rd)
            sa = "00000"
            function = funcR[R.index("mul")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "mult"):
            Op = "000000"
            rs = format(int(registradores_num[registradores.index(listar[1])]),"b")
            rs = lenBin(rs)
            rt = format(int(registradores_num[registradores.index(listar[2])]),"b")
            rt = lenBin(rt)
            rd = "00000"
            rd = lenBin(rd)
            sa = "00000"
            function = funcR[R.index("mult")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "multu"):
            Op = "000000"
            rs = format(int(registradores_num[registradores.index(listar[1])]),"b")
            rs = lenBin(rs)
            rt = format(int(registradores_num[registradores.index(listar[2])]),"b")
            rt = lenBin(rt)
            rd = "00000"
            rd = lenBin(rd)
            sa = "00000"
            function = funcR[R.index("multu")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "div"):
            Op = "000000"
            rs = format(int(registradores_num[registradores.index(listar[0])]),"b")
            rs = lenBin(rs)
            rt = format(int(registradores_num[registradores.index(listar[1])]),"b")
            rt = lenBin(rt)
            rd = "00000"
            rd = lenBin(rd)
            sa = "00000"
            function = funcR[R.index("div")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "divu"):
            Op = "000000"
            rs = format(int(registradores_num[registradores.index(listar[1])]),"b")
            rs = lenBin(rs)
            rt = format(int(registradores_num[registradores.index(listar[2])]),"b")
            rt = lenBin(rt)
            rd = "00000"
            rd = lenBin(rd)
            sa = "00000"
            function = funcR[R.index("divu")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "mfhi"):
            Op = "000000"
            rs = "00000"
            rs = lenBin(rs)
            rt = "00000"
            rt = lenBin(rt)
            rd = format(int(registradores_num[registradores.index(listar[0])]),"b")
            rd = lenBin(rd)
            sa = "00000"
            function = funcR[R.index("mfhi")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "mflo"):
            Op = "000000"
            rs = "00000"
            rs = lenBin(rs)
            rt = "00000"
            rt = lenBin(rt)
            rd = format(int(registradores_num[registradores.index(listar[0])]),"b")
            rd = lenBin(rd)
            sa = "00000"
            function = funcR[R.index("mflo")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "and"):
            Op = "000000"
            rs = format(int(registradores_num[registradores.index(listar[1])]),"b")
            rs = lenBin(rs)
            rt = format(int(registradores_num[registradores.index(listar[2])]),"b")
            rt = lenBin(rt)
            rd = format(int(registradores_num[registradores.index(listar[0])]),"b")
            rd = lenBin(rd)
            sa = "00000"
            function = funcR[R.index("and")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "or"):
            Op = "000000"
            rs = format(int(registradores_num[registradores.index(listar[1])]),"b")
            rs = lenBin(rs)
            rt = format(int(registradores_num[registradores.index(listar[2])]),"b")
            rt = lenBin(rt)
            rd = format(int(registradores_num[registradores.index(listar[0])]),"b")
            rd = lenBin(rd)
            sa = "00000"
            function = funcR[R.index("or")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "slt"):
            Op = "000000"
            rs = format(int(registradores_num[registradores.index(listar[1])]),"b")
            rs = lenBin(rs)
            rt = format(int(registradores_num[registradores.index(listar[2])]),"b")
            rt = lenBin(rt)
            rd = format(int(registradores_num[registradores.index(listar[0])]),"b")
            rd = lenBin(rd)
            sa = "00000"
            function = funcR[R.index("slt")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "sltu"):
            Op = "000000"
            rs = format(int(registradores_num[registradores.index(listar[1])]),"b")
            rs = lenBin(rs)
            rt = format(int(registradores_num[registradores.index(listar[2])]),"b")
            rt = lenBin(rt)
            rd = format(int(registradores_num[registradores.index(listar[0])]),"b")
            rd = lenBin(rd)
            sa = "00000"
            function = funcR[R.index("sltu")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "sll"):
            Op = "000000"
            rs = "00000"
            rs = lenBin(rs)
            rt = format(int(registradores_num[registradores.index(listar[1])]),"b")
            rt = lenBin(rt)
            rd = format(int(registradores_num[registradores.index(listar[0])]),"b")
            rd = lenBin(rd)
            sa = format(int(registradores_num[registradores.index(listar[2])]),"b")
            sa = lenBin(sa)
            function = funcR[R.index("sll")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "srl"):
            Op = "000000"
            rs = "00000"
            rs = lenBin(rs)
            rt = format(int(registradores_num[registradores.index(listar[1])]),"b")
            rt = lenBin(rt)
            rd = format(int(registradores_num[registradores.index(listar[0])]),"b")
            rd = lenBin(rd)
            sa = format(int(registradores_num[registradores.index(listar[2])]),"b")
            sa = lenBin(sa)
            function = funcR[R.index("srl")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        if (R[instruRCont] == "jr"):
            Op = "000000"
            rs = format(int(registradores_num[registradores.index(listar[0])]),"b")
            rs = lenBin(rs)
            rt = "00000"
            rt = lenBin(rt)
            rd = "00000"
            rd = lenBin(rd)
            sa = "00000"
            sa = lenBin(sa)
            function = funcR[R.index("jr")]
            arquivoBin = open("assembly.m", "a")
            arquivoBin.write(Op)
            arquivoBin.write(rs)
            arquivoBin.write(rt)
            arquivoBin.write(rd)
            arquivoBin.write(sa)
            arquivoBin.write(format(int(function),"b"))
            arquivoBin.write("\n")
            arquivoBin.close()

        
            
        
        

        