import time
import math

dict = {}
def main():
    x = 20
    smallestmultiple(x)

def smallestmultiple(x):
    for i in range(1,x+1):
        # print(i,x)
        factors = getFactors(i)
        for k in factors:
            if k in dict:
                if dict[k] < factors[k]:
                    dict[k] = factors[k]
            else:
                dict[k] = 1
    total = 1
    for k,v in dict.items():
        # print(total)
        total *= k**v
    # print(dict)
    print(total)

def getFactors(x):
    factors = {}
    i=3
    while x%2==0:
        if 2 in factors:
            factors[2] += 1
        else:
            factors[2] = 1
        x/=2
    while i <= x:
        if x%i==0:
            if i in factors:
                factors[i]+=1
            else:
                factors[i]=1
            x/=i
            i=3
            continue
        i+=2
    # print(x, factors)
    return factors

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))