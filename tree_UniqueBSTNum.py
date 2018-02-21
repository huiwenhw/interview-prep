'''
https://leetcode.com/problems/unique-binary-search-trees/description/
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
Good explanation: https://discuss.leetcode.com/topic/8398/dp-solution-in-6-lines-with-explanation-f-i-n-g-i-1-g-n-i/2
'''

# idea: for values 1 ... n
# use every index as the root node and 
# count how many ways there are to generate unique BSTs on the right and left subtrees
# e.g. n = 3
# root index = 1, ans[3] += num ways to generate [] and [2,3]
# root index = 2, ans[3] += num ways to generate [1] and [3] 
# root index = 3, ans[3] += num ways to generate [1,2] and []
# trick here is, no matter what the index for the left and right subtree are 
# for e.g. [1,2] or [2,3], we only look at the number of indexes i.e. 2 
def numTrees(n):
   ans = [0] * (n+1)
   ans[0] = 1

   for i in range(1, n+1):
       for j in range(i):
           ans[i] += ans[j] * ans[i-j-1]
   return ans[n] 

print(numTrees(3)) # 5
print(numTrees(4)) # 14
