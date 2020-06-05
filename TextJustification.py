import sys
from math import inf

def quality(string,MaxLen):
    if(string==[]):
        return 0
    a=sum([len(i) for i in string])+len(string)-1
    return (MaxLen-a)**3



def paraSeparate(fp):
    fpt=fp.split('\n')
    paras=[[]]
    for i in fpt:
        if(i==''):
            paras.append([])
        else:
            tmp=i.split()
            for j in tmp:
                paras[-1].append(j)
    return paras





def justify(List,dp,index,MaxLen):
    if(List==[]):
        dp[(0,0)]=(0,[])
    for j in range(len(List)-1,-1,-1):
        tmp=List[j:]
        q=quality(tmp,MaxLen)
        p=tmp
        if(q<0):
            q=inf
        
        for k in range(j+1,len(List)):
            tmpq=quality(List[j:k],MaxLen)
            tmp2= (tmpq if (tmpq>=0) else inf)+dp[(k,len(List))][0]
            path=List[j:k]+['\n']+dp[k,len(List)][1]
            if(tmp2>=0 and tmp2<q):
                q=tmp2
                p=path
        dp[(j,len(List))]=(q,p)

def FormattedPrint(arr):
    for i in arr:
        newArr=[]
        for j in i:
            newArr.append(j)
            if(j!='\n'):
                newArr.append(' ')
        if(newArr!=[]):
            print(''.join(newArr))
            print('')



if(len(sys.argv)<3):
    print("Provide Arguments please. First One File Name and Second width of page")
else:
    fp=open(sys.argv[1],"r")
    MaxLen=int(sys.argv[2])
    fpt=fp.read()
    fp.close()
    paras=paraSeparate(fpt)
    justified=[]
    for stuff in paras:
        dp={}
        justify(stuff,dp,0,MaxLen)
        justified.append(dp[0,len(stuff)][1])
    FormattedPrint(justified)


