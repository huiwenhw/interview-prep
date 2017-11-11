'''
https://leetcode.com/problems/lru-cache/description/
'''

class LRUCache(object):
    def __init__(self, capacity):
       self.capacity = capacity
       self.d = {}
       self.index = 0
       self.lrulist = []

    def get(self, key):
        if key not in self.d:
            return -1
        i = self.lrulist.index(key)
        self.lrulist = self.lrulist[:i] + self.lrulist[i+1:] + [key]
        return self.d.get(key)

    def put(self, key, value):
        if key in self.d:
            self.d[key] = value
            i = self.lrulist.index(key)
            self.lrulist = self.lrulist[:i] + self.lrulist[i+1:] + [key]
        elif self.index == self.capacity:
            self.d.pop(self.lrulist[0], None)
            self.lrulist = self.lrulist[1:]
            self.d[key] = value
            self.lrulist.append(key)
        else:
            self.d[key] = value
            self.lrulist.append(key)
            self.index += 1

# Using doubly linked list to provide O(1) get / put
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.d = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.head = self.tail 
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
        n = Node(key, value)
        self.d[key] = n
        self.add(n)
        if len(self.d) > self.capacity:
            n = self.head.next
            self.remove(n)
            self.d.pop(n.key, None)

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
    obj = LRUCache(2)
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

    obj = LRUCache(2)
    print(obj.get(2)) # -1 
    obj.put(2, 6)
    print(obj.get(1)) # -1 
    obj.put(1, 5)
    obj.put(1, 2)
    print(obj.get(1)) # 2 
    print(obj.get(2)) # 6
    # print(obj.d, obj.lrulist)

    obj = LRUCache(2)
    obj.put(2,1)
    obj.put(1,1)
    obj.put(2,3)
    obj.put(4,1)
    print(obj.get(1)) # -1 
    print(obj.get(2)) # 3
    # print(obj.d, obj.lrulist)

if __name__ == "__main__":
    main()
