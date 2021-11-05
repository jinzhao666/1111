for b in range(1,10):
    for s in range(0,10):
        for g in range(0,10):
            if 100*b+10*s+g == b**3+s**3+g**3:
                print(100*b+10*s+g)
