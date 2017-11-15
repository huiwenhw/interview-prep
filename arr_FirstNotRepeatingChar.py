'''
Given a string s, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.
Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you would be asked to do during a real interview.
'''

# O(n) time and space
def first(s):
    if not s: return '_'
    d = {}
    for i in range(len(s)):
        ch = s[i]
        if ch not in d:
            d[ch] = [0, i]
        d[ch] = [d[ch][0]+1, i]
    index, key = float('inf'), ''
    for k, v in d.items():
        if v[0] == 1 and v[1] < index:
            index = v[1]
            key = k
    return [key, '_'][index == float('inf')]

print(first("abacabad")) # c
print(first("abacabaabacaba")) # '_'
