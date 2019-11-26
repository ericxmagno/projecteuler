import time
import math

def main():
    n = 600851475143

    primefactor(n)

def primefactor(n):
    factors = set()
    #divide until no longer even
    while n%2==0:
        factors.add(2)
        n/=2
    i = 3
    while i <= math.sqrt(n):
        if n%i==0:
            factors.add(i)
            n/=i
            i = 3
        i+=2
    factors.add(int(n))
    print(sorted(factors))
    print(max(factors))


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))