for s in open('6-1.in').readlines():
    idx = 3
    while True:
        if len(set(s[idx-3:idx+1])) == 4:
            print(idx+1)
            exit() 
        idx = idx + 1
