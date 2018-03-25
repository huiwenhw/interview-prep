# Swaps elements from 0...sorted index, bringing max to the end each time
# Best: O(n) sorted arr, Worst: O(n^2), In-place, Stable, Extra O(1)
def bubblesort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for k in range(n-i-1):
            if arr[k] > arr[k+1]:
                swapped = True
                arr[k], arr[k+1] = arr[k+1], arr[k]
        # if arr is sorted, don't need to spend time going through the arr again
        if not swapped: break
        print(arr)

arr = [64, 90, 34, 25, 12, 22, 11]
bubblesort(arr)
print('sorted arr: ', arr)

