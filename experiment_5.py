import os
import time

def for_loop(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

def while_loop(n):
    sum = 0
    i = 1
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum

n_values = [10, 100, 1000, 10000, 100000]

for n in n_values:
    start_time = time.time()
    result = for_loop(n)
    end_time = time.time()
    print(f"For loop sum of {n} numbers: {result}, execution time: {end_time - start_time:.6f} seconds")

    start_time = time.time()
    result = while_loop(n)
    end_time = time.time()
    print(f"While loop sum of {n} numbers: {result}, execution time: {end_time - start_time:.6f} seconds")
    print("=" * 78)
    
os.system("pause")