'''
https://leetcode.com/problems/group-anagrams/description/
Given an array of strings, group anagrams together.
'''

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    d = {}
    for s in strs:
        sorteds = ''.join(sorted(s))
        d[sorteds] = d.get(sorteds, []) + [s]

    ans = []
    for key, value in d.items():
        ans.append(value)
    print(d.values())
    return ans

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [["ate", "eat","tea"], ["nat","tan"], ["bat"]]
