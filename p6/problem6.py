import time

n = 100

def main():
    x = sumOfSquares(n)
    y = squareOfSum(n)
    print(y-x)

def sumOfSquares(n):
    sum = 0
    for i in range(n,0,-1):
        sum += i*i
        print(i,sum)
    return sum

def squareOfSum(n):
    sum = int(n*(n+1)/2)
    return sum*sum




start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))