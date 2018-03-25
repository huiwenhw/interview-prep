'''
https://leetcode.com/problems/basic-calculator-ii/description/

Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5

Note: Do not use the eval built-in library function.
'''
import re

# separate all digits, operators into iterable (0, -, 2147483647)
# iterate through, if its +/-, we add that to the total, update the sign
# if its */, we calc the term and kiv that
# if its digit, we update the term
# at the end, we need to add term*sign, cause the last one will be left out
def calc_short(s):
    tokens = iter(re.findall('\d+|\S', s))
    total, term, sign, num2 = 0, 0, 1, 0
    for token in tokens:
        if token in '+-':
            total += sign * term
            sign = ' +'.find(token) # 1 if +, -1 if -
        elif token in '*/':
            num2 = int(next(tokens))
            term = term * num2 if token == '*' else int(term/num2)
        else:
            term = int(token)
    return total + term * sign

# if its digit, get all digits
# if its +-*/, we append that to sign and continue
# else we pop from sign, if its +-, we add that to total, update prev with +/-
# if its */, we calc and update prev and kiv
# at the end, we need to add prev
def calc(s):
    s = s.replace(' ', '')
    i = prev = total = 0
    sign = ['+']
    while i < len(s):
        ch = s[i]
        print('ch ', ch, ' prev ', prev, ' total ', total)
        if ch in '+-*/':
            sign.append(ch)
            i += 1
            continue
        if ch.isdigit():
            while i+1 < len(s) and s[i+1].isdigit():
                i += 1
                ch += s[i]
        exp = sign.pop()
        if exp in '+-':
            total += prev
            prev = int(ch) * [-1, 1][exp == '+']
        else:
            curr = prev * int(ch) if exp == '*' else prev / int(ch)
            prev = int(curr)
        i += 1
    print('ch ', ch, ' prev ', prev, ' total ', total)
    total += prev
    return total

# works only for single digit
def calculate(s):
    stack = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == '*' or ch == '/':
            num1 = stack.pop()
            num2 = s[i+1]
            i += 1
            if ch == '*':
                evl = int(num1) * int(num2)
            else:
                evl = int(num1) / int(num2)
            stack.append(int(evl))
        else:
            stack.append(ch)
        i += 1
        print(stack)

    while len(stack) > 1:
        num1 = stack.pop()
        exp = stack.pop()
        num2 = stack.pop()
        if exp == '+':
            evl = int(num1) + int(num2)
        else:
            evl = int(num1) - int(num2)
        stack.append(int(evl))
        print(stack)
    return stack[0] 

print('hi ', calc_short('14-3/2'))
print(calc_short("0-2147483647")) # -2147483647
print(calc_short('0*0')) # 0
print(calc_short('  42 ')) # 42
print(calc_short('3+2')) # 5
print(calc_short('3+2*2')) # 7
print(calc_short('3/2')) # 1 
print(calc_short('3+5/2')) # 5
print(calc_short('3+2*2/2+10')) # 14

'''
print('hi ', calc('14-3/2'))
print(calc("0-2147483647")) # -2147483647
print(calc('0*0')) # 0
print(calc('  42 ')) # 42
print(calc('3+2')) # 5
print(calc('3+2*2')) # 7
print(calc('3/2')) # 1 
print(calc('3+5/2')) # 5
print(calc('3+2*2/2+10')) # 14

print(calculate('3+2')) # 5
print(calculate('3+2*2')) # 7
print(calculate('3/2')) # 1 
print(calculate('3+5/2')) # 5
'''
