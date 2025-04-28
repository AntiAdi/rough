def fibonacci_by_memoization(n, memo) :
    if n<=1 : 
        return n
    
    if n in memo :
        return memo[n]
    else : 
        memo[n] = int(fibonacci_by_memoization(n-1, memo) + fibonacci_by_memoization(n-2, memo))
        return memo[n]


fibo_dict = dict()
fibonacci_by_memoization(6, fibo_dict)
print(fibo_dict)