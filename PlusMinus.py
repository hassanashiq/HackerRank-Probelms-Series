def plusMinus(arr):
    count_plus = 0
    count_minus = 0
    count_zero = 0

    
    for x in arr:
        if x>0:
            count_plus +=1
        if x<0:
            count_minus +=1
        if x==0:
            count_zero +=1
    
    
    plus = count_plus / len(arr)
    minus = count_minus / len(arr)
    zero = count_zero/ len(arr)
    
    
    print(round(plus,6))
    print(round(minus,6))
    print(round(zero,6))
