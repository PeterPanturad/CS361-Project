#merge sort
import random
import numpy as np #to make random number
import time #to record time
import matplotlib.pyplot as plt
#general code taken from https://www.geeksforgeeks.org/dsa/3-way-merge-sort/
def merge3Way(arr, left, mid1, mid2, right):
    n1 = mid1 - left + 1
    n2 = mid2 - mid1
    n3 = right - mid2
    L = [0] * n1   
    M = [0] * n2
    R = [0] * n3

    i = j = k = 0 # Pointers for L, M, R
    l = left

    #Compare all three and pick the smallest
    while i < len(L) and j < len(M) and k < len(R):
        if L[i] <= M[j] and L[i] <= R[k]:
            arr[l] = L[i]; i += 1
        elif M[j] <= L[i] and M[j] <= R[k]:
            arr[l] = M[j]; j += 1
        else:
            arr[l] = R[k]; k += 1
        l += 1

    #If one array is empty, merge the remaining two 2 way merge
    while i < len(L) and j < len(M):
        if L[i] <= M[j]:
            arr[l] = L[i]; i += 1
        else:
            arr[l] = M[j]; j += 1
        l += 1

    while j < len(M) and k < len(R):
        if M[j] <= R[k]:
            arr[l] = M[j]; j += 1
        else:
            arr[l] = R[k]; k += 1
        l += 1

    while i < len(L) and k < len(R):
        if L[i] <= R[k]:
            arr[l] = L[i]; i += 1
        else:
            arr[l] = R[k]; k += 1
        l += 1

    # last array          #section taken from geeks for geeks 3 way merger immplementation
    while i < len(L):
        arr[l] = L[i]
        i += 1
        l += 1
    while j < len(M):
        arr[l] = M[j]
        j += 1
        l += 1
    while k < len(R):
        arr[l] = R[k]
        k += 1
        l += 1

def threewaymerger(arr, left, right):
    if left < right:
        # Divide into three parts
        mid1 = left + (right - left)// 3
        mid2 = left + 2 * (right - left) //3

        #used to have two recursive calls
        #orginal merge sort is aarry, most left, and most right
        #
        threewaymerger(arr, left, mid1)
        threewaymerger(arr, mid1 + 1, mid2)
        threewaymerger(arr, mid2 + 1, right)

        # A new merge function for 3
        merge3Way(arr, left, mid1, mid2, right)

#lets generate numbers and use merge

Powers=[]
Times=[]
Powers_dp=[]
Times_dp=[]
print("normal")
for i in range(31):
    arr = np.random.randint(0, 10, size=2**i)
    start_time=time.time()
    threewaymerger(arr, 0,len(arr)-1)
    end_time=time.time()
    #end of timer
    Powers.append(i)
    Times.append(end_time-start_time)
    print(f" 2^{i} took {end_time-start_time} seconds")
print("double precision")
for i in range(31): #30 should be the max due to tie constrains
    arr = np.random.uniform(0, 10, size=2**i).astype(np.float64) #64 is doube precisions
    start_time=time.time()
    threewaymerger(arr, 0,len(arr)-1)
    end_time=time.time()
    #end of timer
    Powers_dp.append(i)
    Times_dp.append(end_time-start_time)
    print(f" 2^{i} took {end_time-start_time} seconds")

plt.figure(figsize=(10, 6))
plt.plot(Powers, Times, marker='o', label='Integers (int)')
plt.plot(Powers_dp, Times_dp, marker='s', linestyle='--', label='Double Precision (float64)')

plt.xlabel('Input Size (Log Scale: $2^{i}$)')
plt.ylabel('Time (seconds)')
plt.title('Performance Comparison: 3-Way Merge Sort')
plt.xticks(Powers)
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.5)

# Save or show the plot
plt.savefig('merge_sort_plot.png')
plt.show()
