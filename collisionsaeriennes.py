def nb_conflits():
    
    N=len(conflit)
    res=0
    for lig in range(N):
        for col in range(lig+1,N):
            if conflit[i][j]>0:
                res=res+1

    return res


def nb_vol_par_niveau_relatif(regulation):

    
    a,b,c=0,0,0

    
    for r in regulation:
        if r==0:
            a=a+1
        if r==1:
            b=b+1
        if r==2:
            c=c+1
    return [a,b,c]

def cout_regulation(regulation):
    N=len(regulation)
    cout=0
    for lig in range(N):
        r=3*lig+regulation[lig]
        for col in range(lig+1,N):
            cout=cout+conflit[r][3*col+regulation[col]]
    

    return cout


def cout_RFL():
    return cout_regulation([0]*len(conflit)//3))




def cout_du_sommet(s,etat_sommet):

    couttot=0
    for i in range(len(etat_sommet)):
        if etat_sommet[i]>0 and i !=s:
            couttot=coutot+conflit[s][i]

    return couttot



def sommet_de_cout_min(etat_sommet):

    cout_min=np.inf
    sommet_min=0
    for i in range(len(etat_sommet)):
        if etat_sommet[i]==2:
            cout=cout_du_sommet(i,etat_sommet)
            if cout_min<0 or cout<cout_min:
                cout_min=cout
                indice=i
    return indice


def recuit(regulation):
    T=1000
    n=len(regulation)

    cout=cout_regulation(regulation)

    while T>=1:
        val=randint(n)
        r=regulation[val]
        regulation[val]=(r+1+randint(2))%3
        cout_test=cout_regulation(regulation)
        if cout_test<cout or random()<exp((cout-cout_test)):
            cout=cout_test
        else:
            regulation[val]=r
        T=0.99*T


