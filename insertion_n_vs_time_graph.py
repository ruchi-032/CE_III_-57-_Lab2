from insertion_sort import insertion_sort

import random
from time import time
import matplotlib.pyplot as plt

n = 1000
time_best_case = []
time_average_case = []
time_worst_case = []
size = []

for i in range(n, n*20, n):
    size.append(i)
    randomvalues = random.sample(range(i), i)
    
    #for best case
    startTime_best = time()
    a = list(range(i))
    insertion_sort (a)
    endTime_best = time()
    totalTime_best = endTime_best - startTime_best
    time_best_case.append(totalTime_best)
    
    #for average case
    startTime_average = time()
    insertion_sort (randomvalues)
    endTime_average = time()
    totalTime_average = endTime_average - startTime_average
    time_average_case.append(totalTime_average)
    
    #for worst case
    startTime_worst = time()
    d = list(range(i))[::-1]
    insertion_sort(d)
    endTime_worst = time()
    totalTime_worst = endTime_worst - startTime_worst
    time_worst_case.append(totalTime_worst)
    
fig, ax = plt.subplots(1,1)
ax.plot(size, time_best_case, label='Best Case')
ax.plot(size, time_average_case, label='Average Case')
ax.plot(size, time_worst_case, label='Worst Case')

legend = ax.legend(loc = 'upper center', shadow = True, fontsize = 'small')
plt.show()