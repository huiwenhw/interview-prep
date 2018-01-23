'''
Strings (Immutable)
'''

# String methods
print('hello'.upper() == 'HELLO') 
print('HELLo'.lower() == 'hello') 
print('hello'.index('h') == 0)
print('abc'.isalpha() == True)
print('123'.isdigit() == True)
print('   '.isspace() == True)
print('12345'.find('23') == 1) # returns first index of found '2'
print('bye'.endswith('e') == True)
print('abc'.startswith('a') == True)
print(' strip spaces '.strip() == 'strip spaces')
print('ahaealalao'.replace('a', '') == 'hello') # replaces all 'a'
print('thisbecomesempty' * False) # same logic as 'a'*1 = 'a', 'a'*0 = ''

# Convert String -> List
print(list('abcd') == ['a', 'b', 'c', 'd']) # split by character 
print('abcd efgh'.split() == ['abcd', 'efgh']) # splits on whitespace
print('a,b,d,d'.split(',') == ['a', 'b', 'd', 'd'])

# Convert List -> String
print(''.join(['a', 'b', 'c']) == 'abc')
print(''.join(['a', 'b', 'c']) * False == '') # useful for returning empty string if condition not met

'''
Slicing (String / Lists)
Returns new String/List, does not modify original String/List
-5 -4 -3 -2 -1
 H  E  L  L  O
 0  1  2  3  4
s[n:] + s[n:] == s
'''

s = "hello"	
print(s[:2] + s[2:] == s) 	# True
print(s[:] == 'hello') 		# s[start, end]
print(s[0:1] == 'h') 		# s[0, 1)
print(s[1:] == 'ello') 		# s[1,end]
print(s[:2] == 'he') 		# s[start,2)
print(s[-1:] == 'o') 		# s[1st index from the back, end]
print(s[:-3] == 'he')		# s[start, 3rd index from the back)

# Extended slicing, s[start : end : step]
s = '01234'
print(s[::2] == '024') 							# even indices
print(s[1::2] == '13') 							# odd indices
print(['a','b','c'][::-1] == ['c', 'b', 'a']) 	# Reverse

# Modifying original list (Lists only)
l = [1,2,3,4,5,6]
l[:] = l[2:] + l[:2] 
print(l == [3, 4, 5, 6, 1, 2])

'''
Lists / Matrix (Mutable)
'''

l = ['a','b','c']
l[0] = 'p' 	# Access / Assign
print(l) 	# ['p', 'b', 'c']

# List comprehension [ expression *for* var *in* list *if* ]
# Create List
print([0 for _ in range(5)] == [0, 0, 0, 0, 0])
print([0] * 5 == [0, 0, 0, 0, 0])
# Create 2D matrix
rows, cols = 2, 3 
print([[0 for _ in range(cols)] for _ in range(rows)]) # [[0, 0, 0], [0, 0, 0]]
# expression 
fruits = ['apple', 'cherry', 'banana']
afruits = [ s.upper() for s in fruits if 'a' in s ] 
print(afruits == ['APPLE', 'BANANA'])

# Iteration (using indices)
ans, ans2, ans3 = '', '', ''
for i in range(5): print(i, end='') 			# 01234
for i in range(len([1,2,3])): print(i, end='') 	# 012
for i in range(5, -1, -1): print(i, end='') 	# 543210	# range(start, stop, step)

# Iteration (using elements)
s, ans = 'abcd', ''
for char in s: ans += char
print(ans == 'abcd')

# List Methods, Modifies original array && does not return anything 
nums = [1,2]
nums.append(3)				# O(1) 		# [1, 2, 3]
nums.insert(0, 4) 			# O(n)		# [4, 1, 2, 3] 			# insert(index, element)
nums.extend([5,6])			# O(k)		# [4, 1, 2, 3, 5, 6]	# same as [1, 2] + [3, 4] # O(k)
nums.index(4)				# O(n)		# 0
if 3 in nums: nums.index(3) # O(n)		# [4, 1, 2, 3, 5, 6]	# searches for first element
if 3 in nums: nums.remove(3)# O(n)		# [4, 1, 2, 5, 6]
nums.sort()					# O(n logn) # [1, 2, 4, 5, 6]
nums.reverse()				# O(n)		# [6, 5, 4, 2, 1]
print(nums) 							# [6, 5, 4, 2, 1]

# List copy / deepcopy
import copy
oldl = [1,2,3,4]
newl = oldl[:]
newl2 = list(oldl)
newl3 = copy.deepcopy(oldl) # if list contains objects and we want to copy them too
print(newl, newl2, newl3) # [1, 2, 3, 4]
newl = oldl 	# maintains a reference, newl or oldl value changes affecs the other

'''
Using list for Stack / Queue
'''
stack = [1,2,3]
stack.pop() 		# O(1) 		# returns 3  		# [1,2]
stack.append(10) 	# O(1) 		# returns nothing 	# [1,2,10]
len(stack) 			# O(1)		# 3
queue = [1,2,3]
queue.pop(0) 		# O(n)		# returns 1			# [2.3]
queue.append(10)	# O(1)		# returns nothing 	# [2,3,10]	
len(queue) 			# O(1)		# 3
print(stack, queue)

'''
Dictionary
'''

d = {'a': 'alpha'}
d['b'] = 'beta'			# O(1)
print(d.keys()) 		# dict_keys(['a', 'b'])
print(d.values()) 		# dict_values(['alpha', 'beta'])
print(d.items())		# dict_items([('a', 'alpha'), ('b', 'beta')])
if 'b' in d: print('b') # b

nums, dic = [1,2], {1: 3}
for item in nums:
	dic[item] = dic.get(item, 0) + 1	# if item doesnt exist in d, return 0+1
print(dic)								# {1: 4, 2: 1}

# Iteration in dict 
for key in d: print(key)							# b a
for key in d.keys(): print(key) 					# b a
for key, value in d.items(): print(key, value) 		# a alpha b beta 
for index, key in enumerate(d): print(index, key)	# 0 a 1 b
for key in sorted(d.keys()): print(key)				# a b

'''
Set
'''

# Methods below don't return anything except for .pop()
s = set() 									# s {}
s = set({1,2,3})						# O(len of set)
b = {1, 2, 3}
s.add(4)						# O(1)		# s {1, 2, 3, 4}
len(s)		 					# O(1)		# 4
if 3 in s: print('3  in set') 	# O(1) 		# 3 in set
print(s.pop())					# O(1)		# 1
s.remove(2)						# O(1)		# s {3, 4}
s.clear()						# O(1)		# s {}
s.update(b)						# O(k)		# s {1, 2, 3}
a = s.copy()					# O(n)		# {1, 2, 3}
print(s, a)

# Convert set to list 
print(list(set({1,2,3,3,3}))) 			# O(n)		# [1, 2, 3]
print(list(set({'a', 'b', 'c', 'c'}))) 	# O(n)		# ['a', 'b', 'c']
print(list(set({ (1,2), (1,2) }))) 		# O(n)		# [(1, 2)]
print(list(map(list, { (1,2), (1,2) })))			# [(1, 2)]

# Iteration 
s = set({1,2,3,4})
for item in s: print(item, end='') 		# O(len(s)) # 1234











