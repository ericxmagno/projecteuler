import time
import math 

n=10001
def main():
    print(prime(n))

def prime(n):
    counter = 3
    num = 5
    i = 3
    while counter <= n:
        while True:
            if num%i==0:
                num+=2
                i=3
                continue
            if i >= math.sqrt(num):
                # print(i,counter, num)
                if counter == n:
                    return(counter,num)
                counter+=1
                num+=2
                i=3
                break
            i+=2

        

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))