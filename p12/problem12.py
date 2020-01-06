import time
import math

def main():
    n = 500

    factorCount(n)

# Brute force too slow
# def factorCount(n):
#     factors = set()
#     #divide until no longer even
#     count = 1
#     while len(factors) < n:
#         num = getTriangleNum(count)
#         print(num,count)
#         factors.clear()
#         for i in range(1,num/2+1):
#             if num%i==0:
#                 factors.add(i)
#         factors.add(num)
#         print(sorted(factors))
#         count+=1

def factorCount(num):
    factors = dict()
    factCnt = 1
    count = 1
    nHold = 0
    while factCnt < num:
        factCnt = 1
        n = getTriangleNum(count)
        nHold = n
        factors.clear()
        # factors[1] = 1
        # factors[n] = 1
        # print(n, count)
        while n%2==0:
            if not 2 in factors:
                factors[2] = 1
            else:
                factors[2] +=1
            n/=2
        i = 3
        while i <= n:
            if n%i==0:
                n/=i
                if not i in factors:
                    factors[i] = 1
                else:
                    factors[i] += 1
                i = 3
                continue
            i+=2
        count+=1
        for i in factors:
            factCnt *= factors[i]+1
        print(factors)
        print(nHold, count, factCnt)
    print(factors)
    print(nHold, count, factCnt)

def getTriangleNum(n):
    num = 0
    for i in range(1, n+1):
        num += i
    return num


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))