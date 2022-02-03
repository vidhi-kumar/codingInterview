def fibo_recur(n):
    if n <= 1:
       return n
    else:
       return(fibo_recur(n-1) + fibo_recur(n-2))

if __name__ == "__main__":
    try:
        num = int(input("Enter number : "))
        if num > 0:
            print("Fibonacci series :", end=" ")
            for i in range(num):
                print(fibo_recur(i), end=" ")
            print(end="\n")
        else:
            print("Please enter a natural number(positive number) only!")
    except:
        print("Invalid input, enter natural number(positive)")
    