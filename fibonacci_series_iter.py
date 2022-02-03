def fibonacci_iter(num):
    if num == 1:
        print("Fibonacci series: 0")
        return
    elif num >= 2:
        prev, next = 0, 1
        print("Fibonacci series:", "0", "1", end=" ")
        for i in range(2, num):
            next += prev
            print(next, end=" ")
            prev = next - prev
        print(end="\n")
    else:
        print("Invalid Input, make sure input is a natural number(positive number)")

if __name__ == "__main__":
    try:
        num = int(input("Enter number : "))
        fibonacci_iter(num)
    except:
        print("Invalid Input, enter a natural number only!")