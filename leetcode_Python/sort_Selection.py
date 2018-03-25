# finds min elem, swap with first elem of unsorted subarray
# Best/Worst: O(n^2), Inplace, Stable, Extra O(1) space
# Insertion/Selection: Faster for small arrays
def selection(arr):
    n = len(arr)

    for i in range(n):
        min_i = i
        for k in range(i+1, n):
            if arr[k] < arr[min_i]:
                min_i = k

        # swap min elem with first elem
        arr[i], arr[min_i] = arr[min_i], arr[i]
        print(arr, 'swapping ', arr[i], arr[min_i])

arr = [64, 25, 12, 22, 11]
print(arr, ' original')
selection(arr)
print(arr, ' sorted')
