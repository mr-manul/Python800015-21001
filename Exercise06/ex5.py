def search_common(list1, list2):
    common_values = list(set(list1) & set(list2))
    return common_values

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_list = search_common(list1, list2)
print(common_list)
