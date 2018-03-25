# Takes curr, moves elem up the list, places elem at found position in front
# Best O(n), Worst O(n^2) when reversed, In-place, Stable, Extra O(1)
# Insertion/Selection: Faster for small arrays
def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        k = i-1

        # using k to move elements up the list
        while k >= 0 and key < arr[k]:
            arr[k+1] = arr[k]
            k -= 1
        arr[k+1] = key
        print(arr, ' moving: ', key)

arr = [12, 11, 13, 5, 6]
insertion(arr)
print('sorted: ', arr)
