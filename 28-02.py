# Given a dictionary with nested dictionaries sort the inner dictionaries by value
dict1={"a":1,"b":-1,"c":2,"d":-5}
temp_list = list(dict1.items())
for i in range(len(temp_list)):
    for j in range(len(temp_list)-1):
        if temp_list[j][1] > temp_list[j + 1][1]:
            temp_list[j],temp_list[j + 1] = temp_list[j + 1], temp_list[j]
print(temp_list)

dict1 = dict(temp_list)
print(dict1)


def sort_dict(dict1):
    temp_list = list((dict1.items()))
    for i in range(len(temp_list)):
        for j in range(len(temp_list)-1):
            if temp_list[j][1] > temp_list[j + 1][1]:
                temp_list[j],temp_list[j + 1] = temp_list[j + 1], temp_list[j]
    dict1 = dict(temp_list)
    return dict1
dict_input = {"A":{"x":5,"y":-4},"B":{"x":10,"y":-3}}
for i, j in dict_input.items():
    dict_input[i] = sort_dict(j)
print(dict_input)


dict1={"y":-3,"x":1}
print(dict(sorted(dict1.items())))

# based on values
print(dict(sorted(dict1.items(),key = lambda item:item[1])))


# string to sort
def sort_str(str1):
    temp_list = list(str1)
    for i in range(len(temp_list)):
        for j in range(len(temp_list)-1):
            if temp_list[j] > temp_list[j + 1]:
                temp_list[j],temp_list[j + 1] = temp_list[j + 1],temp_list[j]

    fin_str = "".join(temp_list)
    return fin_str
print(sort_str("hello"))

temp_list = sorted("hello")
new_str = "".join(temp_list)
print(new_str)


# grouping anagrams
list1=["ate","eat","tea","cat","act","tac","hit"]
def grp(list1):
    for i in range(len(list1)):
        for j in range(len(list1)-1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1],list1[j]

    fin_list = " ".join(list1)
    return fin_list
print(grp(list1))

list1=["ate","eat","tea","cat","act","tac","hit"]
res_dict1 ={}
for i in list1:
    temp_str = sort_str(i)
    if temp_str in res_dict1:
        res_dict1[temp_str].append(i)
    else:
        res_dict1[temp_str] = [i]
print(res_dict1)