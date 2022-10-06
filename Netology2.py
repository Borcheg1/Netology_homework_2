from os import getcwd, listdir


def sort_list_file_info(list_):
    for i in range(len(list_) - 1):
        for j in range(len(list_) - 1 - i):
            if list_[j][1] > list_[j + 1][1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
    return list_


directory = getcwd() + r'\test'
folder = listdir(directory)
list_file_info = []

for file_name in folder:
    with open(directory + '/' + file_name, 'r', encoding='UTF-8') as file:
        file_line = file.readlines()
        list_file_info.append([file_name, len(file_line), file_line])

list_file_info = sort_list_file_info(list_file_info)

with open(getcwd() + '/' + 'new_file.txt', 'w', encoding='UTF-8') as new_file:
    for number, item in enumerate(list_file_info):
        if number == len(list_file_info) - 1:
            new_file.write(f"{item[0]}\n{item[1]}\n{''.join(item[2])}")
        else:
            new_file.write(f"{item[0]}\n{item[1]}\n{''.join(item[2])}\n")
