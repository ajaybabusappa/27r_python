# list1 = [1, 2, 3, 4, 5, 8, 23, 541]
# list2 = [4, 7, 9, 11, 12, 34, 600, 700, 900]

#output = [1, 2, 3, 4, 4, 5, 7, 8, 9, 11, 12, 23, 34, 541, 600]



# list1 = [4, 5, 7, 8]
# list1.extend([9, 7, [11, 22]])
# #[4, 5, 7, 8, 9, 7, [11, 22]]



#T.C - O(n1 + n2)
#S.C - O(n1 + n2)
def merge_helper(list1, list2):
    low1, low2 = 0, 0
    res = []
    while low1 < len(list1) and low2 < len(list2):
        if list1[low1] < list2[low2]:
            res.append(list1[low1])
            low1 += 1 
        else:
            res.append(list2[low2])
            low2 += 1


    res.extend(list1[low1:])
    res.extend(list2[low2:])
    return res


#merge_helper(list1, list2)

def merge_sort(list1, low, high):
    if low == high:
        print("Printing single list element", list1[low: high + 1])
        return list1[low: high + 1]
    #print(list1[low: high+1])
    mid = (low + high) // 2

    left_sorted_list = merge_sort(list1, low, mid)
    right_sorted_list = merge_sort(list1, mid + 1, high)
    sorted_list = merge_helper(left_sorted_list, right_sorted_list)
    list1[low: high+1] = sorted_list
    return sorted_list


list1 = [55, 10, -32.3, -2, 72, 99, 110, 6.2, -32]

merge_sort(list1, 0, len(list1) - 1)
print(list1)







list1[5] = 10
list1 [7] = 11

list1[5: 7] = [2, 3]