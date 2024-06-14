#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
# Author:      Marie SENGLER
# Created:     04/09/2023
# Copyright:   (c) Marie SENGLER 2023
#-------------------------------------------------------------------------------

from time import time
from math import floor

def main():
    pass

if __name__ == '__main__':
    main()

def algo_trivial(x,n):
    if n==1:
        return x
    else:
        return x*algo_trivial(x,n-1)

def algo_parite(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    if n%2==0:
        return algo_parite(x,n//2)**2
    else:
        return x*algo_parite(x,(n-1)//2)**2

def algo_binaire(x,n):
    y,z,m=x,1,n
    #print("m : "+str(m)+" , y : "+str(y)+" , z : "+str(z))
    while n>1:
        m=floor(n/2)
        if n>2*m:
            z*=y
        n=m
        y*=y
        #print("m : "+str(m)+" , y : "+str(y)+" , z : "+str(z))
    return z*y

print(algo_trivial(5,24))
print(algo_parite(5,24))
print(algo_binaire(5,24))



