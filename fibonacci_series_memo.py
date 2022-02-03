def fibo_memo(n):
    if n <= 1:
        return n
    else:
        if t[n] != -1:
            return t[n]
        else:        
            t[n] = fibo_memo(n-1) + fibo_memo(n-2)
            return t[n]

if __name__ == "__main__":
    try:
        num = int(input("Enter number : "))
        if num > 0:
            t = [-1 for i in range(num+1)] #memoization to calculate once and use anytime 
            print("Fibonacci series :", end=" ")
            for i in range(num):
                print(fibo_memo(i), end=" ")
            print(end="\n")
        else:
            print("Please enter a natural number(positive number) only!")
    except:
        print("Invalid input, enter natural number(positive)")
    