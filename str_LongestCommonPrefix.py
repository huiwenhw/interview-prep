'''
https://leetcode.com/problems/longest-common-prefix/description/
'''

# finds min len of all strings
# for min length, for each string, find if all current ith elem is the same
# same, return min string. nope, return [0:i]
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if strs == []: return ''
    min_str = min(strs)
    minn = len(min_str) 

    for i in range(minn):
        curr = strs[0][i]
        for k in range(1, len(strs)):
            if curr != strs[k][i]:
                return strs[0][:i]
    return min_str

print(longestCommonPrefix(['a'])) # a
print(longestCommonPrefix(['abc', 'ab', ''])) # ''
print(longestCommonPrefix(['abc', 'ab'])) # ab

# zip(*strs) takes ith element from each string and assembles it into a list
# it continues doing this until it reaches the shortest input
# unzip ['abc', 'ab']: ['a', 'a'], ['b', 'b']
def longestCommonPrefix(strs):
    if strs == []: return ''

    i = 0
    for i, first_letters in enumerate(zip(*strs)):
        if len(set(first_letters)) > 1: 
            return strs[0][:i]
    return min(strs)

print(longestCommonPrefix(['a'])) # a
print(longestCommonPrefix(['abc', 'ab', ''])) # ''
print(longestCommonPrefix(['abc', 'ab'])) # ab

