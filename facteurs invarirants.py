

matrice_test=[[2,4],[6,8]]
#print(matrice_test)
def find_min(matrice,i): # ok marche
    n = len(matrice)
    p= len(matrice[0])
    k,l=-1,-1
    for ii in range(i,n):
        for j in range(i,p):
            if (abs(matrice[ii][j])<abs(matrice[k][l]) or k==-1)and matrice[ii][j]!=0: #le plus petit en valeur absolue
                k,l=ii,j 
    if matrice[k][l]==0:
        return -2,-2
    return k,l


#print(find_min(matrice_test))

def switch_ligne(matrice,i,j):
    n = len(matrice[0])
    for k in range(n):
        matrice[i][k],matrice[j][k]=matrice[j][k],matrice[i][k]
    

#print(switch_ligne(matrice_test,0,1))
#print(matrice_test)

def switch_colonne(matrice,i,j):
    n = len(matrice)
    for k in range(n):
        matrice[k][i],matrice[k][j]=matrice[k][j],matrice[k][i]
        
def operation_ligne(matrice,i,j,facteur):
    n=len(matrice)
    m=len(matrice[0])
    for k in range(m):
        matrice[i][k]= matrice[i][k] +matrice[j][k]*facteur 

def operation_colonne(matrice,i,j,facteur):
    n=len(matrice)
    m=len(matrice[0])
    for k in range(n):
        matrice[k][i]= matrice[k][i] +matrice[k][j]*facteur 

#print(switch_colonne(matrice_test,0,1))
#print(matrice_test)

def Div_eucl_colonne(matrice,i): # i est le numéro de l'étape # 
    #problème il faut aussi la faire sur le reste de la matrice
    n=len(matrice)
    m=len(matrice[0])
    operation=[0 for i in range(n)]
    min=matrice[i][i]
    for k in range(i+1,n): # on obtient les opérations faites sur la premières colonne
        operation[k]= matrice[k][i]//min 
        matrice[k][i]= matrice[k][i]%min
    # on les fait sur le reste des colonnes
    for j in range(i+1,m):
        v=matrice[i][j]
        for k in range(i+1,n):
            matrice[k][j]= matrice[k][j] - operation[k]*v
    return operation 

def Div_eucl_ligne(matrice,i):# i est le numéro de l'étape
    n=len(matrice)
    m=len(matrice[0])
    operation=[0 for i in range(m)]
    min=matrice[i][i]
    for k in range(i+1,m):
        operation[k]= matrice[i][k]//min 
        matrice[i][k]= matrice[i][k]%min
        
    for j in range(i+1,n):
        v=matrice[j][i]
        for k in range(i+1,m):
            matrice[j][k]= matrice[j][k] - operation[k]*v
    return operation 
    
def test_fini_colonne_k(matrice,k):
    n=len(matrice)
    m=len(matrice[0])
    for i in range(k+1,n):
        if matrice[i][k]!=0:
            return False  
    return True
#print(test_fini_colonne_k([[4,6],[2,2]],0))

def test_fini_ligne_k(matrice,k):
    n=len(matrice)
    m=len(matrice[0])
    for j in range(k+1,m):
        if matrice[k][j]!=0:
            return False    
    return True

def test_fini_stage_k(matrice,k):
    return test_fini_colonne_k(matrice,k) and test_fini_ligne_k(matrice,k)

def test_end(matrice):
    n,m=len(matrice),len(matrice[0])
    p=min(n,m)
    for i in range(p-1):
        if matrice[i][i]%matrice[i-1][i-1]!=0:
            return False
    return True

def test_divisibilité(matrice,i):
    n=len(matrice)
    m=len(matrice[0])
    for j in range(i+1,n):
        for k in range(i+1,m):
            if matrice[j][k]%matrice[i][i]!=0:
                return j,k 
    return -1,-1
    
def algo_thmstructure(matrice):
    n=len(matrice) # lignes
    m=len(matrice[0]) # colonnes
    P=[[0 for i in range(m)] for j in range(n)] # matrice p des opérations sur les lignes , pas fait au final mais on pas long à rajouter
    p=min(n,m)
    c=100
    i=0
    while i<p and i<c:
        b=True# test pour savoir s'il les coefs sont nuls sauf celui sur la diagonale
        j=0
        while b and j<c:
            k,l=find_min(matrice,i) #minimum dans la matrice réduite j,k>=i
            if (k,l)==(-2,-2):
                b=False 
                break
            switch_ligne(matrice,i,k)
            switch_colonne(matrice,i,l)
            Div_eucl_colonne(matrice,i)
            if test_fini_colonne_k(matrice,i):
                b=False
            j=j+1
        b=True
        j=0
        while b and j<c:
            k,l=find_min(matrice,i) #minimum dans la matrice réduite j,k>=i
            if (k,l)==(-2,-2):
                b=False 
                break
            switch_ligne(matrice,i,k)
            switch_colonne(matrice,i,l)
            Div_eucl_ligne(matrice,i)
            if test_fini_ligne_k(matrice,i):
                b=False
            j=j+1
        # cas d1 ne divise pas d2
        j,k=test_divisibilité(matrice,i)
        if j!=-1: 
            operation_ligne(matrice,i,j,1)
        elif test_fini_stage_k(matrice,i):
            i=i+1
            
    # pour retourner des coefs positives
            
    return [abs(matrice[i][i]) for i in range(p)] # retourne la liste des facteurs invariants de la matrice

test1=matrice_test
test2=[[1,0],[1,1]]
test3=[[4,6],[10,14]] #ok
test4=[[2,3],[5,7]] # ok
test5=[[2,4],[1,2]]
test6=[[2,4,6],[4,8,12],[1,2,3]]
test7=[[3,6,9],[6,15,21],[3,9,12]]
#print(find_min(test5,0))

# à faire : d1 | d2 et matrice rectangulaire
test8=[[2,0],[0,3]]
test9=[[6,0],[0,15]]
test10=[[4,0,0],[0,6,0],[0,0,9]]
#print(operation_ligne(test8,0,1,1))
print(test8)

# test rectangulaire
test11=[[2,4,6],[6,8,10]] # ok 
test12=[[2,4],[4,8],[6,12]]
A=[[2,4,4,6],[6,10,8,14],[4,6,6,8]]
print(algo_thmstructure(test1)) # problème matrice pas carré
