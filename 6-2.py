for s in open('6-1.in').readlines():
    idx = 13
    while True:
        if len(set(s[idx-13:idx+1])) == 14:
            print(idx+1)
            exit() 
        idx = idx + 1
