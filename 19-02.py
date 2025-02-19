#21, 18, 16
#Multidimensional arrays
#Given array of N integer, the task is to replace each element of the array  by its rank in the array
# Input: 20 15 26 2 98 6       Output:4 3   5   1  6 2
#3 4 2 6 1 5


list1 = [20, 15, 26, 2, 98, 6]
list2 = sorted(list1)
print(id(list1))
print(id(list2))
print(list1)
print(list2)


res = []
for i in list1:
    temp = (len(list1) - (list2.index(i))) 
    res.append(temp)

print(res)




#Using inbuilt functions => index 
#Linear search
#Binary search


#8 7 1 6 5 9 
#1 5 6 9 8 7
#Sort the list - 1 5 6 7 8 9
#Reversing second half - 1 5 6 9 8 7

list1 = [8, 7, 1, 6, 5, 9, 2]
list1.sort() # 1 2 5 6 7 8 9 
#8, 7, 1, 6, 5, 9, 2 => 1 2 5 6 7 8 9 => 1 2 5 6 9 8 7


low = (len(list1) - 1)//2 + 1 #0
high = len(list1) - 1
while low < high:
    list1[low], list1[high] = list1[high], list1[low]
    low += 1
    high -= 1


print(list1) # 9 8 7 6 5 1


#
list1 = [[3, 4, 5], [6, 7, 8], [-10, -11, -12]]

sum = 0
for i in list1:
    for j in i:
        sum += j

sum = 0
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if i == 0 or i == len(list1) - 1:
            sum += list1[i][j]
        else:
            if j == 0 or j == len(list1[i]) -1:
                sum += list1[i][j]
print(sum)

sum = 0
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if (i == 0 or i == len(list1) - 1) or (j == 0 or j == len(list1[i]) -1):
            sum += list1[i][j]

print(sum)