'''
'''

import sys 

def get_column_num(string):
    base_ascii = ord('A')-1 # 65-1
    alphabets = 26 # 26-1
    col = 0
    rstr = string[::-1]
    for i in range(len(rstr)):
        curr_ascii = ord(rstr[i])
        diff = curr_ascii - base_ascii
        if i == 0:
            col = col + diff
        else:
            col = col + alphabets * diff * i
        #print('i ', i, ' str[i] ', rstr[i], ' currascii ', curr_ascii, ' diff ', diff, ' col ', col)
    return col

def main():
    # args = sys.argv[1:]
    # nums = [int(i) for i in args[0].split(",")]
    # target = int(args[1])
    print(get_column_num('A'))
    print(get_column_num('ZZ'))
    print(get_column_num('AAA'))

if __name__ == '__main__':
    main()
