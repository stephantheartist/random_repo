my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list)
my_sliced_list = my_list[0:]
my_sliced_list.sort()
print('sliced list', my_sliced_list)

my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list)
my_sliced_list = my_list[0:]
my_sliced_list.sort(reverse=True)
print('sliced list descending', my_sliced_list)


my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
for num in my_list:
    if num % 2 != 0:
        print( num, end=  " ")


my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
for num in my_list:
    if num % 2 == 0:
        print( num, end=  " ")




