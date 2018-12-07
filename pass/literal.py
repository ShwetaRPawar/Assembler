from sys import argv
from symboltable import *
from registers import *
def count_len(string):
    return (string.split('"')[1])
filename=argv[1]

with open(filename,"r")as files:
    variable=[]
    num=[]
    hexval=[]
    actual=[]
    temp=[]
    temp1=[]
    sh=[]
    num1=[]
    dic=['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    p=0
    for line in files:
        s=line.split()
        if(len(s)>2):
            if(s[1]=="dd"):

                k=s[2].split(",")
                for i in range(0,len(k)):
                    f=(hex(int(k[i])))
                    y=f.upper()
                    v=y.split("0X")
                    hexval.append(v[1])

                for j in range(0,len(hexval)):
                    if hexval[j] in dic:

                        temp1.append(hexval[j])
                        temp1.append("000000")
                        temp1.insert(0,"0")
                        str="".join(temp1)
                        sh.append(str)
                        temp1=[]
                    else:
                        temp1.append(hexval[j])
                        temp1.append("0000000")
                        str="".join(temp1)
                        sh.append(str)
                        temp1=[]
                if s[2] not in actual:
                    p=p+1
                    actual.append(s[2])
                    temp.append(sh)
                    sh=[]
                    hexval=[]
                    b="{}".format(p)
                    num.append(b)
                    num.insert(0,"lit")
                    str1="".join(num)
                    num1.append(str1)
                    num=[]
                    variable.append(s[0])


            elif(s[1]=="db"):

                b=""
                if(s[2]=='"%d"'):
                    pass
                else:
                    str2=count_len(' '.join(s[2:]))
                    for i in range(0,len(str2)):
                        a=hex(ord(str2[i]))
                        q=a.split("0x")
                        b=b+q[1]
                if str2 not in actual:
                    p=p+1
                    actual.append(str2)
                    temp.append(b)
                    b="{}".format(p)
                    num.append(b)
                    num.insert(0,"lit")
                    str1="".join(num)
                    num1.append(str1)
                    num=[]
                    variable.append(s[0])

            elif(s[1]=="resd"):

                f=hex(int(s[2]))
                y=f.upper()
                v=y.split("0X")
                if v[1] in dic:
                    temp1.append(v[1])
                    temp1.append("000000")
                    temp1.insert(0,"0")
                    str="".join(temp1)
                    sh.append(str)
                    temp1=[]

                else:
                    temp1.append(v[1])
                    temp1.append("0000000")
                    str="".join(temp1)
                    sh.append(str)
                    temp1=[]

                if s[2] not in actual:
                    p=p+1
                    actual.append(s[2])
                    temp.append(sh)
                    sh=[]
                    b="{}".format(p)
                    num.append(b)
                    num.insert(0,"lit")
                    str1="".join(num)
                    num1.append(str1)
                    num=[]
                    variable.append(s[0])

            else:
                for i in range(0,len(s[2])):
                    if(s[2][i]==','):
                        c=s[2].split(",")
                        g=c[1].split("[")
                        if c[1] in inst:
                            break
                        elif c[1] in reg:
                            break
                        elif(g[0]=="dword"):
                            pass
                        elif c[1] in name:
                            pass
                        else:
                            h=(hex(int(c[1]))).upper()
                            w=h.split("0X")

                            if w[1] in dic:
                                temp1.append(w[1])
                                temp1.append("000000")
                                temp1.insert(0,"0")
                                str="".join(temp1)
                                temp1=[]
                                if c[1] not in actual:
                                    p=p+1
                                    b="{}".format(p)
                                    num.append(b)
                                    num.insert(0,"lit")
                                    str1="".join(num)
                                    num=[]
                                    num1.append(str1)
                                    temp.append(str)
                                    actual.append(c[1])
                            else:
                                temp1.append(w[1])
                                temp1.append("000000")
                                str="".join(temp1)
                                temp1=[]
                                if c[1] not in actual:
                                    p=p+1
                                    b="{}".format(p)
                                    num.append(b)
                                    num.insert(0,"lit")
                                    str1="".join(num)
                                    num=[]
                                    num1.append(str1)
                                    temp.append(str)
                                    actual.append(c[1])
        elif(len(s)==2):
             for i in range(0,len(s[1])):
                if(s[1][i]==','):
                    c=s[1].split(",")
                    g=c[1].split("[")
                    if c[1] in inst:
                        break
                    elif c[1] in reg:
                        break
                    elif(g[0]=="dword"):
                        pass
                    else:
                        h=(hex(int(c[1]))).upper()
                        w=h.split("0X")

                        if w[1] in dic:
                            temp1.append(w[1])
                            temp1.append("000000")
                            temp1.insert(0,"0")
                            str="".join(temp1)
                            temp1=[]
                            if c[1] not in actual:
                                p=p+1
                                b="{}".format(p)
                                num.append(b)
                                num.insert(0,"lit")
                                str1="".join(num)
                                num=[]
                                num1.append(str1)
                                temp.append(str)
                                actual.append(c[1])
                        else:
                            temp1.append(w[1])
                            temp1.append("000000")
                            str="".join(temp1)
                            temp1=[]
                            if c[1] not in actual:
                                p=p+1
                                b="{}".format(p)
                                num.append(b)
                                num.insert(0,"lit")
                                str1="".join(num)
                                num=[]
                                num1.append(str1)
                                temp.append(str)
                                actual.append(c[1])

    print("\t\t","------------------------LITERAL TABLE---------------------","\n\n")
    print("Lit_num","\t\t","Hex_val","\t\t","Actual_val")
    for i in range(0,len(temp)):
        print(num1[i],"\t","".join(temp[i]),"\t",actual[i])

