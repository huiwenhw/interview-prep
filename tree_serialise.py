import collections 

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 1 2 # # 3 4 # # 5 # # 
def serialise(root):
    def ser(node):
        if node:
            vals.append(str(node.val))
            ser(node.left)
            ser(node.right)
        else:
            vals.append('#')
    vals = []
    ser(root)
    return ' '.join(vals)

# Changed to not use pop(0) as it is O(n)
# deque makes popleft O(1)
def deserialise(data):
    if not data: return
    def deser(vals):
        if len(vals) == 0: return
        # val = vals.pop(0) # so that we will go through the array in order
        val = vals.popleft()
        print(val, vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = deser(vals)
        node.right = deser(vals)
        return node
             
    # vals = data.split()
    vals = collections.deque(data.split())
    return deser(vals)

def deserialise_withiter(data):
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
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

data = serialise(root)
print('data ', data)
ans = deserialise(data)
print(level_order(ans))

'''
root = deserialise("5,4,7,3,None,2,None,-1,None,9")
print(level_order(root))
print(serialise(root))
'''
