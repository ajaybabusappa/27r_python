# def max_min_sum(list_passed):
#     if len(list_passed) == 0:
#         return

#     max = min = list_passed[0]
#     sum = 0
#     for i in list_passed:
#         max = i if i > max else max
#         min = i if i < min else min
#         sum += i
#     return max, min, sum


# list1 = []#[1, 2, 0.7, -32, 11, 0, -3]

# tup1 = max_min_sum(list1)

# if tup1:
#     print("Max", tup1[0])
#     print("Min", tup1[1])
#     print("Sum", tup1[2])
# else:
#     print("Not possible in empty list")




# #Question2 - Find if an element exists in the list - If yes print found
# #2.0 -now I want Index
# #This is called Linear search - O(n), O(1)


# def search_a_num(list1, search_num):
#     for i in list1:
#         if i == search_num:
#             return True
#     return False

# list12 = [1, 2, 0.7, -32, 11, 0, -3]
# search_num2 = int(input("Enter integer to search"))

# if search_a_num(list12, search_num2):
#     print("Found")
# else:
#     print("Not found")



#Iterative method
# flag = False
# for i in list1:
#     if i == search_num:
#         print("Number found")
#         flag = True
#         break

# if not flag:
#     print("Not found")



#2 ways to take list input
#Size of list - 5
#5 times run the loop and take input
#list1.append(input)


# list2 = []

# size_of_list = int(input("Enter the size of list"))

# for i in range(size_of_list):
#     num1 = float(input("Enter the number"))
#     list2.append(num1)

# print(list2)



str1 = input("Enter the numbers in csv formay").split(',')
print(str1)

list1 = list(map(float, str1))
print(list1)

list1 = list(map(float, input("Enter the numbers in csv formay").split(',')))