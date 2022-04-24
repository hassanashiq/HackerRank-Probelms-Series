def miniMaxSum(arr):
    # Write your code here
    all_sums=[]
    for i in range(len(arr)):
        numbers = arr.copy()
        numbers.pop(i)
        sum_of_four = sum(numbers)
        all_sums.append(sum_of_four)
    print(min(all_sums), max(all_sums))
