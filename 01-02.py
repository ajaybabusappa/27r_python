# #Example: Code to find max, min and sum of all elements in a list
# list1 = [1, 45, 8.2, -32, -55, 90]

# max_mem = list1[0]
# min_men = list1[0]
# sum = 0
# for i in range(0, len(list1)):
#     print(list1[i])
#     if list1[i] > max_mem:
#         max_mem = list1[i]

#     if list1[i] < min_men:
#         min_men = list1[i]
    
#     sum += list1[i]

# print(max_mem)
# print(min_men)


# #Q1
# #Basic operations.
# #Take 2 numbers - performmultiply, divide, substract, add
# #Exponent and also floor division
# #Without function and with function.


# num1 = 52
# num2 = 2

# print (num1 + num2)
# print (num1 - num2)
# print (num1 * num2)
# print (num1 / num2)
# print (num1 // num2)
# print (num1 ** num2)

# def simple_operation (num1, num2):
#     sum = num1 + num2
#     sub = num1 - num2
#     mul = num1 * num2
#     div = num1 / num2
#     return sum, sub, mul, div

# res = simple_operation(15, 16)
# print (res)
# #print(simple_operation(15, 16))



# #Q2:Find greatest number in given 2 numbers
# ramesh_age = int(input("Enter ramesh age"))
# suresh_age = int(input("Enter suresh age"))


# if ramesh_age < suresh_age:
#     print ("Suresh is elder to ramesh")
# elif ramesh_age == suresh_age: # Edge case - Never missout on edges cases.
#     print("Twins")
# else:
#     print ("Suresh is younger to Ramesh")


#Variation2 - Assume ages are not equal. Do using Terinary operator

# str1 = 'Suresh is younger' if suresh_age < ramesh_age else 'Ramesh is younger'
# print(str1)

#Q3: Find the greatest or lowest age person among 3 persons. Assume all are not equal
# ramesh_age = int(input("Enter ramesh age"))
# suresh_age = int(input("Enter suresh age"))
# naresh_age = int(input("Enter naresh age"))


# if ramesh_age < suresh_age and ramesh_age < naresh_age:
#     print ("Ramesh is the youngest")
# elif suresh_age < naresh_age:
#     print ("Suresh is youngest")
# else:
#     print("Naresh is the youngest")



# str1 = 'Ramesh is youngest' if ramesh_age < suresh_age and ramesh_age < naresh_age else 'suresh is youngest' if suresh_age < naresh_age else 'naresh is youngest'
# print(str1)



#Q4 Implement a simple calculator 
#Input format - total 3 inputs
#1st input - "add", "mul", "div", "sub" - ADD or Add or ADd - Can be like this also
#2nd and 3rd inputs are - numbers

opt = input("Enter operation to perform").lower()
opd1 = float(input("Enter first number"))
opd2 = float(input("Enter second number"))

if opt == 'add':
    print(opd1 + opd2)
elif opt == 'sub':
    print(opd1 - opd2)
elif opt == 'mul':
    print (opd1 * opd2)
elif opt == 'div': #Division by zero error
    str1 = "Division by zero not possible" if opd2 == 0 else opd1/opd2
    print (str1)
else:
    print ("Invalid operator")



# print(int('21.56')) #This will not work.
# print (int(21.56))




