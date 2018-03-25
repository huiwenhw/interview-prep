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

s = "1+1"
print(calc_short(s))
s = "(1-2)+(3-4)"
print(calc_short(s))
s = "3-(2+(9-4))"
print(calc_short(s))
s = '2-(5-6)'
print(calc_short(s))
s = '1-(5)' # -4
s = ' 30 + ( 25 + 1 ) '
s = "2-1+2" # 3
s = "(1+(4+5+2)-3)+(6+8)" # 23
s = "  30" # 20
