import re
with open("Day 6 input") as Day_6_Input:
    input_list = [x.strip() for x in Day_6_Input.readlines()]

num_of_people = 0
total_value = 0
temp_string = ""
for line in input_list:
    if re.match(r"[a-z]+", line):
        temp_string += line
        num_of_people += 1
    else:
        temp_list = list(temp_string)
        group_dict = {}
        for letter in temp_list:
            if letter in group_dict.keys():
                group_dict[letter]+=1
            else:
                group_dict[letter] = 1
        for pair in group_dict.keys():
            if group_dict[pair] == num_of_people:
                total_value +=1

        group_dict = {}
        temp_string = ""
        num_of_people = 0

        temp_list = list(temp_string)
        group_dict = {}

temp_list = list(temp_string)
for letter in temp_list:
    if letter in group_dict.keys():
        group_dict[letter]+=1
    else:
        group_dict[letter] = 1
for pair in group_dict.keys():
    if group_dict[pair] == num_of_people:
        total_value +=1

print(total_value)
