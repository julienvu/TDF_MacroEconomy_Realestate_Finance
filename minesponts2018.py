
import numpy as np
import math

def moyenne(liste_niveaux:list):
    
    som=0
    for i in range(len(liste_niveaux)):
        som=som+liste_niveaux[i]


    moy=som/len(liste_niveaux)

    print(moy)

    return moy

moyenne([1,2,3])

def integr_precise(list_niveaux):
    dt=0.5
    inte=0
    for i in range(len(list_niveaux)-1):
        trapeze=(list_niveaux[i]+list_niveaux[i+1])/2*dt
        inte=inte+trapeze
    print(inte)
    return inte

integr_precise([1,2,3])

def moy_precise(list_niveaux):
    dt=0.5
    t_tot=(len(list_niveaux)-1)*dt
    inte=integr_precise(list_niveaux)
    print(inte)
    return inte


moy_precise([1,2,3])

def ind_premier_pzd(list_niveaux):

    moy=moy_precise(list_niveaux)
    for par in range(len(list_niveaux)):
        if list_niveaux[par]>moy and list_niveaux[par]<moy:
            return par-1
    return -1

def ind_premier_pzd1(list_niveaux):

    moy=moy_precise(list_niveaux)
    for par in range(len(list_niveaux)):
        if list_niveaux[par]>moy and list_niveaux[par]<moy:
            return par
    return -2

def decompose_vagues(list_niveaux:list):
    succ=construction_succ(list_niveaux)
    vag=[]
    for i in range(len(succ)-1):
        Zi=succ[i]
        Zi1=succ[i+1]
        vag.append(list_niveaux[Zi:Zi1])
    return vag

def proprietes(list_niveaux:list):
    cag=decompose_vagues(list_niveaux)s
    dt=0.5
    P=[]
    i0=ind_premier_pzd(list_niveaux)+1
    H1=max(list_niveaux[:i0])-min(vag[0])
    T1=len(vag[0])*dt
    P.append([H1,T1])

    for i in range(len(vag)-1):
        Hi=max(vag[i])-min(vag[i+1])
        Ti=len(vag[i])*dt
        P.append([Hi,Ti])
    return P


def H_m(list_niveaux:list):
    pr=proprietes(list_niveaux)
    Hm=0
    for Pi in pr:
        Hi,Ti=Pi
        if Hi>Hmax:
            Hmax=Hi
    return Hmax
        




    
        

    
