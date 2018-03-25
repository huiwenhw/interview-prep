'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Given a string, find the length of the longest substring without repeating characters.

i, ch, start, maxlen, d
0 p 0 1 {'p': 0}
1 w 0 2 {'w': 1, 'p': 0}
2 w 2 2 {'w': 1, 'p': 0}
3 k 2 2 {'w': 1, 'p': 0, 'k': 3}
4 e 2 3 {'w': 1, 'p': 0, 'k': 3, 'e': 4}
5 w 2 4 {'w': 1, 'p': 0, 'k': 3, 'e': 4}
'''

# O(n) time and space, where n = num of chars in s
def substring_short(s):
    d = {}
    start, maxlen = 0, 0
    for i, ch in enumerate(s):
        if ch in d:
            start = max(start, d[ch] + 1)
        d[ch] = i
        maxlen = max(maxlen, i - start + 1)
    return maxlen

print(substring_short('abba')) # 2
print(substring_short('pwwkew')) # 3
        
def substring(s):
    start, end = 0, len(s)
    ans = set()
    length, maxlen, i = 0, 0, 0
    while start < end: 
        if s[start] not in ans:
            ans.add(s[start])
            length += 1
            # print('s[start] ', s[start], ' length ', length, ' ans ', ans)
        else:
            maxlen = max(length, maxlen)
            while i < start:
                if s[i] == s[start]:
                    i += 1 
                    length -= 1
                    break
                ans.remove(s[i])
                i += 1 
                length -= 1
            length += 1
            # print('i ', i, ' s[start] ', s[start], ' length ', length, ' ans ', ans)
        start += 1
    maxlen = max(length, maxlen)
    return maxlen

print(substring('abcabcbb')) # 3
print(substring('bbbbb')) # 1
