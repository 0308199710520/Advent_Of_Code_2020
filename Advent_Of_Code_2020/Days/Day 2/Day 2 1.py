import re

with open("Day 2 Input") as inputs:
    input_list = [x.strip() for x in inputs.readlines()]

print(input_list)
split_input_list = []

for line in input_list:
    split_input_list.append(re.split(r":", line))

for i in split_input_list:
    i.append(i[0][-1])
    i[0] = i[0][0:-1]
    i.append(re.split(r"-",i[0]))
    i.pop(0)

#This returns all the metadata required for step 2

def pswd_checker(password_metadata:list):
    password = password_metadata[0].strip()
    password_key = password_metadata[1]
    occ_range = range(int(password_metadata[2][0]), int(password_metadata[2][1]) +1)
    occ_count = 0

    for i in range(0, len(password)):
        if password[i] == password_key:
            occ_count +=1

    if occ_count in occ_range:
        return True
    else:
        return False



#print(pasdwords)

def pswd_checker_2(password_metadata:list):
    password = password_metadata[0].strip()
    password_key = password_metadata[1]
    occ_pos = password_metadata[2]
    occ_count = 0

    for i in occ_pos:
        if password[int(i)-1] == password_key:
            occ_count +=1

    if occ_count == 1:
        return True
    else:
        return False

pasdwords = 0
for password in split_input_list:
    if pswd_checker_2(password):
        pasdwords +=1

print(pasdwords)