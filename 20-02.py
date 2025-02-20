list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def print_matrix(list2):
    for i in range(len(list2)):
        for j in range(len(list2[i])):
            print(list2[i][j], end=" ")
        print()

print_matrix(list1)
print(list1)
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if i <= j:
            list1[i][j], list1[j][i] = list1[j][i], list1[i][j]

print(list1)
print_matrix(list1)

#4 coord - 0, 2 => 2
#9 - 1, 1 => 2
#3 - 2, 0  => 2


#0, 3 => 3
#1, 2 => 3
#2, 1 => 3
#3, 0 => 3


#Diagonals sum

sum = 0
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if i == j or i + j == len(list1) -1 :
            sum += list1[i][j]
            if i == j and i + j == len(list1) -1:
                sum += list1[i][j]

print(sum)


def print_matrix_space(list2):
    for i in range(len(list2)):
        for j in range(len(list2[i])):
            if i == 0 or j == 0 or i == len(list1)-1 or j == len(list1[i])-1:
                print(list2[i][j], end=" ")
            else:
                print(" ", end=" ")
        print()

print_matrix_space(list1)