from math import sqrt
def isprime(n):
    if n == 1:
        return False
    if n==2:
        return True
    x = int(sqrt(n))+1
    for t in range(2,x+1):
        if n%t==0:
            return False
    return True