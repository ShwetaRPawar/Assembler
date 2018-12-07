from sys import argv
from symboltable import *
from literal import *
from registers import *
import fnmatch
import os
if len(argv)<2:
    print("Error:Specify the Filename")
else:
    filename=argv[1]
def str1(var):
    return (var.split('"')[1])
with open(filename,"r")as file:
    inter_file=os.path.splitext(filename)[0]
    li=[inter_file,"i"]
    inter_file=".".join(li)
    f=open(inter_file,"w")
    output=[]
    temp1=[]
    temp2=[]
    temp3=[]
    for line in file:
        s=line.split()
        if(len(s)==2):
            if(s[0] in sections):
                if(s[1] in sections):

                    f.write(line)

            elif(s[0]=="main:"):
                if(s[1]) in inst:
                    f.write(line)

            else:
                if s[0] in inst:
                    f.write(s[0])
                    f.write("\t")
                k=s[1].split(",")
                if(len(k)==2):
                    d=k[1].split("[")
                    if(k[0]) in reg:
                        if k[0] in assign:
                            temp1.append(assign[k[0]])
                    if(k[1]) in reg:
                        if (k[1]) in assign:
                            temp1.append(assign[k[1]])
                    elif (d[0]=="dword"):
                        q=d[1].split("]")
                        if q[0] in reg:
                            if q[0] in assign:
                                temp2.append(assign[q[0]])
                        elif q[0] in name:
                            for i in range(0,len(name)):
                                if(q[0]==name[i]):
                                    temp2.append(symbol[i])
                                    pass
                        temp3.insert(0,"dword")
                        temp3.insert(1,"[")
                        temp3.insert(2,temp2[0])
                        temp3.insert(3,"]")
                        str="".join(temp3)
                        temp1.append(str)
                        temp2=[]
                        temp3=[]


                    else:
                        for i in range(0,len(actual)):
                            if(actual[i]==k[1]):
                                temp1.append(num1[i])
                                pass
                    temp1.insert(1,",")
                    str="".join(temp1)
                    f.write(str)
                    f.write("\n")
                    temp1=[]
                elif(len(k)==1):
                    if k[0] in inst:
                        f.write(s[1])
                        f.write("\n")
                    elif k[0] in reg:
                        if k[0] in assign:
                            f.write(assign[k[0]])
                            f.write("\n")
                    else:
                        for i in range(0,len(name)):
                            if(name[i]==k[0]):
                                f.write(symbol[i])
                                f.write("\n")

        elif(len(s)>2):
            if(s[1]=="dd" or s[1]=="dq"):
                for i in range(0,len(actual)):
                    if(actual[i]==s[2]):
                        break
                f.write(s[0])
                f.write("\t")
                f.write(num1[i])
                f.write("\n")
            elif(s[1]=="db"):
                if s[2]=='"%d"':
                    f.write(s[0])
                    f.write("\t")
                    f.write(s[2])
                    f.write("\n")
                    pass
                else:
                    p=str1(" ".join(s[2:]))
                    for i in range(0,len(actual)):
                        if(actual[i]==p):
                            break
                    f.write(s[0])
                    f.write("\t")
                    f.write(num1[i])
                    f.write("\n")

            elif(s[1]=="resd"):
                for i in range(0,len(actual)):
                    if (s[2]==actual[i]):
                        pass
                        f.write(s[0])
                        f.write("\t")
                        f.write(num1[i])
                        f.write("\n")
            else:
                for i in range(0,len(s[0])):
                    if(s[0][i]==":"):
                        f.write(s[0])
                        f.write("\t")
                        pass


                if s[1] in inst:
                    f.write(s[1])
                    f.write("\t")
                k=s[2].split(",")
                d=k[1].split("[")
                if(k[0]) in reg:
                    if k[0] in assign:
                        temp1.append(assign[k[0]])
                if(k[1]) in reg:
                    if (k[1]) in assign:
                        temp1.append(assign[k[1]])
                elif k[1] in name:
                    for i in range(0,len(name)):
                        if(name[i]==k[1]):
                            temp1.append(symbol[i])
                elif (d[0]=="dword"):
                    q=d[1].split("]")
                    if q[0] in reg:
                        if q[0] in assign:
                            temp2.append(assign[q[0]])
                    elif q[0] in name:
                        for i in range(0,len(name)):
                            if(q[0]==name[i]):
                                temp2.append(symbol[i])
                                pass
                    temp3.insert(0,"dword")
                    temp3.insert(1,"[")
                    temp3.insert(2,temp2[0])
                    temp3.insert(3,"]")
                    str="".join(temp3)
                    temp1.append(str)
                    temp2=[]
                    temp3=[]
                else:
                    for i in range(0,len(actual)):
                        if(actual[i]==k[1]):
                            temp1.append(num1[i])
                            pass

                temp1.insert(1,",")
                str="".join(temp1)
                f.write(str)
                f.write("\n")
                temp1=[]

        elif(len(s)==1):
            if(s[0])in inst:
                f.write(s[0])
                f.write("\n")
            else:
                for i in range(0,len(s[0])):
                    if(s[0][i]==":"):
                            f.write(s[0])
                            f.write("\n")
                            temp1=[]





