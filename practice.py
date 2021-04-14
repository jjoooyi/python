# words = 'Connect Foundation'

# if 'F' in words:
#     words.lower()
#     nwords = words.replace(words[7], '&')
# else:
#     print(words)
# print(words)
# print(nwords)

# # i = hex(int(input()))
# # print(i)

# print(pow(2, 10))

with open('test.txt', 'r', encoding='utf8') as f:
    # for line in f:
    #     print(line.strip())

    lines = f.readlines()

    dlist = []
    ddict = {}

    for line in lines:
        line = line.strip('\n')
        dlist = line.split(',')
        # line = [i.strip() for i in line]
        print(dlist)
f.close()


file = open('test.txt', mode='r', encoding='utf-8-sig')
lines = file.readlines()
file.close()
my_dict = {}
my_list = []
for line in lines:
    line = line.split(',')
    line = [i.strip() for i in line]
    print(line)
