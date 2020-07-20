# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(len(arr) - 1):
        smallest_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped_this_cycle = True
    while swapped_this_cycle:
        swapped_this_cycle = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped_this_cycle = True

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None): # O(n)
    # Determine maximum if needed: O(n)
    if not maximum:
        maximum = 0
        for item in arr:
            if item > maximum:
                maximum = item
    if len(arr) < 2:
        return arr
    # Create counting array: O(n)
    counting_array = [0] * (maximum + 1)
    for item in arr:
        if item < 0:
            return "Error, negative numbers not allowed in Count Sort"
        counting_array[item] += 1
    # Create sorted array O(1)
    output_array = []
    for i in range(len(counting_array)):
        if counting_array[i] != 0:
            output_array.extend([i]*counting_array[i])

    return output_array
