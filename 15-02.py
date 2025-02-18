# str1 = input("Enter the string")  #Someshh


# res = {}
# for k in str1:
#     if k in res:
#         res[k] += 1
#     else:
#         res[k] = 1

# print(res)



def max_min_sum(list_passed):
    if len(list_passed) == 0:
        return

    max = min = list_passed[0]
    sum = 0
    for i in list_passed:
        max = i if i > max else max
        min = i if i < min else min
        sum += i
    return max, min, sum


#Level2 - 
list1 = ["Deeksha", "Ammu", "Random"]
final_res = []

for str in list1:
    res = {}
    for k in str:
        if k in res:
            res[k] += 1
        else:
            res[k] = 1

    final_res.append({str: res})

print(final_res)

#Second largest element

#Disadvantages - Does not work for duplicate values. Time complexity.
list1 = [2, 4, 5, -1, -32, 79]
list1.sort()
print(list1)
print(list1[-2])



#Other way
max, min, sum = max_min_sum(list1)

second_largest = float('-inf')
for i in list1:
    if i != max and i > second_largest:
        second_largest = i

print(second_largest)



print(int(float('-inf')))

#Second largest code - 2 ways
#Linear search
#You have to find duplicate elements and unique elements

