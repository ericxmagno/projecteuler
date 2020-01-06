import time

nums = {}

def main():
    n = 1000000
    longest = 0
    n = 0
    for i in range(1000000):
        print(i)
        x = getCollatz(i)
        if x > longest:
            longest = x
            n = i
    print(n, x)

def getCollatz(i):
    temp = i
    count = 1
    while temp > 1:
        if temp % 2 == 0:
            count += 1
            temp/=2
        else:
            count += 1
            temp = temp * 3 + 1
        if temp in nums:
            count += nums[temp]
            break
        else:
            count += 1

    nums[i] = count
    return count




start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))