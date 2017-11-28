'''
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.
'''

# O(n) time and space, assuming N is max length of binary representation
def solution(N):
    bin = "{0:b}".format(N)
    count, maxn = 0, 0
    for b in bin:
        if b == '0':
            count += 1
        else:
            maxn = max(maxn, count)
            count = 0
    return maxn

print(solution(9)) # 2
print(solution(1041)) # 5
