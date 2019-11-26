import time
import math

def main():
    n = 63

    primefactor(n)

def primefactor(n):
    factors = set()
    #divide until no longer even
    while n%2==0:
        factors.add(2)
        n/=2
    i = 3
    print(n)
    while i <= n:
        if n%i==0:
            factors.add(i)
            n/=i
            i = 3
            continue
        i+=2
    print(sorted(factors))
    print(max(factors))


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))