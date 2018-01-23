'''
https://leetcode.com/problems/reorganize-string/description/
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
'''

# Sort the string according to freq of characters
# find middle
# place start to middle at odd indices and middle to end at even indices
# letters cannot be rearranged if last 2 characters are the same
def string(S):
    a = sorted(sorted(S), key=S.count)
    h = int(len(a)/2)
    a[1::2], a[::2] = a[:h], a[h:]
    return ''.join(a) * (a[-1:] != a[-2:-1]) 

print(string("vvvlo")) # vlvov
print(string("lovvv")) # vlvov
print(string("a")) # a
print(string("aa"))
print(string("aab")) # aba
print(string("aaab"))
print(string("baaba")) # ababa
print(string("abaaaba"))
print(string("bbbbbbb"))

'''
def string(S):
    start, end, nextn = 1, len(S), 0
    quit = False
    while start < end:
        if S[start] == S[start-1]:
            if nextn >= end: 
                return ""
            while S[nextn] == S[start] or nextn+1 < end and S[nextn-1] == S[nextn+1]:
                nextn += 1
                if nextn >= end: 
                    return ""
            print('start ', start, ' nextn ', nextn, ' end ', end, ' S ', S)
            if nextn < start:
                S = S[:nextn] + S[nextn+1:start] + S[nextn] + S[start:]
            else:
                S = S[:start] + S[nextn] + S[start:nextn] + S[nextn+1:]
                nextn += 1
            start += 1
            print('after start ', start, ' nextn ', nextn, ' end ', end, ' S ', S)
        else:
            start += 1
    return S 
'''
