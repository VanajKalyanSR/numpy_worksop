# create a list as below
output=[[1,2,3],[4,5,6],[7,5,3,2,3,[2,[3]]]]
a=[1,2,3]
b=[4,5,6]
c=[7,5,3,2,3]
d=[2]
e=[3]

# use these lists to create another list which will look like the list output in line 2

# use append method to do this.

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 5, 3, 2, 3]
d = [2]
e = [3]

output = []
output.append(a)
output.append(b)
nested_list = c.copy()
nested_list.append(d.copy())
nested_list[-1].append(e.copy())
output.append(nested_list)

print(output)
