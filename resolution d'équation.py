def f(x):
    return 2*(x)**2-8

def df(x):
    return 4*x


#Méthode de Dichotomie
def dicho(f,a,b,epsi):
    while b-a > epsi:
        c=(a+b)/2
        if f(a)*f(c)<=0:
            b=c
        else:
            a=c
    return [a,b]
print("Méthode de Dichotomie: "+str(dicho(f,1,3,0.001)))

#Méthode de Lagrange
def Lagrange(f,a,b,epsi):
    ac=a
    c=b
    while abs(c-ac)> epsi:
        ac=c
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        if f(a)*f(c)<=0:
             b=c
        else:
             a=c
    return  c
print("Méthode de Lagrange: "+str(Lagrange(f,1,3,0.001)))

#Méthode de  Newton
def Newton1(f,df,a,b,epsi):
    ac=a
    c=b
    while abs(ac-c)> epsi:
        ac=c
        c=ac-f(ac)/df(ac)
        if f(a)*f(c)<=0:
            b=c
        else:
            a=c
    return c
print(Newton1(f,df,1,3,0.001))

