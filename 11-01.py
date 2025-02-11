#Nearest prime
#Prime numbers in a given range

# num1 = int(input("Enter lower bound"))
# num2 = int(input("Enter upper bound"))

# for p in range(num1, num2 + 1): #(O(m))
#     count = 0
#     for i in range(1, p + 1): #(O(n))
#         if p % i == 0:
#             count += 1

#     if count == 2:
#         print(p, "is prime")
#     # else:
#     #     print(p, "Not prime")




#Nearest prime

num1 = int(input("Enter number")) #5

while True:
    num1 += 1
    count = 0
    for i in range(1, num1 + 1): #(O(n))
        if num1 % i == 0:
            count += 1

    if count == 2:
        maxside_prime = num1
        break



while True:
    if num1 in [0, 1, 2]:
        print("Not exists")
        break
    num1 -= 1
    count = 0
    for i in range(1, num1 + 1): #(O(n))
        if num1 % i == 0:
            count += 1

    if count == 2:
        minside_prime = num1
        break



#Q1: Nearest leap year in the increasing side
#Q2 -Perfect number 6 => 1, 2, 3, 6 => Sum of 1, 2, 3 => 6
#Q3: Find all armstrong number in a given range (100 to 1000)
#153 => 125 + 27 + 1 => 153
#


#2018 => 2020
#2196 =>  2200 (It is not leap year) => 2204


