# for i = 0

# list = [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
# my_list = [0, 4]

# # print(0 % 2)
# for i in range(20):
#     if i % 2 == 0:
#         my_list.append(i**2)

# print(my_list)

# my_list = [i**2 for i in range(20) if i % 3 == 0]
# print(my_list)


# [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]


# set = {'Maksudur', 'Khan', 'Maateen'}

# dic = {'career': 'TeleTalk', 'country': 'Bangladesh', 'name': 'Maateen'}
#
#
#
# n_list = [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]


# a_list = ['Maateen', 'Khan', 'Maksudur', 'a', 'b', 'c']

# my_set = {i for i in a_list if len(i) > 4}

# print(my_set)


# a_list = ['name', 'country', 'career', 'Bd']
# b_list = ['Maateen', 'Bangladesh', 'TeleTalk']

# c = zip(a_list, b_list)
# print(set(c))

# my_dict = {i: j for i, j in zip(a_list, b_list)}
# print(my_dict)

my_dict = {'career': 'TeleTalk', 'country': 'Bangladesh', 'name': 'Maateen'}
new_dict = {key: value for value, key in my_dict.items()}

print(new_dict)
new_dict = {key: value for key, value in my_dict.items()}

print(new_dict)
