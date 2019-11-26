import time

dict = {}
def main():
    r = range(100,999)
    for x in r:
        for y in r:
            if isPalindrome(x*y):
                dict[x*y] = (x,y)
    maxPal = max(k for k,v in dict.items())
    print(maxPal, dict.get(maxPal))


def isPalindrome(n):
    if str(n) == ''.join(reversed(str(n))):
        return True
    else:
        return False

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))