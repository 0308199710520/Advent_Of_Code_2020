with open("./Day 11 input.txt") as Day_11_input:
    Day_11 = [list(line.strip("\n")) for line in Day_11_input.readlines()]

def checker():
    global Day_11
    checking_spots = ((-1,-1),(-1,0), (-1,1),(0,-1),(0, 1), (1, -1), (1, 0), (1, 1))

    for y in range(len(Day_11)):
        for x in range(len(Day_11[1])):
            occupied_counter = 0
            try:
                if Day_11[y][x] == ".":
                    continue
            except IndexError:
                continue
            for coord in checking_spots:
                x0, y0 = coord
                try:
                    if Day_11[x + x0][y + y0] == ["#"]:
                        if x + x0>=0 and y + y0 >=0:
                            occupied_counter +=1
                except IndexError:
                    continue

            if occupied_counter >=4:
                Day_11[y][x] = "L"
                continue
            elif occupied_counter == 0:
                Day_11[y][x] = "#"
                continue
            else:
                Day_11[y][x] = "L"
def counter():
    """
    Iterates through the Seat Data noting the number of occupied seats in the current itteration,
    it then appends this data into a list to track the list progression
    """
    #The data
    global Day_11

    counter = 0

    for x in Day_11:
        for y in x:
            if y == "#":
                counter += 1
    return counter


def passthrough():
    pass


def demo_check(y, x):
    global Day_11
    checking_spots = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    for check in checking_spots:
        y0, x0 = check
        print(Day_11[y+y0][x+x0])

for line in Day_11[:3][:3]:
    print(line)

demo_check(0,0)