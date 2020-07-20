def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    else:
        return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = len(arr)-1
    while end >= start:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid
    else:
        return -1  # not found
