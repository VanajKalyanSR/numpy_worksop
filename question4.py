#write a program to find the sum of digits of a given number'
a=int(input("Enter a number:"))
for i in ramge(len(a)+1):
  remainder=remainder%10
  a=a/10
  sum+=remainder
print(sum)
