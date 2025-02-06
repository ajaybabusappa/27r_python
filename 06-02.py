#If else - One quick revision
#2 nested complex if and else


# actual_username = "Dj Tillu"
# actual_password = "Radhika"

# username_input = input("Enter user name")
# password_input = input("Enter password")

# if username_input == actual_username and password_input == actual_password:
#     print("Login succesful and you are Tillu")
# elif username_input != actual_username and password_input != actual_password:
#     print("Wrong Username and password")

# elif username_input != actual_username:
#     print("Username is wrong")
# else:
#     print("Password is wrong")
#     print("Login failed....Nuv nijamgane Tilluvena???")


# # 1 1 1
# # 0 0 0
# # 1 0 0
# # 0 1 0




# #Karthik's question

# path = int(input())

# if path == 1:
#     print("Enter either bear or snake")
#     animal_threat = input("Enter Animal").lower()
#     if animal_threat == 'bear':
#         print("Choose either to fight or flight")
#         decision = input("Flight(tree) or Fight(weapon)")
#         if decision == 'tree':
#             print("Hamayya Bathiki poyam")
#         else:
#             print("Gelichava Chachava?")
#             won = int(input("Enter 1 or 0"))
#             if won == 1:
#                 print("Nenu Gelicha....Roja template")
#             else:
#                 print("Hi Yamaraja")
#     else:
#         print("Choose either to step on it or flight")
#         decision = input("Flight(careful) or Fight(step)")
#         if decision == 'careful':
#             print("Hamayya Bathiki poyam")
#         else:
#             print("Gelichava Chachava?")
#             won = int(input("Enter 1 or 0"))
#             if won == 1:
#                 print("Nenu Gelicha....Roja template")
#             else:
#                 print("Hi Yamaraja")


# else:  #Where are coding for path2
#     pass



#Loops - For loop and while

# for i in range(0, 101, 2):
#     print(i)


# for i in range(1, 101, 2):
#     print(i)


# #3 multiples code
# for i in range(0, 101, 3):
#     print(i)

# 3 X 1 = 3
# 3 X 2 = 6

# for i in range(1, 21):
#     print(3, 'X', i, '=', i * 3)


# for i in range(0, 101, 3):
#     print(3, 'X', int(i/3) ,'=',i)



sum = 0
for i in range(1, 20): #N times => O(N) time complexity or Linear time complexity
    sum += i #sum = sum + i

print(sum)

n = 10

print((n * (n+1))/2) # 1 time -> O(1) or constant time complexity

#Time complexity - Estimate of time taken to complete execution of your code or code piece


n = 20

#20 => 400
#30 => 900
#40 => 1600
# for i in range(0, 20): #O(n square)
#     for j in range(0, 20): # O(m * n)
#         print(i, j)





print("Enter positive numbers or else I will stop execution")

while True:
    num1 = float(input("Enter a number"))
    if num1 <= 0:
        break
    print(num1)


num1 = 2

while num1>0:
    num1 = float(input("Enter a number"))
    print(num1)