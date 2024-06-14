def f(x):
    return 2*x**3

def rectangle( f,a,b,n):
    h=(b-a)/n
    u=a
    s=0
    for k in range(n):
        s+=f(u)
        u+=h
    return h*s
print("méthode des rectangles: "+str(rectangle(f,0,3,10)))

def trapeze(f,a,b,n):
    h=(b-a)/n
    u=a+h
    s=(f(a)+f(b))/2
    for k in range(n-1):
        s+=f(u)
        u+=h
    return h*s
print("méthode du trapeze: "+str(trapeze(f,0,3,10)))


def simpson(f,a,b,n) :
    S=0
    for i in range (0,n) :
        xi=a+(b-a)*i/n
        xj=a+(b-a)*(i+1)/n
        S+=(xj-xi)*(f(xi)+4*f((xi+xj)/2.0)+f(xj))/6.0
        return S
print("méthode de simpson: "+str(simpson(f,0,3,1)))
