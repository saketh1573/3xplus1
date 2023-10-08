def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

if __name__ == "__main__":
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Please enter a positive integer.")
        else:
            steps = collatz_steps(num)
            print(f"Number of steps to reach 1: {steps}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
