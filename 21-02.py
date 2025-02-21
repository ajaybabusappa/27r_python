# #Recursion - a function calling itself is called recursion
# #Factorial - 5 * 4! => 4 * 3! = 3 * 2! => 2 * 1! 

# def factorial (n):
#     if n == 1 or n == 0:
#         return 1
    
#     return n * factorial(n-1)

# # print(factorial(5))


# def fib (n):
#     if n == 0 or n == 1:
#         return n
#     return fib(n-1) + fib(n-2)


# #sum of digits
# num1 = 23564

# #2356, 4
# #235, 6
# #23, 5
# #2, 3
# #0, 2

# def sum_of_digits(num1):
#     if num1 == 0:
#         return 0
    
#     rem = num1 % 10
#     return rem + sum_of_digits(num1 // 10)

# print(sum_of_digits(23564))



# #a power b = a * (a power b - 1)
# #b == 0 return 1
# #b == 1 return a


# def exponent (a, b):
#     if b == 0:
#         return 1
#     return a * exponent(a, b - 1)


#Reverse a string
new_str1 = ""
str1 = "Reverse a string"

for i in str1:
    new_str1 = i + new_str1

print(new_str1)


#Reverse
#Revers, e
#Rever, s
#Reve, r
#Rev, e
#Re, v
#R, e
#'', R


def reverse_string(str1):
    if len(str1) <= 0:
        return ''
    return str1[-1] + reverse_string(str1[:-1])


def reverse_string_no_slice(str1, len):
    if len == 0:
        return ''
    return str1[len - 1] + reverse_string_no_slice(str1, len - 1)



print(reverse_string("Reverse"))
print(reverse_string_no_slice("Reverse", len('Reverse')))






#LEVEL => L, L , need to check for EVE
#MADAM



#MALAYALAM
#M, M ; ALAYALA
#A, A; LAYAL
#L,L; AYA
#A,A, Y



def is_palindrome(str1):
    if len(str1) in [0, 1]:
        return True
    return str1[0] == str1[-1] and is_palindrome(str1[1:-1])

print(is_palindrome("MALAYALAM"))
print(is_palindrome("SATISH"))


#[1, 4, 9, 11, 13, 17]
#first_ele = 1
#rec_max = max in remaining list


def max_in_list(list1):
    if len(list1) == 1:
        return list1[0]
    
    first_elemet = list1[0]
    rec_max = max_in_list(list1[1:])

    final_max = first_elemet if first_elemet > rec_max else rec_max
    return final_max

list1 = [1, 4, 9, 111, 13, 92]
print(max_in_list(list1))

