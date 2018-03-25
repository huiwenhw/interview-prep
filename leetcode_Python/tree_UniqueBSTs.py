'''
https://leetcode.com/problems/unique-binary-search-trees-ii/description/
'''

from LevelOrder import level_order

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def generateTrees(n):
    def generate(first, last):
        trees = []
        for root in range(first, last+1):
            for left in generate(first, root-1):
                for right in generate(root+1, last):
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    trees.append(node)
        return trees or [None]
    return generate(1, n)

res = generateTrees(3)
for root in res:
    print(level_order(root))
