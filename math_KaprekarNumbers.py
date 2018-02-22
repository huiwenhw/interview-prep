'''
https://www.hackerrank.com/challenges/kaprekar-numbers/problem
'''

def kaprekarNumbers(p, q):
    ans = []
    for i in range(p, q+1):
        sq_str = str(i**2)
        length = int(len(sq_str) / 2)
        n1, n2 = sq_str[:length], sq_str[length:]
        n1 = 0 if n1 == '' else int(n1)
        n2 = 0 if n2 == '' else int(n2)
        if i == n1 + n2:
            ans.append(i)
    return ["INVALID RANGE", ans][ans != []]

print(kaprekarNumbers(1, 100)) # [1, 9, 45, 55, 99]
