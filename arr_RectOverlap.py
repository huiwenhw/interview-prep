'''
'''

import sys 

def overlap(l1, r1, l2, r2):
    if (l1[0] > l2[0] and l1[0] > r2[0]) or (r1[0] < l2[0] and r1[0] < r2[0]):
        return False
    if (l1[1] < l2[1] and l1[1] < r2[1]) or (r1[1] > l2[1] and r1[1] > r2[1]):
        return False
    return True

def main():
    # args = sys.argv[1:]
    # nums = [int(i) for i in args[0].split(",")]
    # target = int(args[1])
    print(overlap([0,5], [5,0], [6, 3], [8,0]))
    print(overlap([0,5], [5,0], [3, 3], [8,0]))

if __name__ == '__main__':
    main()
