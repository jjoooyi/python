# my_list = []

# with open('test.txt', 'r', encoding='utf8') as f:
#     lines = f.readlines()
#     columns = []  # To store column names

#     i = 1
#     for line in lines:
#         line = line.strip()
#         if line:
#             if i == 1:
#                 columns = [item.strip() for item in line.split(',')]
#                 i = i + 1
#             else:
#                 d = {}
#                 data = [item.strip() for item in line.split(',')]
#                 for index, elem in enumerate(data):
#                     d[columns[index]] = data[index]

#                 my_list.append(d)  # append dictionary to list

# print(my_list)

import json

my_list = []

with open('test.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()

    dindex = []
    i = 1

    for line in lines:
        line = line.strip()
        if line:  # 값이 존재하면!
            if i == 1:
                dindex = [index.strip() for index in line.split(',')]
                i += 1
            else:
                d = {}
                data = [item.strip() for item in line.split(',')]
                for i, elem in enumerate(data):
                    d[dindex[i]] = data[i]
                my_list.append(d)
print(my_list)
print(json.dumps(my_list, ident=4))
