def test():
    s = "yxyxyxyxyxioio"
    d = {}
    newstr = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for ch in s:
        if ch not in vowels and ch not in newstr:
            newstr += ch
        print('ch ', ch, ' newstr ', newstr)
        d[ch] = True
    print(newstr)

print(test())
