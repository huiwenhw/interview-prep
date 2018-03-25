'''
https://leetcode.com/problems/count-and-say/
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.
'''

def countAndSay(n):
    prev = '1'
    for i in range(1, n):
        currel, count, newstr = prev[0], 1, ''
        for k in range(1, len(prev)):
            if currel == prev[k]:
                count += 1
            else:
                newstr += str(count) + currel
                count = 1
                currel = prev[k]
        newstr += str(count) + currel
        prev = newstr
    return prev

print(countAndSay(6)) # 312211

# using ''.join(arr) is faster then concatenating strings in python
def countAndSay(n):
    prev = '1'
    for i in range(1, n):
        currel, count, newstr = prev[0], 1, []
        for k in range(1, len(prev)):
            if currel == prev[k]:
                count += 1
            else:
                newstr.append(str(count))
                newstr.append(currel)
                count = 1
                currel = prev[k]
        newstr.append(str(count))
        newstr.append(currel)
        prev = ''.join(newstr)
    return prev

print(countAndSay(6)) # 312211
