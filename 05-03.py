# #OOPS - Object oriented programming system
# #Procedural programming 

# #sum, mul, add, sub, 

# def sum():
#     pass



# print("Patern printing")


# def sub():
#     pass



#OOPS -
#class
# #int, float, string, dict, set
# class Calculator:
#     def sum(self, a, b):
#         print(a + b)
#         return a + b
    
#     def sub(self, a, b):
#         return a - b
    
#     def mul(self, a, b):
#         return a * b


# #Object
# calc1 = Calculator()

# calc1.sum(2, 3)
# calc2 = Calculator()
# print(type(calc1))

#constructor - function


class Human:
    #static variables
    species_name = 'Homo Sapiens'
    def __init__(self, name1, age1, dob1):
        self.name = name1 #Instance variables
        self.age = age1
        self.dob = dob1
        print("Human object is created")

    def self_intro(self):
        print(self.name, self.age, self.dob)
    
    def learn(self):
        print(self.name, 'I am learning')
    
human1 = Human('Dj Tillu', 12, '22-12-2012')
human2 = Human('Radhika', 14, '22-12-2010')


print(human1.name)
print(human2.age)
human1.self_intro()
human2.self_intro()

# #First way
# human1.name = 'Dj Tillu'
# human1.age = 12

# print(human1.name)
# # print(human2.name)

print(human1.species_name)
print(human2.species_name)




#Patterns
#1
#3 2
#4 5 6
#10 9 8 7


start = 1
for i in range(1, 6):
    temp_string = ''
    for j in range(0, i): # j - 0, 1; i = 2
        if i >= j:
            if i % 2 != 0:
                temp_string += str(start)
            else:
                temp_string = str(start) + temp_string # 3 2 
            start += 1
    print(temp_string)

#1

#assignment question
#     ********
#   ********
#  ********
# ********
#********