'''
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example 
For a = [2, 3, 3, 1, 5, 2], the output should be
firstDuplicate(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than than second occurrence of 2 does, so the answer is 3.

For a = [2, 4, 3, 5, 1], the output should be
firstDuplicate(a) = -1.
'''

import collections 

# once we find the first element, we return 
def firstDuplicate(a):
    if sum(a) == (len(a)*(len(a)+1))/2:
        return -1
    d = collections.defaultdict(int)
    index, element = float('inf'), -1
    for i in range(len(a)):
        if a[i] in d:
            element = a[i]
            break
        d[a[i]] = 1
    return element

# use array element to check if there's duplicate
# use abs(a[i]) so we use the original element and not the 'marked' one 
# if arr = [2,3,3,1,5,2], 
# after first round = [2,-3,3,1,5,2] # arr[1] (arr[2]-1) is marked as visited by * -1
def firstDuplicate_short(a):
    for i in range(len(a)):
        if a[abs(a[i])-1]<0:
            return abs(a[i])
        else:
            a[abs(a[i])-1] *= -1
    return -1

a = [2,3,3,1,5,2]
print(firstDuplicate(a))
a = [2,1,3,3,5,2]
print(firstDuplicate_short(a))
