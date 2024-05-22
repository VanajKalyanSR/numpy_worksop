# find if the given number is a palindrome or not?
a=int(input("Enter a number:"))
b=a[::-1]
if (a==b):
  print("pallindrome")
else:
  print("Not a pallindorme")
