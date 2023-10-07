import random
from timeit import default_timer as timer  # library import

start = timer()


def partition(arr, left, right, pivot):  # partition around the pivot element
    pivot_no = arr[pivot]
    arr[pivot], arr[right] = arr[right], arr[pivot]
    store_index = left

    for i in range(left, right):
        if arr[i] < pivot_no:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1

    arr[right], arr[store_index] = arr[store_index], arr[right]
    return store_index


# recursive call function which is called until k is found around the pivot
def select(arr, left, right, k):
    if left == right:
        return arr[left]

    num_of_elements = right - left + 1

    # Divide the input of the array into sub lists (5)
    sublists = []
    for i in range(left, right + 1, 5):
        sublist = arr[i:i + 5]
        sublists.append(sublist)
    medians = [sorted(sub)[len(sub) // 2] for sub in sublists]

    # Find the median of medians recursively
    median_of_medians = select(medians, 0, len(medians) - 1, len(medians) // 2)

    # Part the array given by the user around the median of medians
    pivot = arr.index(median_of_medians)
    pivot = partition(arr, left, right, pivot)

    if k == pivot:
        return arr[k]
    elif k < pivot:
        return select(arr, left, pivot - 1, k)
    else:
        return select(arr, pivot + 1, right, k)


n = 1000  # Number of elements
k = 5


arr = []
for _ in range(n):
    arr.append(random.randint(1, 100))
result = select(arr, 0, n - 1, k - 1)

arr.sort()  # Sort the array for comparing it
print(f"The {k}th smallest element in the given array is: {result}") 
end = timer()   # get the execution time
print(end - start)
