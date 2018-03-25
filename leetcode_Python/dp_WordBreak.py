'''
https://leetcode.com/problems/word-break/description/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode", dict = ["leet", "code"].
Return true because "leetcode" can be segmented as "leet code".
'''

# any returns as early as it sees the first True value
def wordbreak(s, wordDict):
    ok = [True]
    for i in range(1, len(s)+1):
        # ok += [any(ok[j] and s[j:i] in wordDict for j in range(i))] # both works
        ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
        print(ok)
    return ok[-1]

def wordbreak_readable(s, wordDict):
    dp = [False for _ in range(len(s)+1)]
    dp[0] = True

    # dp[i] == True means: I can start my next word from there 
    for i in range(len(s)):
        if dp[i]:
            for k in range(i, len(s)):
                if s[i:k+1] in wordDict:
                    dp[k+1] = True
    return dp[-1]

print(wordbreak("leetcode", ["leet", "code"])) # True
print(wordbreak("water", ["wa", "ater"])) # False
print(wordbreak_readable("leetcode", ["leet", "code"])) # True
print(wordbreak_readable("water", ["wa", "ater"])) # False
