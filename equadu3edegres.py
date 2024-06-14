#résolution d'une équation du 3e degré
from math import cos,sin,pi,acos
from cmath import*

def décompsition(a,b,c,d,r):
    L=[]
    L.append(a)
    L.append(r*a+b)
    L.append(r**2*a+r*b+c)
    return L


a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
d=int(input("d= "))
assert(a!=0)
print(str(a)+"*x^3+"+str(b)+"*x^2+"+str(c)+"*x+"+str(d)+"=0")


p=(c/a-b**2/(3*a**2))
q=(2*b**3/(27*a**3)+d/a-b*c/(3*a**2))
print("X^3+"+str(p)+"*X+"+str(q)+"=0")


if p==0 and q==0:
    if -b/(3*a)<0:
        print(str(a)+"*(x+"+str(b/(3*a))+")^3=0")
    else:
        print(str(a)+"*(x-"+str(b/(3*a))+")^3=0")

elif p==0:
    X=(-q)**(1/3)
    x=X-b/(3*a)
    L=décompsition(a,b,c,d,x)
    if x<0:
        print(str(a)+"*(x+"+str(-x)+")*("+str(L[0])+"*x^2+"+str(L[1])+"*x+"+str(L[2])+")=0")
    else:
        print(str(a)+"*(x-"+str(x)+")*("+str(L[0])+"*x^2+"+str(L[1])+"*x+"+str(L[2])+")=0")

elif q==0:
    x1=-b/(3*a)
    if p<=0:
        x2=(-p)**(1/2)-b/(3*a)
        x3=-(-p)**(1/2)-b/(3*a)
        print(str(a)+"*(x-("+str(x1)+"))*(x-("+str(x2)+"))*(x-("+str(x3)+"))=0")
    else:
        print(str(a)+"*(x-("+str(x1)+"))*(x**2+"+str(p)+")=0")


else:
    delta=4*p**3+27*q**2
    j=-1/2+(3)**(1/2)/2*1j
    if delta>0:
        if -q+(delta/27)**(1/2)>0 and -q-(delta/27)**(1/2)>0:
            print("v")
            x1=((-q+(delta/27)**(1/2))/2)**(1/3)+((-q-(delta/27)**(1/2))/2)**(1/3)-b/(3*a)
            x2=j*((-q+(delta/27)**(1/2))/2)**(1/3)+j**2*((-q-(delta/27)**(1/2))/2)**(1/3)-b/(3*a)
            x3=j**2*((-q+(delta/27)**(1/2))/2)**(1/3)+j*((-q-(delta/27)**(1/2))/2)**(1/3)-b/(3*a)
            print(str(a)+"*(x-("+str(x1)+"))*(x-("+str(x2)+"))*(x-("+str(x3)+"))=0")

        if -q+(delta/27)**(1/2)>0 and -q-(delta/27)**(1/2)<0:
            print("n")
            x1=((-q+(delta/27)**(1/2))/2)**(1/3)-((+q+(delta/27)**(1/2))/2)**(1/3)-b/(3*a)
            x2=j*((-q+(delta/27)**(1/2))/2)**(1/3)-j**2*((q+(delta/27)**(1/2))/2)**(1/3)-b/(3*a)
            x3=j**2*((-q+(delta/27)**(1/2))/2)**(1/3)-j*((q+(delta/27)**(1/2))/2)**(1/3)-b/(3*a)
            print(str(a)+"*(x-("+str(x1)+"))*(x-("+str(x2)+"))*(x-("+str(x3)+"))=0")

        if -q+(delta/27)**(1/2)<0 and -q-(delta/27)**(1/2)<0:
            print("h")
            x1=-(((q-(delta/27)**(1/2))/2)**(1/3)+((q+(delta/27)**(1/2))/2)**(1/3))-b/(3*a)
            x2=-(j*((q-(delta/27)**(1/2))/2)**(1/3)+j**2*((q+(delta/27)**(1/2))/2)**(1/3))-b/(3*a)
            x3=-(j**2*((q-(delta/27)**(1/2))/2)**(1/3)+j*((q+(delta/27)**(1/2))/2)**(1/3))-b/(3*a)
            print(str(a)+"*(x-("+str(x1)+"))*(x-("+str(x2)+"))*(x-("+str(x3)+"))=0")

    if delta<0:
        u0=((-q+1j*(abs(delta)/27)**(1/2))/2)**(1/3)
        x0=u0+u0.conjugate()-b/(3*a)
        x1=j*u0+(j*u0).conjugate()-b/(3*a)
        x2=j**2*u0+(j**2*u0).conjugate()-b/(3*a)
        print(str(a)+"*(x-("+str(round(x0.real,3))+"))*(x-("+str(round(x1.real,3))+"))*(x-("+str(round(x2.real,3))+"))=0")

    if delta==0:
        x1=(-p/3)**(1/2)-b/(3*a)
        x2=-(-p/3)**(1/2)-b/(3*a)
        x3=3*q/p
        print(str(a)+"*(x-("+str(x1)+"))*(x-("+str(x2)+"))*(x-("+str(x3)+"))=0")

