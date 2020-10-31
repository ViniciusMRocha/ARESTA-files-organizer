list = [1, 0, 0, 0, 1, 0, 1]

new_list = []
for item in list[1:len(list)]:
    if item == 1:
        print(new_list)
        new_list = []
    else:
        new_list.append(item)
