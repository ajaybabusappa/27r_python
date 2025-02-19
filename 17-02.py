# # #Wap to print duplicates and unique numbers in an array/List.
# # #Wap to check if each number in an  list contains duplicate digits, returning true for duplicates and false for unique digits.
# # #        Input: [202,89,112,88]           Output:[true ,false ,true ,true]
# # #8) Wap to check if the digits of each number in an list are in increasing order, returning true or false for each Increasing order or not
# # # Input: [568,89,112,88,571]     Output: [true,true ,false,false ,false]
# # #11) Find the missing numbers. Input: 34571      Outpur : 26 missing
# # #15) Reverse an Array.


# # #Reverse an array
# # #O(n) - Time complexity, O(n)
# # list1 = [1, 4, "String", "Str2", 5.5, 90]
# # #[90, 5.5, str2, .....]
# # rev = []
# # for i in list1:
# #     #rev.append(i)
# #     rev.insert(0, i)

# # list1 = rev
# # print(rev)
# # print(list1)


# # list1 = list1[::-1]

# # #Most efficient approach - O(n) T.c anf O(1) S.C

# # low = 0
# # high = len(list1) - 1
# # while low < high:
# #     list1[low], list1[high] = list1[high], list1[low]
# #     low += 1
# #     high -= 1

# # print(list1)



# #Wap to print duplicates and unique numbers in an array/List.

# duplicates = set()
# unique = set()
# list1 = [1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 7, 9, 11, 11]
# for i in list1:
#     if i in unique:
#         duplicates.add(i)
#         unique.remove(i)
#     elif i not in duplicates:
#         unique.add(i)

# print(list(duplicates))
# print(unique)




def duplicate_digit_exists(num1):
    curr_list = []
    while num1 > 0:
        rem = num1 % 10
        if rem in curr_list:
            return True
        curr_list.append(rem)
        num1 = num1 // 10
    return False

list2 = [202,89,112,88]
res = []
for i in list2:
    #res.append(duplicate_digit_exists(i))
    temp = duplicate_digit_exists(i)
    res.append(temp)

print(res)


#Find the missing numbers. Input: 34571      Outpur : 26 missing


#list1 = [1, 7, 5, 4, 3]
#max = 7
#for i in range(1, max):


def missing_number(num1):
    reminder = []
    str1 = ""
    while num1 > 0:
        rem = num1 % 10
        reminder.append(rem)
    
    for i in range(1, max(reminder)):
        if i not in reminder:
            str1 += str(i)

    return str1 + " missing"

print(missing_number(19))

