import numpy as np

# quickSort, mergeSort, heapSort, (one of your choice)
# 4 algoritmi de anayzat + raport

#Generate an array for all the algorithms
# randnums= np.random.randint(1,101,40)
numbers = [28, 100, 50, 7, 3, 48, 87, 100, 94, 53, 50, 61, 27, 66, 31, 38, 14, 6, 43, 32,
                34, 54, 19, 8, 12, 49, 83, 3, 33, 82, 5, 61, 93, 71, 25, 67, 27, 43, 91, 76]


# Quiq Sort
# ------------------------------------------------------------------------------------------------------------------------

# function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1


# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)


# Merge sort
# ------------------------------------------------------------------------------------------------------------------------

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i], end=" ")

mergeSort(arr, 0, n - 1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i], end=" ")


# This code is contributed by Mohit Kumra


#  Heap sort
# ------------------------------------------------------------------------------------------------------------------------

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root

    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap

        # Heapify the root.

        heapify(arr, n, largest)


# The main function to sort an array of given size

def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)


# Driver code to test above

arr = [12, 11, 13, 5, 6, 7, ]
heapSort(arr)
n = len(arr)
print('Sorted array is')
for i in range(n):
    print(arr[i])


# This code is contributed by Mohit Kumra


# Insertion Sort
# ------------------------------------------------------------------------------------------------------------------------

def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])


# sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)
