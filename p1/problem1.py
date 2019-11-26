import time


def brute():
    x = 1000
    n = 0

    for i in range(1,x):
        if i % 3 == 0 or i % 5 == 0:
            n+=i
    print(f"brute force sol: {n}")

start_time = time.time()
brute()
print("--- %s seconds ---" % (time.time() - start_time))