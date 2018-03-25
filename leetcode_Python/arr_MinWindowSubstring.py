'''
https://leetcode.com/problems/minimum-window-substring/description/
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
If there is no such window in S that covers all characters in T, return the empty string "".
'''

from collections import defaultdict, deque

# O(n^2) cause of the remove
def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    mapp = defaultdict(deque) # ch: index
    l = [] # list of indexes of t in s
    d = {} # ch: freq 
    length = len(t)
    minstart, minend = 0, float('inf')

    for ch in t:
        d[ch] = d.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if ch in d and d[ch] > 0:
            d[ch] -= 1
            l.append(i)
            mapp[ch].append(i)
        elif ch in d and d[ch] == 0:
            l.remove(mapp[ch][0])
            mapp[ch].popleft()
            mapp[ch].append(i)
            l.append(i)
        if len(l) == length:
            start, end = l[0], l[-1]
            if ((end - start) < (minend - minstart)):
                minstart, minend = start, end
        #     print('start ', start, ' end ', end, ' minstart ', minstart, ' minend ', minend)
        # print('i ', i, ' ch ', ch, ' d ', d, ' mapp ', mapp, ' l ', l)

    if l == [] or len(l) < len(t): return ""
    return s[minstart:minend+1]

print(minWindow('cabwefgewcwaefgcf', 'cae')) # cwae
print(minWindow('ADOBECODEBANC', 'ABC')) # BANC
