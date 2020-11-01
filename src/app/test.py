import json

list = [1, 0, 0, 0, 1, 0, 1]

new_list = []
for item in list[1:len(list)]:
    if item == 1:
        print(new_list)
        new_list = []
    else:
        new_list.append(item)

path = '../out/temp/flag.pdf'
print(path[:-4])


# Python program to illustrate
# enumerate function in loops
l1 = ["eat", "sleep", "repeat"]

# changing index and printing separately
for count, file in enumerate(l1, 1):
    print(count, file)


def load_map(path_to_map):
    with open(path_to_map) as json_file:
        json_content = json.load(json_file)
        return json_content


map = load_map('../data/map.json')

for i in range(1, 5):
    # value =
    print(map["{}".format(i)])
