'''
https://leetcode.com/problems/implement-strstr/description
'''

def strStr(haystack, needle):
    if needle == '': return 0
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            if haystack[i:i+len(needle)] == needle:
                return i
    return -1

print(strStr('hello', 'll')) # 2
print(strStr('asdf', '')) # 0
