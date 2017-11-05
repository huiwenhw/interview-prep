# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialise(root):
    def doit(node):
        if node:
            vals.append(str(node.val))
            doit(node.left)
            doit(node.right)
        else:
            vals.append('#')
    vals = []
    doit(root)
    print(' '.join(vals))
    return ' '.join(vals)

def deserialise(data):
    def doit():
        val = next(vals)
        print('val ', val, ' vals ', vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = doit()
        node.right = doit()
        print('node ', node.val)
        return node
    vals = iter(data.split())
    print(data.split())
    return doit()

'''
def serialise(root):
    ans, queue = "", [root]
    while queue:
        node = queue.pop(0)
        if node:
            ans += str(node.val) + ","
            queue.append(node.left)
            queue.append(node.right)
    return ans[:-1]

def deserialise(data):
    if data == '': return TreeNode(data)
    qdata = data.split(",")
    queue = []
    for num in qdata:
        if num == 'None':
            queue.append(None)
        else:
            queue.append(int(num))
    print(queue)

    pointer, length = 0, len(queue)
    node = TreeNode(queue[0])
    queue[0] = node
    for i in range(length):
        node = queue[i]
        if pointer == 0: root = node
        print('node.val ', node.val)
        if node.val is None:
            print('pointer - i ', i, ' pointer ', pointer)
            pointer -= 1
        else:
            print('pointer + i ', i, ' pointer ', pointer)
            pointer += 1
        
            print('i ', i, ' pointer ', pointer)
            if i+pointer < length:
                left = queue[i+pointer]
                node.left = TreeNode(left)
                queue[i+pointer] = node.left
            if i+pointer+1 < length:
                right = queue[i+pointer+1]
                node.right = TreeNode(right)
                queue[i+pointer+1] = node.right
            print('current ', queue[i].val, ' left ', left, ' right ', right)
    return root
 '''
 
def level_order(root):
    index = 0
    ans, queue = [], [(root, index)]
    while queue:
        node, level = queue.pop(0)
        if node:
            if len(ans) == level:
                ans.append([])
            ans[level] = ans[level] + [node.val]
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
    return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

ans = deserialise(serialise(root))
print(level_order(ans))

'''
root = deserialise("5,4,7,3,None,2,None,-1,None,9")
print(level_order(root))
print(serialise(root))
'''
