Day_11 = [[1]]

def checker(plan):

    checking_spots = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    for y in range(len(plan)):
        for x in range(len(Day_11[0])):

            occupied_counter = 0

            if Day_11[y][x] == ".":
                continue

            counter = proximity_checker(y, x plan)
            if counter == 0:
                plan[y][x] = "#"

            if counter >= 4:
                plan[y][x] = "L"

    return plan



def proximity_checker(y, x, plan):
    checking_spots = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    counter = 0

    for check in checking_spots:
        y0,x0 = check
        if 0 <= (x+x0) <= len(plan)-1 and 0 <= (y+y0) <= len(plan[1])-1:
            if plan[y+y0 ][x + x0] == "#":
                counter +=1

    return counter