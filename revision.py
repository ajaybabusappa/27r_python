num1 = 12
num1 = num1 + 5
print (num1 + 5)
print (num1)

#Variables - Reassignment possible.
#A.Op - 
#R.Op - >, < , >=, <=, ==, !=
#L.Op -> and, or, not 


num2 = 25

if num2 % 2 == 0:
 print ("Even")
 print ("Evadiki upayogam")
else:
   print ("Odd")


list1 = [1, 3, 54, 54.0, 32, 37, 78, 91]

# print (list1[3])
# print (len(list1))

#print(list1[6])

# print (54.4 % 2)


#Iteration of lists
# for i in list1:
#     if i % 2 == 0:
#         print ("Even", i)
#         print ("Evadiki upayogam")
#     else:
#        print ("Odd")




for i in range(0, len(list1)):
   #print (list1[i])
   if i % 3 == 0:
     print(list1[i])


i = 50
count = 0
while i > 0:
  count += 1
  print ("Hello")
  i -= 1 
  
print (count)

# 1 to 12 numbers print 
for i in range(1, 13):
  print (i)


num = 0
while num <= 12:
    num += 1
    print (num)
    if num == 12:
      break
    



str1 = "Repati Kosam"

for i in str1:
  #if i == 'e' and i == 'a':
  if i in ['e', 'a']:
    break
  print (i)
  print("Ok")


for i in range(0, len(str1)):
  if i % 2 == 0:
    print (str1[i])

#If my focus is on index
# for i in str1:
#   if i % 2 == 0:
#     print (str1[i])
  
#If my requirement is based on value then you can use any type of for loop

#Functions - arguments, parameters, 

# def calc_area(r, r2):
#   area = 3.14 * r ** 2
  
#   print(area)
#   return 6 

# print (calc_area(5, 4))




# *
# * *
# * * *
# * * * *

# for i in range(1, 5):
#   print (i * "* ")


def pattern_fun(n):
  for i in range(1, n+1):
    print (i * "* ")

def rev_pattern_fun(n):
  for i in range(n, 0, -1):
    print (i * "* ")
pattern_fun(6)
rev_pattern_fun(5)

str1 = "abc"
