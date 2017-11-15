'''
https://leetcode.com/problems/basic-calculator/description/

Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.
Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
'''

# works 
# if its digit, get all digits (e.g. could be 20) 
# keep a signs array, use the previous sign and * either 1 or -1 (if its minus)
# this ensures that 1-(2-3) = 1+1
def calc_short(s):
    total = 0
    i, signs = 0, [1, 1]
    while i < len(s):
        print('%11s   %-16s %2d' % (s[i:], signs, total))
        ch = s[i]
        if ch.isdigit():
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            total += int(s[start:i]) * signs.pop()
            continue
        if ch in "(+-":
            signs.append(signs[-1] * [1, -1][ch == '-'])
        elif ch == ")":
            signs.pop()
        print('%11s   %-16s %2d' % (s[i:], signs, total))
        i += 1
    return total



# push to stack expressions
# if +, push 1 
# if -, push -1
# if (, push 1
# if ), pop
# will not work for '1-(5)' or '2-(5-6)' 
def calc(s):
    s = s.replace(' ', '')
    stack, sumn, snum = [1], 0, ''
    for i in range(len(s)):
        print('i ', i, ' s[i] ', s[i], ' s ', stack, ' sum ', sumn)
        if s[i].isdigit() and s[i+1:i+2].isdigit():
            snum += s[i]
        elif s[i].isdigit():
            snum += s[i]
            sumn += int(snum) * stack.pop()
            snum = ''
        elif s[i] == "+":
            stack.append(1)
        elif s[i] == "-":
            stack.append(-1)
        elif s[i] == "(":
            stack.append(1)
        elif s[i] == ")":
            stack.pop()
    return sumn
# 1 + 1
# push things to stack, if see +/-: pop from stack, n1 (exp) i+1
# 2-1+2
# [2], see -, 2-1, push that back to stack
# [1], see +, 1+2, push that back to stack
# end of str, pop val from stack

# if open bracket, want to wait for close bracket
# [(,1,+,(,4,+,5,+,2] 
# see close bracket, pop n1 pop (exp) pop n2, push to stack
# [(,1,+,(,4,+,7]
# pop n1 pop + pop 7, push to stack
# [(,1,+,(11]
# pop n1 pop exp (check if open bracket). if yes, pop back n1 

# use another stack for brackets?

# case1: open bracket: just append
# case2: digit: just append
# case3: if prev is + or -, check if s[i+1] is digit 
#       digit, evaluate, push back result. 
#       not digit, ignore 
# case4: close bracket. while stack[-1] != "(" 

def calculate(s):
    s = s.strip()
    stack, bstack = [], []
    if s[0] == "(":
        bstack.append(s[0])
    stack.append(s[0])

    for i in range(1,len(s)):
        print('i ', i, ' s[i] ', s[i])
        print('bstack ', bstack, ' stack ', stack)
        if s[i] == "(":
            bstack.append(s[i])
            stack.append(s[i])
        elif s[i-1] == "+" or s[i-1] == "-":
            exp = stack.pop()
            n1 = int(stack.pop())
            n2 = int(s[i])
            if exp == "+":
                stack.append(n1 + n2)
            else:
                stack.append(n1-n2)
        elif s[i] == ")":
            while stack[-1] != "(":
                print('else ', stack)
                n1 = int(stack.pop())
                exp = stack.pop()
                if exp == "(":
                    stack.append(n1)
                    break
                elif exp == "+":
                    n2 = int(stack.pop())
                    stack.append(n1+n2)
                else:
                    n2 = int(stack.pop())
                    stack.append(n1-n2)
            bstack.pop()
        elif len(bstack) > 0:
            print('hi')
            stack.append(s[i])
        else:
            stack.append(s[i])
        print('end bstack ', bstack, ' stack ', stack)

    if len(stack) == 1:
        return stack[-1]
    elif len(stack) == 2:
        return stack[0] + stack[1]
    else:
        n1 = int(stack.pop())
        exp = stack.pop()
        n2 = int(stack.pop())
        if exp == "+":
            stack.append(n1 + n2)
        else:
            stack.append(n1-n2)
    return stack[-1]


s = "1+1"
print(calc_short(s))
s = "(1-2)+(3-4)"
print(calc_short(s))
s = "3-(2+(9-4))"
print(calc_short(s))
s = '2-(5-6)'
print(calc_short(s)) # 3
'''
s = '1-(5)'
s = '2-(5-6)'
print(calc_short(s)) # 3
s = ' 30 + ( 25 + 1 ) '
print(calc(s)) # 56
s = "1+1"
print(calc(s)) # 2
s = "2-1+2"
print(calc(s)) # 3
s = "(1+(4+5+2)-3)+(6+8)"
print(calc(s)) # 23 
s = "  30"
print(calc(s)) # 30
'''
