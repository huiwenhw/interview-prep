'''
Given a string s, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.
Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you would be asked to do during a real interview.
'''

# O(n) time and space
def first(s):
    d = {}
    for i in range(len(s)):
        d[s[i]] = d.get(s[i], [0, i])
        d[s[i]][0] += 1
    min_i = float('inf')
    for k,v in d.items():
        if v[0] == 1 and v[1] < min_i:
            min_i = v[1]
    return [min_i, -1][min_i == float('inf')]

def first_short(s):
    letters = 'abcdefghijklmnopqrstuvwyz'
    min_i = float('inf')
    for i in range(len(s)):
        if s.count(s[i]) == 1 and i < min_i:
            min_i = i
    return [min_i, -1][min_i == float('inf')]
print(first("abacabad")) # c
print(first("abacabaabacaba")) # '_'
