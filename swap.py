def swap(num1, num2):
    num1 ^= num2
    num2 ^= num1
    num1 ^= num2
    print("First and second number are now", num1, num2, "respectively")

if __name__ == "__main__":
    try:
        inp = [int(x) for x in input("Enter 2 numbers: ").split()]
        num1, num2 = inp[0], inp[1]
        if len(inp) != 2:
            print("Invalid Input, enter 2 numbers")
        else:
            swap(num1, num2)
    except:
        print("Enter 2 numbers only!")