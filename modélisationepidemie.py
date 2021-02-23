import random
import numpy as np
def tri(L):
    n=len(L)
    for i in range(1,n):
    
        j=i
        x=L[i]
        while 0 <j and x<L[j-1]:
            L[j]=L[j-1]
            j=j-1
        L[j]=x
        print("contenu de la liste L à la fin de l'itération",i,": ",L)
tri([5,2,3,1,4])
def tri_chaine(L):
    n=len(L)
    for i in range(1,n):
    
        j=i
        x=L[i]
        while 0 <j and x[1]<L[j-1][1]:
            L[j]=L[j-1]
            j=j-1
        L[j]=x
        print("contenu de la liste L à la fin de l'itération",i,": ",L)

tri_chaine([['Bresil',76],['Kenya',26017],['Ouganda',8431]])

def grille(n) :
    M=[ ]
    for i in range(n) :
        L=[ ]
        for j in range(n): L.append(0)
        M.append(L)
        
    return M
def init(n):

    gril=grille(n)
    
    lig=random.randrange(n)
    col=random.randrange(n)

    gril[lig][col]=1
    print('contenu de grille',gril)
    return gril
init(5)

def compte(G):
    
    compter=[0,0,0,0]
    for i in range(1,len(compter)):
        for j in range (i):
            compter[j]+=1
