import math
import numpy as np
import random
import numbers
def moyenne(X):
    somme=0
    for i in range(len(X)):
        somme+=X[i]
        
   
    moyenne=somme/len(X)
    
    print('moyenne de la série X= ' ,moyenne)
    
    return moyenne

moyenne([1,2,3,4])

def variance(X):
    sommevar=0
    somme=0
    for i in range(len(X)):
        somme+=X[i]

    for i in range(len(X)):
        sommevar+=(X[i]-((1/len(X))*somme))**2
   
    variance=sommevar/len(X)
    print('variance de la série X= ' ,variance)
    
    return variance

variance([1,2,3,4])

def somme(M):

    if isinstance(M, numbers.Real):
        return M
    else:
        somme1=0
        for i in M:
            somme1+=somme(i)
        print("somme des élements de M=",somme1)    
    return somme1

somme([[[1,2],[3,4,5]],6, [7,8],9])




def seuillage(A:np.ndarray, seuil:int):

    B=np.zeros(A.shape,int)

    for lig in A.shape[0]:
        for col in A.shape[1]:
            if A[lig,col]<seuil:
                B[lig,col]=1
            print(B[lig,col])

    return B

def pixel_centre_bille(A:np.ndarray):
    abscises=[]
    ordonnees=[]
    for i in A.shape[0]:
        for j in A.shape[1]:
            if A[i,j]==1:
                abscises.append(i)
                ordonnees.append(j)
    return(round(moyenne(abscises)),round(moyenne(ordonnees)))


def positions(n:int,seuil:int):
    Li=[]
    for i in range(n):
        B=prendre_photos()
        C=seuillage(B,seuil)
        Li.append(pixel_centre_bille(C))

    return Li

def fluctuations(P:[(int,int)]):
    n=len(P)
    x=0
    y=0
    for position in P:
        x+=position[0]
        y+=position[1]

    x/=n
    y/=n
    fluc=0
    for pos in P:
        fluc+=(position[0]-x)**2+(position[1]-y)**2
    return (fluc*t**2)/n


def force(z,Lp,L0,T):
   return (K_B*T/Lp)*(1/(4*(1-z/L0)**2)-1/4+z/L0)

def ajusteWLC(Fz: np.ndarray, T:float):
    def f(z,Lp,L0):
        return force(z,Lp,L0,T)

def derive(phi,x:float,h:float):
    return phi(x*(1+h))-phi(x*(1-h))/2*x*h

def derive_seconde(phi,x:float,h:float):
    derivphi_droite=derive(phi,x*(1+h),h)
    derivphi_gauche=derive(phi,x*(1-h),h)
    return (derivphi_droite-derivphi_gauche)/(2*x*h)

def min_local(phi,x0:float,h:float):
    x=x0
    while abs(derive(phi,x,h))>1e-7:
        x=x-derive(phi,x,h)/derive_seconde(phi,x,h)
    return x

def grad(G,X:np.ndarray, h:float):
    x,y=X
    gx=G(x*(1+h),y)-G(x*(1-h),y)
    gy=gx=G(x,y(1+h))-G(x,y*(1-h))
    return np.array([gx,gy])

def min_local_2d(G,X0:np.ndarray,h:float):
    X=X0
    grad1=grad(G,X,h)
    while abs(grad1[0])<1e-7 and abs(grad1[1])<1e-7:

        X=X-np.dot(np.linalg.inv(J(G,X,h),grad1))
        grad1=grad(G,X,h)
    return X

def conformation(n:int):
    the=[]
    for i in range(n):
        the.append(2*Math.pi*random.random()-Math.pi)


def allongement(theta,l):
    z=0
    for t in theta: z+=l*math.cos(t)

    return z




                   


        
                

        


    
        
