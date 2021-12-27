
#  present back words from giving number to -1
n = 100
for i in range(n):
    print(n - i)


#  Flatten a List
# Use Itertools. 
regular_list = [[1.2,4.2,1,3,4,],[3,2,1,23]]
flat_list = sum(regular_list,[])
print(sorted(flat_list))