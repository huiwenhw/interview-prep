'''
https://leetcode.com/problems/most-frequent-subtree-sum/description/
The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself)
If there is a tie, return all the values with the highest frequency in any order.
'''

class TN:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findFrequentTreeSum(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    ans = {}

    if root is None: return []

    def recurse(node):
        if node is None: return 0

        left = recurse(node.left)
        right = recurse(node.right)

        now = left + right + node.val
        ans[now] = ans.get(now, 0) + 1
        return now 

    recurse(root)

    sorted(ans.items(), key= lambda x: x[1])
    max_value = max(ans.items(), key=lambda x:x[1])[1]

    res = []
    for k,v in ans.items():
        if v == max_value:
            res.append(k)
    return res

root = TN(0)
print(findFrequentTreeSum(root)) # [0]

root = TN(5)
root.left = TN(2)
root.right = TN(-3)
print(findFrequentTreeSum(root)) # [2, 4, -3]

root = TN(5)
root.left = TN(2)
root.right = TN(-5)
print(findFrequentTreeSum(root)) # [2]
