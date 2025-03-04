# str1 = "WElcome 25r from 27r".lower()
# res_str = ""

# for i in str1:
#     if i not in 'aeiou':
#         res_str = i + res_str


# print(res_str)



# str1 = "are the google docs are better than word docs?"
# word_list = str1.split()
# print(word_list)

# res_list = []

# max_string = word_list[0]
# for i in word_list:
#     if len(i) >= len(max_string):
#         if len(i) > len(max_string):
#             res_list.clear()
#         max_string = i
#         res_list.append(i)

# print(res_list)


# print('b' > 'ba')
# print('e' > 'ba')

# print('apple' > 'ball')




#longest palindrome in a string
str1 = 'abccbc'


#palindrome

#{1, 2} , {1, 5, 2, 7}
#ab, abbbab

#a
#ab
#abc, abcc, abccb, abccbc - str1[0: 6]
#b
#bc
#bcc, bccb, bccbc
#c
#cc

# def check_palindrome(str1):
#     return str1 == str1[::-1]

# max_string = str1[0]
# for i in range(len(str1)):
#     for j in range( i+1, len(str1)+1):
#         sub_str = str1[i: j]
#         if check_palindrome(sub_str):
#             if len(sub_str) > len(max_string):
#                 max_string = sub_str

# print(max_string)

# print(max_string.find('bc'))


# # str1 = 'takeyouforward'
# # str2 = 'ake'
# # index_at = -1

# # for i in range(len(str1)): #t
# #     temp = i
# #     spy = True
# #     for j in range(len(str2)):#f
# #         if temp < len(str1) and str1[temp] == str2[j]:
# #             temp += 1
# #         else:
# #             spy = False
# #             break
# #     if spy == True:
# #         index_at = i

# # print(index_at)













# str1 = 'takeyouforward' #f index 7
# str2 = 'farward' #0
# index_at = -1

# for i in range(len(str1)): #t
#     spy = True
#     temp = i #7
#     for j in range(len(str2)):#f
#         if temp < len(str1) and str1[temp] == str2[j]:
#             temp += 1 #8
#         else:
#             spy = False
#             break
#     if spy == True:
#         index_at = i

# print(index_at)




#Patterns

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *


n = 6

for i in range(0, n):
    for j in range(0, n):
        print("* ", end = '')
    print()


# for i in range(0, n):
#     print(n * '* ')


for i in range(0, n):
    for j in range(0, n):
        if i >= j:
            print("* ", end = '')
    print()

print("----------------")

print("----------")

for i in range(0, n):
    for j in range(0, n):
        if i <= j:
            print("* ", end = '')
        else:
            print("  ", end='')
    print()





for i in range(0, n):
    for j in range(0, n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("* ", end = '')
        else:
            print('  ', end = '')
    print()


n = 8
for i in range(0, n):
    for j in range(0, n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or i + j == n -1:
            print("* ", end = '')
        else:
            print('  ', end = '')
    print()



#

n = 8
for i in range(0, n):
    for j in range(0, n):
        if j == 0 or i == n-1 or i == j:
            print("* ", end = '')
        else:
            print('  ', end = '')
    print()


#q1 -

# * * * * *
# * * * *
# * * *
# * * 
# *

#1 2 3 4 5 6
#1 2 3 4 5 6
#1 2 3 4 5 6
#1 2 3 4 5 6


for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j, end=' ')
    print()



for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i >= j:
            print(j, end=' ')
    print()


start = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i >= j:
            print(start, end=' ')
            start += 1
    print()



#1
#2 3
#4 5 6
#7 8 8 10



#Assignment 3
# *
# * * 
# * * *
# * * * *
# * * * 
# * * 
# *