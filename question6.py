#write a program to find the maximum of two numbers
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

num1 = 10
num2 = 20

maximum = find_max(num1, num2)
print(f"The maximum of {num1} and {num2} is {maximum}.")
