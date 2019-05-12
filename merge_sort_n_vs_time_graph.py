from merge_sort import mergeSort

import random
from time import time
import matplotlib.pyplot as plt

size = []
t = []
n = 1000000
for i in range(n, n*10, n):
    randomvalues = random.sample(range(i), i)
    start_time = time()
    mergeSort(randomvalues, 0, len(randomvalues) - 1)
    end_time = time()
    total_time = end_time - start_time
    
    size.append(i)
    t.append(total_time)
    
print(size)
print(t)
plt.plot(size, t)
plt.show()
