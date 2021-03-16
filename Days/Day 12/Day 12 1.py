with open("Day 12 input.txt") as Day_12_Input:
    Input = [(line[:1], int(line[1:].strip("\n"))) for line in Day_12_Input]

distance_storage = [0, 0]
bearing = 1


def compass_directions(value, direction) -> tuple:
    compass_dict = {
        "N": (value, 0),
        "E": (0, value),
        "S": (-value, 0),
        "W": (0, -value),
        0: (value, 0),
        1: (0, value),
        2: (-value, 0),
        3: (0, -value),
    }

    return compass_dict[direction]


for operation in Input:
    # unpack the tuple of the steps movement information
    action, magnitude = operation
    if action in {"N", "S", "E", "W"}:
        # print(compass_directions(value, direction)[0])
        distance_storage[0] += compass_directions(magnitude, action)[0]
        # print(compass_directions(value, direction)[1])
        distance_storage[1] += compass_directions(magnitude, action)[1]
        continue
    if action in {"R", "L"}:
        if action == "R":
            bearing += (magnitude / 90)
            if bearing >= 4:
                bearing -= 4

        if action == "L":
            bearing -= (magnitude / 90)
            if bearing < 0:
                bearing += 4
        continue

    distance_storage[0] += compass_directions(magnitude, bearing)[0]
    distance_storage[1] += compass_directions(magnitude, bearing)[1]

print(sum([abs(i) for i in distance_storage]))

'''
    ship_direction = {
                        0: compass_directions["N"],
                        90: compass_directions["E"],
                        180: compass_directions["S"],
                        270: compass_directions["W"],
                      }
'''
