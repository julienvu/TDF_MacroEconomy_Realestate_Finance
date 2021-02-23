def occupe(L,i):
    print(L[i])
    return L[i]

occupe([False]*11,3)

def egal(L1,L2):
    if len(L1)!=len(L2):
        return False
    for i in range(len(L1)):
        if(L1[i]!=L2[i]):
            return False

    return True

egal([True]*11,[False]*11)

def avancer_fin(L,m):

    return L[:m]+[False]+L[m:-1]


def avancer_debut(L,b,m):
    return avancer(L[:m+1],b)+L[m+1:]

def avancer_debut_bloque(L,b,m):
    i=m-1

    while i>=0 and occupe(L,i):
        i=i-1
    return avancer_debut(L,b,i)


def avancer_files(L1,b1,L2,b2):
    longL1=len(L1)
    m=longL1//2
    L1_part=avancer_fin(L1,m)
    L2_part=avancer_fin(L2,m)
    R1=avancer_debut(L1_part,b1,m)
    if occupe(R1,m):
        R2=avancer_debut(L2_part,b2,m)
    else:
        
        R2=avancer_debut_bloque(L2_part,b2,m)

    return [R1,R2]

def elim_double(L):

    L_sansdoublon=[]
    
    for element in L:
        if len(L_sansdoublon)==0 or element !=L_sansdoublon[-1]:
            L_sansdoublon.append(element)
    print(L_sansdoublon)
    return L_sansdoublon

elim_double([1,1,3,3,3,7])


def versEntier(L):
    
    
    
    
    
    
