'''
https://leetcode.com/problems/is-subsequence/description/
Given a string s and a string t, check if s is subsequence of t.
e.g. s = "abc", t = "ahbgdc"
Return true.
'''

# will go through the entire t to check if 'x' exists. it doesn't exist, t comes to the end
# so StopIteration will be raised and subsequently all c are False
def is_subseq_short(s, t):
    t = iter(t)
    return all(c in t for c in s)

# If curr char is not in t, then we return False
# Else, we take the substring of t and start from there
def is_subseq_s(s, t):
    for c in s:
        i = t.find(c)
        if i == -1:
            return False
        else:
            t = t[i+1:]
    return True

# got TLE
def is_subseq(s, t):
    if s == '': return True
    sets = set()
    sets.add('')
    for ch in t:
        newsets = set()
        for st in sets:
            newstr = st + ch
            newsets.add(newstr)
        sets.update(newsets)
    sets.remove('')
    if s in sets: return True
    return False

print(is_subseq('abc', 'ahbgdc')) # True
print(is_subseq('axc', 'ahbgdc')) # False
print(is_subseq_s('abc', 'ahbgdc')) # True
print(is_subseq_s('axc', 'ahbgdc')) # False
print(is_subseq_short('abc', 'ahbgdc')) # True
print(is_subseq_short('axgd', 'ahbgdc')) # False, will give [T,F,F]
