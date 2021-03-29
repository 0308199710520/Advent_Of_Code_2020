with open("Day 12 input.txt") as Day_12_Input:
    Input = [(line[:1], int(line[1:].strip("\n"))) for line in Day_12_Input]

# marks the current position of the ship
ship_position = [0, 0]

# marks the position of the waypoint relative to the ship
waypoint_position = [1, 10]

def waypoint_rotation(waypoint: list, operation: str) -> list:
    """
    This rotates the waypoint around the ships current position , simulating
    the movement of the waypoint relative to the ship
    """

    waypoint[0], waypoint[1] = waypoint[1], waypoint[0]

    #Right Turn
    if operation == "R":
        waypoint[0] *= -1

    #Left Turn
    if operation == "L":
        waypoint[1] *= -1

    return waypoint

def waypoint_translation(waypoint: list, operation: str, magnitude: int):

    compass_dict = {
        "N": (magnitude, 0),
        "E": (0, magnitude),
        "S": (-magnitude, 0),
        "W": (0, -magnitude),
    }

    for index in range(2):
        waypoint[index] += compass_dict[operation][index]

    return waypoint


def ship_movement(waypoint: list, magnitude: int, position: list) -> list:
    for i in range(len(position)):
        position[i] += waypoint[i] * magnitude

    return position

for operation in Input:
    if operation[0] in {"L", "R"}:
        if operation[1] == 180:
            for _ in range(2):
                waypoint_position = waypoint_rotation(waypoint_position, operation[0])

        waypoint_position = waypoint_rotation(waypoint_position, operation[0])
        continue

    if operation[0] in {"N", "S", "E", "W"}:
        waypoint_position = waypoint_translation(waypoint_position, operation[0],operation[1])
        continue
    if operation[0] == "F":
        ship_position = ship_movement(waypoint_position, operation[1], ship_position)


print(sum([abs(i) for i in ship_position]))


#print(waypoint_translation([12, 20], "R"))