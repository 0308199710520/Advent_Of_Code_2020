with open("Day 9 input.txt") as Day_9_Input:
    Input_List = [int(line) for line in Day_9_Input.readlines()]

class FILO_stack:
    """The structure for holding the query values"""
    def __init__(self, max_length=10):
        self.stack = []
        self.max_length = max_length

    def length(self):
        return len(self.stack)

    def max_length(self):
        return self.length() == self.max_length()

    def add_value(self, value):
        if self.length() == self.max_length:
            self.stack.pop(-1)
            self.stack.insert(0 ,value)

class checker(FILO_stack):


