str1 = 'a+b-(d * b - {e / f})'
output_str = ''

# for i in str1:
#     if i == '(' or i == ')' or i == '{' or i == '}':
#         pass
#     else:
#         output_str += i

# print(output_str)


# for i in str1:
#     if i not in ['(', ')', '[', ']', '{', '}']:
#         output_str += i


for i in str1:
    if i not in '()[]{}':
        output_str += i

print(output_str)



str1 = "Podhu podhunne class evadu vintadu bro......"
#approach 1

rev_str = ""
for i in str1: #O(n)
    rev_str = i + rev_str 

if str1 == rev_str:
    print("Palindrome")
else:
    print("Not a palindrome")


#approach 2
#MALAYALAM
str1 = "MALAYALAM"
low = 0
high = len(str1) - 1
flag = True
while low < high:
    if str1[low] == str1[high]:
        low += 1
        high -= 1
    else:
        flag = False
        print('not palindrome')
        break

# if low >= high:
#     print("Palindrome")

if flag:
    print("Palindrome")

def check_palindrome(str1):
    low = 0
    high = len(str1) - 1
    while low < high:
        if str1[low] == str1[high]:
            low += 1
            high -= 1
        else:
            return False
    return True


#rev_str = str1[::-1]

str1 = 'take u backward to memories'.lower()
dict1 = {}

for i in str1:
    if i in 'aeiou':
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

#Non duplicate vowels
for i,j in dict1.items():
    if j == 1:
        print(i)


#For duplicate vowels
for i,j in dict1.items():
    if j > 1:
        print(i)
