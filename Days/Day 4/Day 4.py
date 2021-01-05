import re

with open("Day 4 Input") as infi:
    input_data = [line.strip("\n") for line in infi]

temp_string = ""
pprt_info = []

i = 0
while i < len(input_data)-1:
    if input_data[i] != "":
        temp_string = temp_string + input_data[i] + " "
        #print(temp_string)
        i += 1
    else:
        pprt_info.append(temp_string)
        temp_string = ""
        i += 1
count = 0

for pprt in pprt_info:
    pprt = pprt.rstrip(" ")
    pprt = pprt.split(" ")
    keys = []

    for value in pprt:
        keys.append(value.split(":")[0])
    if "cid" in keys:
        keys.remove("cid")
    if len(keys)==7:
        count+=1
    else:
        continue

print(count)

