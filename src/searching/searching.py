import math
# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if len(arr) > 0:
        mid = math.ceil((start + (end - 1)) / 2)
        if arr[mid] < target:
            return binary_search(arr, target, mid, end)
        elif arr[mid] > target:
            return binary_search(arr, target, 0, mid)
        elif arr[mid] == target:
            return mid
    return -1
    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

def agnostic_binary_search(arr, target):
    if len(arr) > 0:
        ascend = True
        if(arr[-1] < arr[0]):
            ascend = False
        start = 0
        end = len(arr)-1
        while end >= start:
            mid = math.ceil((start + end - 1) / 2)
            if arr[mid] == target:
                return mid
            if arr[mid] > target:
                if ascend:
                    end = mid - 1
                else:
                    start = mid + 1
            elif arr[mid] < target:
                if ascend:
                    start = mid + 1
                else:
                    end = mid -1

    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(agnostic_binary_search(arr, 1))
print(agnostic_binary_search(arr2, 1))