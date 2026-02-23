import math
import time
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from dataset import data_set

def numpy_sort(L):
    return np.sort(L)

def merge_sort(L):
    def abc (L1, L2):
        temp = []
        i, j = 0, 0
        a = len(L1)
        b = len(L2)
        while i != a and j != b:
            if L1[i] < L2[j]:
                temp.append(L1[i])
                i = i + 1 
            else:
                temp.append(L2[j])
                j = j + 1
        if i == a:
            temp = temp + L2[j:]
        elif j == b:
            temp = temp + L1[i:]
        return temp

    def xyz(a, b):
        if a == b:
            return [L[a]]
        middle = (a + b) // 2
        return abc(xyz(a, middle), xyz(middle + 1, b))

    return xyz(0, len(L) - 1)

def quick_sort(L):
    def median_of_three(a, b, c):
        if a < b:
            if b < c:
                return b
            return c if a < c else a
        else:
            if a < c:
                return a
            return c if b < c else b

    def partition(low, high):
        mid = (low + high) // 2
        pivot = median_of_three(L[low], L[mid], L[high])

        if pivot == L[mid]:
            L[mid], L[high] = L[high], L[mid]
        elif pivot == L[low]:
            L[low], L[high] = L[high], L[low]

        i = low - 1
        for j in range(low, high):
            if L[j] <= pivot:
                i += 1
                L[i], L[j] = L[j], L[i]

        L[i+1], L[high] = L[high], L[i+1]
        return i + 1

    def helper(low, high):
        while low < high:
            pi = partition(low, high)
            if pi - low < high - pi:
                helper(low, pi - 1)
                low = pi + 1
            else:
                helper(pi + 1, high)
                high = pi - 1

    helper(0, len(L) - 1)
    return L

def heap_sort(L):
    n = len(L)

    def heapify(n, i):
        while True:
            largest = i
            left = 2*i + 1
            right = 2*i + 2

            if left < n and L[left] > L[largest]:
                largest = left

            if right < n and L[right] > L[largest]:
                largest = right

            if largest == i:
                break

            L[i], L[largest] = L[largest], L[i]
            i = largest

    for i in range(n//2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n-1, 0, -1):
        L[0], L[i] = L[i], L[0]
        heapify(i, 0)

    return L

def get_time(f, data, results):
    overall = 0 
    for i in data:
        arr = i.copy()
        a = time.time()
        f(arr)
        b = time.time()
        results.append(b - a)
        overall = overall + b - a
    results.append(overall)

numpy_results = []
merge_results = []
quick_results = []
heap_results = []

get_time(numpy_sort, data_set, numpy_results)
get_time(merge_sort, data_set, merge_results)
get_time(quick_sort, data_set, quick_results)
get_time(heap_sort, data_set, heap_results)

labels = [f"N{i}" for i in range(1, 11)] + ["Total"]

df = pd.DataFrame({
    "Dataset": labels,
    "NumPy Sort": numpy_results,
    "Merge Sort": merge_results,
    "Quick Sort": quick_results,
    "Heap Sort": heap_results
})

datasets = labels[:-1]

x = np.arange(len(datasets))
width = 0.2

fig, ax = plt.subplots(figsize=(12,6))

bars1 = ax.bar(x - 1.5*width, quick_results[:-1], width, label="Quicksort")
bars2 = ax.bar(x - 0.5*width, heap_results[:-1], width, label="Heapsort")
bars3 = ax.bar(x + 0.5*width, merge_results[:-1], width, label="Mergesort")
bars4 = ax.bar(x + 1.5*width, numpy_results[:-1], width, label="NumPy sort")

ax.set_title("Kết quả thử nghiệm trên bộ dữ liệu")
ax.set_ylabel("Thời gian thực hiện (seconds)")
ax.set_xticks(x)
ax.set_xticklabels(datasets)
ax.legend()

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2,
            height/2,
            f"{height:.3f}",
            ha='center',
            va='center',
            color='black'
        )

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)
add_labels(bars4)

plt.tight_layout()
plt.show()

print(df)