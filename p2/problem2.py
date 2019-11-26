import time

limit = 4000000

def dynamic(n1, n2):
    if n1 >= 4000000:
        return 0
    else:
        if n1%2==0:
            return n1 + dynamic(n2, n1+n2)
        else:
            return 0 + dynamic(n2, n1+n2)

start_time = time.time()
print(dynamic(1,2))
print("--- %s seconds ---" % (time.time() - start_time))