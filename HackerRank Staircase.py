def staircase(n):
    symbol = '#'
    space = ' '
    
    for i in range(1, n+1):
        if i<n:
            print(space*(n-i-1), symbol*i)
        else:
            print(symbol*i)
