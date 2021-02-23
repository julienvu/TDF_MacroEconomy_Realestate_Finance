import numpy as np
import math

def smul(a:int,c:list):
    
    g=[]
    for i in range (len(c)):
        g.append(a*c[i])


    print("liste finie smul= ",g)
    return g


smul(2,[2,3,5])


def vsom(a:list,c:list):
    g=[ ]
    compt=0
    if len(c)!=len(a):
        print('Attention: a et c sont de dimensions différentes')
    while(compt<len(c)):
         g.append(a[compt]+c[compt])
         compt=compt+1   

    
    print("liste finie vsom= ",g)
    return g

vsom([1,2,3],[4,5,6])

def vdif(a:list,c:list):
    g=[ ]
    compt=0
    if len(c)!=len(a):
        print('Attention: a et c sont de dimensions différentes')
    while(compt<len(c)):
            g.append(a[compt]-c[compt])
         compt=compt+1
        

    
        
    print("liste finie vdif= ",g)
    return g

vdif([1,2,3],[4,5,6])





def euler(y0,z0,f,h,n):
    L=[]
    N=[]
    y=y0
    z=z0
    L.append(y)
    N.append(z)
    for i in range(n-1):
        fy=f(y)
        y=y+z*h
        z=z+fy*h
        L.append(y)
        N.append(z)
    print("L=  ",L)
    print("N=  ",N)
    return L,N

def verlet(y0,z0,f,h,n):
     L=[]
    N=[]
    y=y0
    z=z0
    L.append(y)
    N.append(z)
    for i in range(n-1):
        fi=f(y)
        y=y+z*h+((h**2)/2)*fi
        fi1=f(y)
        z=z+(h/2)*(fi+fi1)
        L.append(y)
        N.append(z)
    print("L=  ",L)
    print("N=  ",N)
    return L,N

def norme(v):
    norm=0
    for i in range(len(v)):
        norm+=v[i]**2

    return Math.sqrt(norm)

def force2(m1,p1,m2,p2):
    G=6,67e-11
    P1P2=vdif(P2,P1)
    a=G*m1*m2/norme(P1P2)**3

    return smul(a,P1P2)

def pos_suiv(m,posit,vitesse,h):

    L=[]
    for j in range(len(m)):
        m=m[j]
        pj=posit[j]
        vj=vitesse[j]
        force=forceN(j,m,pos)
        nextf=[0,0,0]

        for k in range(3):
            nextf=pj[k]+vj[k]+h**2/2*force[k]/mj
        L.append(nextf)
    return L
        
        

    
    
