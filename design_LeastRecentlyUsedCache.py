'''
https://leetcode.com/problems/lru-cache/description/
'''

# get: if key not in dict, return -1 
#      if key is in dict, get index, slice to append at the back
# put: if key is in dict, simply change value
#      if len(cache) same as capacity, remove LRU from cache
#      add new key, value to dict and cache 
class LRUCache(object):
    def __init__(self, capacity):
       self.capacity = capacity
       self.d = {}
       self.lrulist = []

    def get(self, key):         # O(n) cause of slicing
        if key not in self.d:
            return -1
        i = self.lrulist.index(key)
        self.lrulist = self.lrulist[:i] + self.lrulist[i+1:] + [key]
        return self.d.get(key)

    def put(self, key, value):# O(n) cause of slicing
        if key in self.d:
            self.d[key] = value
            i = self.lrulist.index(key)
            self.lrulist = self.lrulist[:i] + self.lrulist[i+1:] + [key]
        else:
            if len(self.lrulist) == self.capacity:
                self.d.pop(self.lrulist[0], None)
                self.lrulist = self.lrulist[1:]
            self.d[key] = value
            self.lrulist.append(key)

# Using doubly linked list to provide O(1) get / put
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

# dict: {key: node}
# get: if key not in dict, return -1 
#      if key in dict, remove node, add node to before tail, return val
# put: if key in dict, remove node
#      if capacity is up, remove head.next, remove from dict
#      then create and add node to tail.prev and to dict
class LRUCacheTwo(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.d = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail 
        self.tail.prev = self.head 

    def get(self, key):
        if key not in self.d:
            return -1
        n = self.d[key]
        self.remove(n)
        self.add(n)
        return n.val

    def put(self, key, value):
        if key in self.d:
            self.remove(self.d[key])
        elif len(self.d) == self.capacity:
            n = self.head.next
            self.remove(n)
            self.d.pop(n.key, None)
        n = Node(key, value)
        self.d[key] = n
        self.add(n)

    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    def add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

def main():
    obj = LRUCacheTwo(2)
    obj.put(1,1)
    obj.put(2,2)
    print(obj.get(1)) # 1
    obj.put(3,3)
    print(obj.get(2)) # -1
    obj.put(4,4)
    print(obj.get(1)) # -1
    print(obj.get(3)) # 3
    print(obj.get(4)) # 4
    # print(obj.d, obj.lrulist)

    obj = LRUCacheTwo(2)
    print(obj.get(2)) # -1 
    obj.put(2, 6)
    print(obj.get(1)) # -1 
    obj.put(1, 5)
    obj.put(1, 2)
    print(obj.get(1)) # 2 
    print(obj.get(2)) # 6
    # print(obj.d, obj.lrulist)

    obj = LRUCacheTwo(2)
    obj.put(2,1)
    obj.put(1,1)
    obj.put(2,3)
    obj.put(4,1)
    print(obj.get(1)) # -1 
    print(obj.get(2)) # 3
    # print(obj.d, obj.lrulist)

if __name__ == "__main__":
    main()
