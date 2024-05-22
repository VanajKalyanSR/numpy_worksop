#write a program to find the factorial of a nummber
a=int(input("Enter number:"))
def fact(n):
  res=1
  if a==0 or a==1:
    return 1
  else:
    res=a*fact(n-1)
    return res
fact(n)
