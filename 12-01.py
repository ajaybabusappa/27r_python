#Fibnocci numbers
# #f(n) = f(n-1) + f(n-2)
# #f(0) = 0, f(1) = 1

# input_num = int(input("Enter number of fib needed"))

# #0 1 1 2 3 5 8 13 21

# #step1 - init bases 
# n1 = 0
# n2 = 1


# print(n1)
# print(n2)

# for i in range(0, input_num - 2): # range(2, input_num)
#     temp = n1 + n2
#     n1 = n2
#     n2 = temp
#     print(temp)


#Armstrong number
#100 - 999 => 
#153 => 1 + 125 + 27 => 153
#1435 => 1 + 256 + 81 + 625 



num1 = int(input("Enter a number to check if it's a amstrong number"))

temp = num1

#1452 => 145 => 14 => 1 => 0

sum = 0
while temp> 0:
    rem = temp % 10
    print(rem)
    sum += rem ** 3
    temp = temp // 10


print("Armstrong") if sum == num1 else print("Not")


#Only for 3 digit numbers
lower_range = 100
upper_range = 10000

for i in range(lower_range, upper_range + 1):
    temp = i

#1452
    temp_str = len(str(i))

    sum = 0
    while temp> 0:
        rem = temp % 10
        sum += rem ** temp_str
        temp = temp // 10
    
    if i == sum:
        print(i, "Is Armstrong")





#3437 => 3, 3, 7 => 13
#912780 => 2, 7 => 7


#901238
#701238
