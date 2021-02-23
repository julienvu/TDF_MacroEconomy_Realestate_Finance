import math
import numpy as np
import random

def placement1Drapiede(N:int, R:float, L:float):
    li=L-2*R*N
    pos=li*np.random.rand(N)
    for i in range(N):
        for dec in range(N):
            if pos[dec]>pos[i]:
                pos[dec]=pos[dec]+2*R
        pos[i]=pos[i]+R       
    result=[]
    for par in pos:
        result.append(np.array(par))
    print('res =', result)
    return result

placement1Drapiede(6,0.3,4) 

def placement(D:int, N:int,R:float,L:float):
    def possible(c:np.ndarray):
        Dis=0
        for p in result:
             Dis=Dis+(c[i]-p[i])**2   
        if Dis<4*pi*R**2: return False

    return True
    result=[]
    while len(result)<N:
        p=R+(L-2*R)*np.random.rand(D)
        if possible(p): result.append(p)
        else: res=[]
        print(result)
    return res

placement(3,4,0.1,6.1)

def vol(p:[np.ndarray,np.ndarray], t:float):

    p[0]=p[0]+t*p[1]

    

def rebond(p:[np.ndarray, np.ndarray], d:int):

    p[1][d]=-p[1][d]


def choc(p1:[np.ndarray,np.ndarray], p2:[np.ndarray,np.ndarray]):
    valeur=p1[1]
    p1[1]=p2[1]
    p2[1]=p1[1]

def tr(p:[np.ndarray,np.ndarray],R:float,L:float):
    posit=p[0][0]
    vit=p[1][0]

    if vit>0: return ((L-R-posit)/vit,0)
    if vit<0: return ((R-posit)/vit,0)

    return None

def tc(p1:[np.ndarray,np.ndarray], p2:[np.ndarray,np.ndarray], R:float):

    dist=p1[0][0]-p2[0][0]
    vit=p1[1][[0]-p2[1][0]
    if dist*vit>0:  return None
    return (abs(dist-2*R)/abs(vit))


def ajoutEv(catalogue:[[bool,float,int,int or None, int or None]],e:[bool,float,int,int or None, int or None]):
    time=e[1]

    for i in range(len(catalogue)):
        if time>catalogue[i][1]:
            catalogue.insert(time,i)


def ajout1p(catalogue,i,R,L,particules):
    pi=particules[i]
    eve=tr(pi,R,L)

    if eve!= None: ajoutEv(catalogue,eve)

    for j in range(len(particules)):
        if j!=i:
            eve=tc(pi,particules[j],R)

def initCat(particules,R,L):
    catalogues=[]

    for i in range(len(particules)):
        ajout1p(catalogues,i,R,L,particules)

    return catalogues
            
            
                
    
    

            




    
