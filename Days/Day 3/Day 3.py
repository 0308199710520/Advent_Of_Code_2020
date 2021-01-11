import copy

with open("Day 3 Input") as D3Input:
    input_list = [x.strip() for x in D3Input.readlines()]

input_list = [list(x) for x in input_list]
#That has sorted the file input into a matrix for easier traversal

print(len(input_list[1]))
def traversal_checker(start:tuple, step:tuple, traversal_map:list):
    traversal_map_copy = copy.deepcopy(traversal_map)
    x = start[0]
    y = start[1]

    while y < len(traversal_map_copy):
        if x >= len(traversal_map_copy[1]):
            x = x - len(traversal_map_copy[1])
        if traversal_map_copy[y][x] == "#":
            traversal_map_copy[y][x] = "X"
        else:
            traversal_map_copy[y][x] = "O"
        x += step[0]
        y += step[1]

    tree_count = 0
    for i in traversal_map_copy:
        for j in i:
            if j == "X":
                tree_count +=1

    return tree_count
trees = []


for route in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    print(route)
    input_list_copy = []
    input_list_copy = input_list
    trees.append(traversal_checker((0,0), route, input_list_copy))

print(trees)
total = 1

for tree in trees:
    total = total * tree

print(total)
