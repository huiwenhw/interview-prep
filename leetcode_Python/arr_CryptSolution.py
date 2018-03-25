'''
Given array of strings crypt and an array containing the mapping of letters and digits, solution,
encrypt the words to be word1 + word2 = word3

If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true. If it does not become a valid arithmetic solution, the answer is false.
'''

def isCryptSolution(crypt, solution):
    # convert solution to hash
    d = {}
    for l in solution:
        d[l[0]] = l[1]

    nl = []
    for word in crypt:
        nw = ''
        for n in word:
            nw += d[n]
        if nw[0] == '0' and len(nw) > 1:
            return False
        nl.append(nw)

    if int(nl[0]) + int(nl[1]) == int(nl[2]):
        return True
    return False

crypt = ["SEND", "MORE", "MONEY"]
solution = [['O', '0'],
        ['M', '1'],
        ['Y', '2'],
        ['E', '5'],
        ['N', '6'],
        ['D', '7'],
        ['R', '8'],
        ['S', '9']]
print(isCryptSolution(crypt, solution)) # 9567 + 1085 = 10652, True

crypt = ["TEN", "TWO", "ONE"]
solution = [['O', '1'],
        ['T', '0'],
        ['W', '9'],
        ['E', '5'],
        ['N', '4']]
print(isCryptSolution(crypt, solution)) # 054 + 091 = 145, False cause 054 and 091 both contain leading zeroes
