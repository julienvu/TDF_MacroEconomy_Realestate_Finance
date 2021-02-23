from math import log, sqrt, floor,ceil
import numpy as np
print(log(0.5))

def sont_proches(x,y):
    atol=10**-5
    rtol=10**-8
    print(np.abs(x-y)<= atol+np.abs(y)*rtol)
    return np.abs(x-y)<= atol+np.abs(y)*rtol

sont_proches(3,4)

def mystere(x,b):
    if x<b:
        return 0
    else:
        print(1+ mystere(x/b,b))
        return 1+ mystere(x/b,b)
        


mystere(1001,10)


def erato_iter(N):

    liste1=[True]*N
    liste2[0]=False
    for i in range(2, floor(sqrt(N))+1):
        if liste1[i-1]==True:
            for j in range(2*i, N+1,i):
                liste1=False

    return liste1

    
def bbs(N):

    p1=24375763
    p1=28972763

    M=p1*p2
    t=time.time()
    ix=ent(10**7 *(t-floor(t)))

    A=0
    for i in range(N):

        if ix%2==1:
            A=A+2**i
        ix=(ix*ix)%M
    return A


def estfermat(a,N):
    return a**(N-1)/N==1
def premier_rapide(n_max):

    N=mystere(n_max,2)
    prob=False
    
def stats_bbs_fermat(N,nb):
    liste=erato_iter(N)
    faux_pre=[]
    for i in range(nb):
        p=premier_rapide(N+1)
        if not liste[p-1]:
            faux_pre.appen(p)
    taux=len(faux_pre)/nb
    return (taux, faux_pre)

def Pi(N):
    liste1=erato_iter(N)
    liste_npi=[]
    pi=0
    for n in range(1,N+1,1):
        if liste1[n]==True:
            pi=pi+1
        liste_npi([n,pi])
    return liste_npi


def verif_Pi(N):

    liste_npi=Pi(N)
    for n in range(5393,N+1):
        if (n/(log(n)-1))>=liste_npi[n-1][1]:
            return False
    return True



def inv_ln_rect_d(a,b,pas):

  

  pasn=round((b-a)/pas)
    integ=0

    for i in range(pasn):
        x=a+(i+1)*pas
        integ=integ+(1/log(x))
    return integ*pas

def lid_d(x,pas):

    if x<1:
        return inv_ln_rect_d(0,x,pas)
    elif x>1:
        int0_1=inv_ln_rect_d(0,1-pas,pas)
        int1_x=inv_ln_rect_d(1+pas,x,pas)
        return int0_1+int1_x
    else:
        return 10***(-25)


    
    
