#Reverse a number using a while loop.
#12345 => 54321
#Inbuilt methods

#12345 => divided by 10 => Q = 1234 , R = 5, rev_num = 5
#1234 => Q = 123, R = 4
#123 => 12, 3
#12 => 1 , 2
#1 => 0, 1


num = 12345
temp = num
sum = 0
count = 0
rev_num = 0
while num > 0:
    rem = num % 10
    sum += rem #Will give you sum of digits
    count += 1 #Total number of digits
    rev_num = rev_num * 10 + rem
    num = num // 10


print(rev_num)

if temp == rev_num:
    print("Palindrome")



#Implement a basic login system where the user has three attempts to enter the correct password using a loop.


user_accountname = 'Pushpa Raj'
user_password = 'Srivalli'

allowed_attempts = 3

while allowed_attempts > 0:
    print("Enter username and password")
    print("You have", allowed_attempts, "attempts")

    username_input = input("Enter username")
    password_input = input("Enter password")

    if user_accountname == username_input and user_password == password_input:
        print("Login succesful")
        break
    else:
        print("Wrong credentials")
        allowed_attempts -= 1




#Implement a menu-driven program where the user can choose to: 1. Find the square of a number. 2. Find the cube of a number. 3. Exit.

choice = input("Enter either square or cube or exit")

while True:
    if choice == 'square':
        user_num_input = float(input("Enter a number to square"))
        print()

    
    elif choice == "exit":
        break
    else:
        print("Invalid input")




#Find if a given number is prime
#Method 1
num1 = int(input("Enter a number to check if it is a prime"))

count = 0
for i in range(1, num1 + 1):
    if num1 % i == 0:
        count += 1

if count == 2:
    print("Given number is prime")
else:
    print("Not prime")


#Method2
flag = True
if num1 == 2:
    print("Is a prime")
else:
    for i in range(2, num1):
        if num1 % i == 0:
            flag = False
            break
    print("Is a prime number") if flag == True else print("Not a prime number")


#Using functions
def is_prime(num1):
    if num1 == 1:
        return False
    if num1 == 2:
        return True
        
    flag = True
    for i in range(2, num1):
    #for i in range(2, int((num1)/2) + 1)
    # for i in range(2, int(num1 ** 0.5) + 1):
        if num1 % i == 0:
            flag = False
            break
    res = "Is a prime number" if flag == True else "Not a prime number"
    return res
    
print(is_prime(17))


#Comparision between Time complexity - O(1) <O(root of n)  < O(n) < O(n square)


# 34 => 34 * 1
# => 17 * 2

# m = a * b => root of m * root of m 
# => 36 => 6 * 6 => 3 * 12

# 64 => 8 * 8
# => 2 * 32
#=> 1 * 64
#=> 4 * 16
#8 * 8
#16 * 4
#64 * 1

#a, b inputs


#Swapping 2 variable values
a = 10
b = 20

a, b = 10, 20

#Method 1
a, b = b, a



a = 10
b = 20

#Method 2 - Using a 3rd variable
temp = a
a = b
b = temp


#Method 3 - Without using any 3rd variable

a, b = 10, 20
a = a + b
b = a - b
a = a - b


#Method 4 - Using xor
# 1 1 0
# 0 0 0
# 1 0 1
# 0 1 1

# a ^ a  = 0
# 0 ^ a = a 

#a ^ a ^ b  = b


a = a ^ b
b = a ^ b # a ^ b ^ b # a
a = a ^ b # a ^ b ^ a # b



