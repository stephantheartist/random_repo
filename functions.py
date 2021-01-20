# # # # my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# # # # list_lenght= len(my_list)
# # # #
# # # # # if list_lenght % 2 == 0 and list_lenght %5 != 0:
# # # # #     print('my list has even lenght')
# # # # #     if list_lenght % 3 ==0:
# # # # #         print('my list has even multipel of 3 lenght')
# # # # #     print('EVEN NEXT INSTRUCTION;')
# # # # # elif list_lenght % 5 == 0:
# # # # #     print('my list has odd lenght but is multiple of 5')
# # # # # else:
# # # # #     print('my list has odd lenght')
# # # # #
# # # # # print('final next instruction')
# # # # my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# # # # list_lenght= len(my_list)
# # # # index = 0 # [0, 1, 2, ...list_lenght - 1]
# # # #
# # # # while index < list_lenght:    # 9 < 10 (True) -> 10< 10(False)
# # # #     list_element = my_list[index]
# # # #
# # # #     print('instruction from while', list_element)
# # # #     index += 1
# # # #     print('index', index)
# # # my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] # lenght 10
# # #
# # # for index, element in enumerate (my_list):
# # #     if element % 2 == 0:
# # #         print(f'{element} from position {index} is even number')
# # #     else:
# # #         print(f'{element} from position {index} is odd number')
# # #
# # my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# # if len(my_list) % 2 != 0:
# #     pass
# # else:
# #     print('else branch')
#
# def sum_of_numbers(a, b):
#     return a + b
#
# def view_sum_numbers(a, b)
#     print(f'sum of{a} and {b} is {a + b}')
#
# nr_1 = 5
# # nr_2 = 7
# my_sum = sum_of_numbers(nr_1, nr_2)
# print('my_sum', my_sum)
def sum_of_numbers(*args, **kwargs):
    print(args)
    print(kwargs)

sum_of_numbers()
sum_of_numbers(1)
sum_of_numbers(1, 2 )
sum_of_numbers(1, 2, 3)
