# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    if arrA[-1] < arrB[0]:
        merged_arr = arrA + arrB
    else:
        merged_arr = arrB + arrA

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        a = l = r = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                arr[a] = left[l]
                l += 1
            else:
                arr[a] = right[r]
                r += 1
            a += 1

        while l < len(left): 
            arr[a] = left[l] 
            l += 1
            a += 1
          
        while r < len(right): 
            arr[a] = right[r] 
            r += 1
            a += 1

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass