from sys import argv
import fnmatch
from registers import *

filename=argv[1]
if fnmatch.fnmatch(filename,'*.asm'):
    def count_len(var):
        return len(var.split('"')[1])
    with open(filename,"r")as files:
        buffers=[]
        temp=[]
        name=[]
        tot_byte=[]
        byte=[]
        lent=[]
        status=[]
        sys=[]
        addr=[]
        data=[]
        symbol=[]
        temp1=[]
        g=0
        t1=0
        p=0
        li=0
        for line in files:
            li=li+1
            s=line.split()
            if len(s)>1:
                if s[1]=="dd":
                    k=s[2].split(",")
                    if s[0] not in name:
                        ans=4*(len(k))
                        name.append(s[0])
                        tot_byte.append(ans)
                        byte.append(4)
                        lent.append(len(k))
                        status.append('D')
                        sys.append('S')
                        addr.append(t1)
                        data.append(s[2])
                        g=g+1
                        r="{}".format(g)
                        temp1.append(r)
                        temp1.insert(0,"sym")
                        str="".join(temp1)
                        symbol.append(str)
                        temp1=[]
                        t1=t1+ans
                    else:
                        err_line.append(li)
                        err_name.append("Error:already defined")
                        err.append(101)
                        err_spec.append(s[0])


                elif s[1]=="db":
                    if s[0] not in name:
                        ans=count_len(' '.join(s[2:]))
                        name.append(s[0])
                        tot_byte.append(ans)
                        byte.append(1)
                        lent.append(ans)
                        status.append('D')
                        sys.append('S')
                        addr.append(t1)
                        data.append((''.join(s[2:])))
                        g=g+1
                        r="{}".format(g)
                        temp1.append(r)
                        temp1.insert(0,"sym")
                        str="".join(temp1)
                        symbol.append(str)
                        temp1=[]
                        t1=t1+ans
                    else:
                        err_line.append(li)
                        err_name.append("Error:already defined")
                        err_append(102)
                        err_spec.append(s[0])
                elif s[1]=="resd":
                    if s[0] not in name:
                        ans=4*int(s[2])
                        name.append(s[0])
                        tot_byte.append(ans)
                        byte.append(4)
                        lent.append(1)
                        status.append("D")
                        sys.append("S")
                        addr.append(t1)
                        data.append(s[2])
                        g=g+1
                        r="{}".format(g)
                        temp1.append(r)
                        temp1.insert(0,"sym")
                        str="".join(temp1)
                        symbol.append(str)
                        temp1=[]
                        t1=t1+ans
                    else:
                        err_line.append(li)
                        err_name.append("Error:already defined")
                        err_spec.append(s[0])
                        err.append(103)
                else:
                    for i in range(len(s[0])):
                        if(s[0][i]==":"):
                            p=s[0].split(":")
                            name.append(p[0])
                            tot_byte.append("-")
                            byte.append("-")
                            lent.append("-")
                            status.append("D")
                            sys.append("L")
                            addr.append("-")
                            data.append("-")
                            g=g+1
                            r="{}".format(g)
                            temp1.append(r)
                            temp1.insert(0,"sym")
                            str="".join(temp1)
                            symbol.append(str)
                            temp1=[]

            if(len(s)==1):
                for i in range(len(s[0])):
                    if(s[0][i]==":"):
                        p=s[0].split(":")
                        name.append(p[0])
                        tot_byte.append("-")
                        byte.append("-")
                        lent.append("-")
                        status.append("D")
                        sys.append("L")
                        addr.append("-")
                        data.append("-")
                        g=g+1
                        r="{}".format(g)
                        temp1.append(r)
                        temp1.insert(0,"sym")
                        str="".join(temp1)
                        symbol.append(str)
                        temp1=[]

            for j in range(len(s)):
                if(s[j]=="global"):
                    buffers.append(s[j+1])
                elif(s[j]=="jnz"):
                    buffers.append(s[j+1])
                elif(s[j]=="jle"):
                    buffers.append(s[j+1])
                elif(s[j]=="jge"):
                    buffers.append(s[j+1])
        for i in range(0,len(buffers)):
            if buffers[i] not in(name):
                name.append(buffers[i])
                tot_byte.append("-")
                byte.append("-")
                lent.append("-")
                status.append("U")
                sys.append("L")
                addr.append("-")
                data.append("-")
                g=g+1
                r="{}".format(g)
                temp1.append(r)
                temp1.insert(0,"sym")
                str="".join(temp1)
                symbol.append(str)
                temp1=[]
        for i in range(len(status)):
            if 'U'==status[i]:
                err_line.append(li)
                err_name.append("Error:symbol undefined")
                err_spec.append(name[i])
                err.append(i)

        if len(err)==0:
            print("\t\t",  "-------------------SYMBOL TABLE--------------------","\n\n")
            print("sys_name","\t","Tot_Byte","\t","Sym_Size","\t","Tot_len","\t","Sys_DU","\t","Sys_Type","\t","Sym_Addr","\t","Sym_Val")
            for i in range(0,len(name)):
                print(name[i],"\t\t",tot_byte[i],"\t\t",byte[i],"\t\t",lent[i],"\t\t",status[i],"\t\t",sys[i],"\t\t",addr[i],"\t\t",data[i])
        else:
            for i in range(len(err)):
                print(filename,':',err_line[i],':',err_name[i],'"',err_spec[i],'"')
else:
    print("Warning:please specify only asm file")

