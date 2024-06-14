import numpy as np

def sousmatrice(A,n):
    return [A[0:n//2,0:n//2],A[0:n//2,n//2:n],A[n//2:n,0:n//2],A[n//2:n,n//2:n]]

def mult(A,B,n):
    if n==1: 
        return A*B
    else:
        L_A=sousmatrice(A,n)
        L_B=sousmatrice(B,n)

        M1=mult(L_A[1]-L_A[3],L_B[2]+L_B[3],n//2)
        M2=mult(L_A[0]+L_A[3],L_B[0]+L_B[3],n//2)
        M3=mult(L_A[0]-L_A[2],L_B[0]+L_B[1],n//2)
        M4=mult(L_A[0]+L_A[1],L_B[3],n//2)
        M5=mult(L_A[0],L_B[1]-L_B[3],n//2)
        M6=mult(L_A[3],L_B[2]-L_B[0],n//2)
        M7=mult(L_A[2]+L_A[3],L_B[0],n//2)

        C11=M1+M2-M4+M6
        C12=M4+M5
        C21=M6+M7
        C22=M2-M3+M5-M7

        if n==1:
            C1=[C11,C12]
            C2=[C21,C22]
        else:
            C1=np.concatenate((C11,C12),axis=1)
            C2=np.concatenate((C21,C22),axis=1)

        return np.concatenate((C1,C2),axis=0)

def matricebonformat(A,n):
    m=0
    while np.log2(n+m)!=int(np.log2(n+m)):
        m+=1
    print(m)
    MId=np.eye(m)
    Zero1=np.zeros((m,n))
    Zero2=np.zeros((n,m))
    N1=np.concatenate((A,Zero2),axis=1)
    N2=np.concatenate((Zero1,MId),axis=1)
    return np.concatenate((N1,N2),axis=0)


A=np.array([[1,3,3,4],[4,2,6,4],[1,8,3,4],[1,2,2,1]])
B=np.array([[2,0,3,0],[0,1,0,2],[4,0,1,0],[0,2,0,4]])
print(mult(A,B,4))
print(A@B)
