import math
import numpy as np
import random

def générer_PI(n, cmax):
    PI=[]
    while len(PI)<n:
        abscisse=random.randrange(0,cmax+1)
        ordonnee=random.randrange(0,cmax+1)
        if[abscisse, ordonnee] not in PI:
            PI.extend((abscisse,ordonnee))
        print('[PI_X=',abscisse, ', PI_Y=' ,ordonnee,']')
    return np.array(PI,dtype=int)

générer_PI(20,10000)

'I:)A:B)les coordonnées doivent être positifs et donc avoir n points distincts avec n<=(cmax+1)**2'

'I.A2) Calcul des distances'

'fonction position robot'
def position_robot():
    x=random.randrange(0,100)
    y=random.randrange(0,100)
    print('[PI_X=',x, ', PI_Y=' ,y,']')
    return np.array((x,y))


position_robot()
    

def calculer_distances(PI):
    n=len(PI)
    posit=position_robot()
    listdistances=np.zeros((n+1,n+1),dtype='float')
    for i in range(n):
        for j in range(i):
            listdistances[i,j]=math.sqrt((PI[i,0]-PI[j,0])**2 +(PI[i,1]-PI[j,1])**2)
            listdistances[j,i]=listdistances[i,j]
            listdistances[i,n] = math.sqrt((PI[i,0]-posit[0])**2 +(PI[i,1]-posit[1])**2)
            listdistances[n,i]=listdistances[i,n]
            print(listdistances[n,i])
    return listdistances


dist=calculer_distances(np.array([[1,4,5,8,900]]))


def F1(photos:np.ndarray) :
    n =min(photos)
    b = max(photos)
    h = np.zeros(b - n + 1, np.int64)
    for p in range(n-b):
        h[p - n] += 1
    print(h)
    return h

a=[200,100,300]
F1(np.array(a))

'fournit un tableau de pixels à chaque valeur d intensité entre l intensité minimale à 0 et l intensite maximale'


def SELECTIONNNER_PI(photo:np.ndarray, imin:int, imax:int):
    
    TabFinal=[]
    
    size=photo.shape
    
    for lig in range(size[0]):
        for col in range(size[1]):
            if photo[lig,col]>=imin and photo[lig,col]<=imax:
                TabFinal.append(photo[lig,col])
            print(TabFinal)
    return np.array(TabFinal)


'SELECTIONNNER_PI(a,45,67)'

def longueur_chemin(chemin:list,d:np.ndarray):

    distance=0
    indiced=len(d)-1
    for dist in chemin:
        distance=distance + d[indiced,dist]
        indiced=dist
    return distance



def normaliser_chemin(chemin:list, n:int):
    
    valide=False
    nbocc=0
    visited=[]
    lacked=[True]*n
    
    'suppression des doublons'
    for indice in chemin:
        if indice < n and lacked[indice]==True:
            visited.append(indice)
            lacked[indice]=False
            print(visited)
    'ajoute à la fin les éléments manquants'
    for i in range(n):
        if lacked[i]==True:
            visited.append(i)
            print(visited)
    return visited
         
normaliser_chemin([10,456,234,5665],7)     
def plus_proche_voisin(d:np.ndarray):
    chemin=[]
    n=len(d)-1
    lacked=[True]*n
    
    positionfin=n
    maxim=d.max()
    for i in range(n):
        minim=maxim 
        for j in range(n):
            if lacked[j]==True and d[positionfin,j]<minim:
                minim=d[positionfin,j]
                print(minim)
                indice=j
    chemin.append(indice)
    print(chemin)
    positionfin=indice
    lacked[positionfin]=False
    return chemin

plus_proche_voisin(np.array([[0,0],[0,3000],[0,7000]]))

def créer_population(m:int, d:np.ndarray):

    pop=[]
    chemin=list(range(len(d)-1))
    for ind in range(m):
        random.shuffle(chemin)
        long=longueur_chemin(chemin,d)
        pop.append([[long,chemin]])
        print(pop)
    return pop
créer_population(10,np.array([[0,0],[0,3000],[0,7000]]))

def REDUIRE(p:list):
    'trie la liste p'
    p.sort()
    del p[len(p)//2:]
    print(p)

REDUIRE([10,456,234,5665])
    

def muter_chemin(c:list):
    'renvoie liste de 2 éléments distincts de la liste c'
    position=random.sample(list(range(len(c))),2)
    'permutation des indices'
    c[position[0]],c[position[1]]=c[position[1]],c[position[0]]
    print(c)

muter_chemin([10,456,234,5665])
def muter_population(p:list, proba:float, d:np.ndarray):
    for i in range(len(p)):
        if random.random()<proba:
            chem=p([i][1])
            muter_chemin(chem)
            p[i]=[longueur_chemin(chem,d),chem]

muter_population([10,456,234,5665],0.02,np.array([[0,0],[0,3000],[0,7000]]))
def croiser(c1:list, c2:list):
    longchem=len(c1)
    return normaliser_chemin(c1[0:longchem//2]+c2[longchem//2:longchem],longchem )
        
croiser([10,456,234,5665],[10,459,234,562345])
    

def nouvelle_generation(p:list, d:np.ndarray):
    n1=len(p)
    for i in range(n1):
        croisement=croiser(p([[i][1]]),p([[(i+1)%n1][1]]))
        p.append([longueur_chemin(croisement,d),croisement])

'nouvelle_generation([10,456,234,5665],np.array([[0,0],[0,3000],[0,7000]]))'



def algo_gen(PI:np.ndarray, m:int, proba:float,g:int):

    dist=calculer_distances(PI)
    p=créer_population(m,dist)
    for i in range(g):
        REDUIRE(p)
        nouvelle_generation(p,dist)
        muter_population(p,proba,dist)
    indice1=0
    for ind in range(1,m):
        if p([ind][0]) < p([indice1][0]):
            indice1=ind
    return p[indice1]
'algo_gen(np.array([[0,0],[0,3000],[0,7000]]),12,0.02,3)'
    
    


    
