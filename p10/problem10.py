import time
import math

n=2000000
def main():
    print(primeTotal(n))

def primeTotal(n):
    total = 2

    for i in range(3,n+1,2):
        prime = True
        # if i == 3:
        #     total += i
        #     continue
        for j in range(3,int(math.ceil(math.sqrt(i))+1),2):
            if i % j == 0:
                prime = False
                break
        if prime == True:
            # print(total, i)
            total += i
    return total



start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))