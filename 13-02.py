#2 types of functions - Void, Functions with return statements 
def even_or_odd (x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd", "Even or odd", "Edho okati"
    

def void_exmp():
    print("Feb 14 plans ento")



res = even_or_odd(11)
print(res)
print(even_or_odd(11))

print(void_exmp())
res1 = void_exmp()
print(res1)


#Prime using function
def check_if_prime(num1):
    if num1 <= 1:
        return False 
    for i in range(2, num1):
        if num1 % i == 0:
            return False
    return True

input_num = int(input("Enter number to check if prime"))

# function_res = check_if_prime(input_num)
# print(input_num, "is prime") if function_res else print(input_num, "Not a prime")
print(input_num, "is prime") if check_if_prime(input_num) else print(input_num, "Not a prime")



#Armstrong in range

#Function1 - We can write a function which checks if a given number is armstrong number. Call this for 
# all the numbers in the range
#Function2 - Function accepts lower bound and upper bound and directly prints all armstrong numbers in the range.

def check_if_armstrong(num1):
    #Implement the logic here
    temp = num1
    res = 0
    while temp > 0:
        rem = temp % 10
        res += rem ** len(str(num1))
        temp = temp // 10
    
    return res == num1
    # res =  True if res1 == num1 else False
    # return res

lower_bound = int(input("Enter the lower bound"))
upper_bound = int(input("Enter the upper bound"))

# for i in range(lower_bound, upper_bound + 1):
#     #Now I will call a function to check if it is armstrong number
#     if check_if_armstrong(i):
#         print(i)






#Second way
def print_armstrong_in_range(lower_bound, upper_bound):
    for i in range(lower_bound, upper_bound + 1):
        #Implement the logic
        if 


print_armstrong_in_range(upper_bound, lower_bound)





#Nearest prime
#left side nearest prime 
#Right side neartest prime
#Substractions you will find the nearest prime


#One function for left side prime
#One function for right side prime


#Call these functions
#work on returned values


num=int(input("enter a num"))
while True:
    num=num+1
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num)
        max_num=num
        break
while True:
    if num in [0,1,2]:
        print("not exists")
        break
    num=num-1
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num)
        min_num=num
        break
greater=max_num-num
smaller=min_num-num
if greater<smaller:
    print(max_num)
else:
    print(min_num)


#Converting this into function
def check_if_prime(num1):
    if num1 <= 1:
        return False 
    for i in range(2, num1):
        if num1 % i == 0:
            return False
    return True


def find_neareast_greater_prime(num1):
    while True:
        num=num+1
        if check_if_prime(num):
            return num
        

def find_neareast_lesser_prime(num1):
    while True:
        if num in [0,1,2]:
            print("not exists")
            return
        num=num-1
        if check_if_prime(num):
            return num
        
greater = find_neareast_greater_prime() - num
smaller = num - find_neareast_lesser_prime()
if greater<smaller:
    print(max_num)
else:
    print(min_num)