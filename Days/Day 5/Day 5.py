with open("Day 5 input") as day_5_input:
    input_list =[x.split() for x in day_5_input.readlines()]
#print(input_list[0][0])
seat_id = []
highest_value = 0
seat_dict = {}
for i in range(0,len(input_list)):
    a,b = input_list[i][0][:7],input_list[i][0][-3:]

    #a = a[::-1]
    #b = b[::-1]

    a_bin = ""
    b_bin = ""
    for i in range(len(a)):
        if a[i] == "B":
            a_bin += "1"
        else:
            a_bin += "0"
    for i in range(len(b)):
        if b[i] == "R":
            b_bin += "1"
        else:
            b_bin += "0"

    seat_id.append((int((a_bin), 2), int((b_bin), 2)))

print(sorted(seat_id))
all_combos = []
for x in range(11, 105):
    for y in range(1,7):
        all_combos.append((x,y))

for z in all_combos:
    if z not in seat_id:
        print(z)
