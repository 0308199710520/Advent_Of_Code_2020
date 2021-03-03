import os

for day in range(1, 26):
    os.makedirs(f"./Days/Day {day}")


for day_folder in os.listdir("./Days"):
    if len(os.listdir(f"./Days/{day_folder}/")) == 0:
        with open(f"./Days/{day_folder}/{day_folder} input.txt", "w") as temp:
            pass
        with open(f"./Days/{day_folder}/{day_folder} 1.py", "w") as temp:
            pass
        with open(f"./Days/{day_folder}/{day_folder} 2.py","w") as temp:
            pass

