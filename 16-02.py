# #[[1, -5, 92], [-22, -37, -9], [23, -9, 22.5]]
# #[92, -9, 23]


# def find_max(my_list):
#     max = float('-inf')
#     for i in my_list:
#         max = i if i > max else max
#     return max


# list1 = [[1, -5, 92], [-22, -37, -9], [23, -9, 22.5]]
# res = []

# for j in list1:
#     res.append(find_max(j))

# print(res)



#Binary search - It can be perfromed only on a sorted list
#I want 75
#I want 30
search_element = int(input("Enter number to search"))
# list1 = [1 , 2, 10, 32, 75, 89, 100]
# low = 0
# high = len(list1) - 1


# flag = False
# while low <= high:
#     mid = int((low + high)/ 2)
#     if list1[mid] == search_element:
#         flag = True
#         print(mid)
#         break
#     elif list1[mid] > search_element:
#         high = mid - 1
#     else:
#         low = mid + 1


# if flag == False:
#     print("Not found")

#O(Log(n)), 
def binary_search(list1, search_element):
    low = 0
    high = len(list1) - 1
    while low <= high:
        mid = int((low + high)/ 2)
        if list1[mid] == search_element:
            return mid
        elif list1[mid] > search_element:
            high = mid - 1
        else:
            low = mid + 1
    return -1

list2 = [1 , 2, 10, 32, 75, 89, 100]

res = binary_search(list2, search_element)

if res != -1:
    print(res)
else:
    print("Not found")




#Bubble sort
list1 = [45, 32, -5, 92, 99, 101, 45, 11]
#[32, 45, -5, , 92, 99, 101, 45, 11]
#[32, -5, 45, 92, 99, 101, 45, 11]
#[32, -5, 45, 92, 99, 45, 101, 11]
#[32, -5, 45, 92, 99, 45, 11, 101]
print(list1)

#O(n square) - time and O(1) space
for j in range(len(list1)-1):
    for i in range(0, len(list1)-1):
        if list1[i] > list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]
    print(list1)

#T.C - O(nlogn), S.C - O(1)
count = 0
for j in range(len(list1)-1):
    for i in range(0, len(list1)- j -1):
        count += 1
        if list1[i] > list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]
    print(list1)

print(count)