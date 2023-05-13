import copy


class Fruit:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.type = name
        # Making fruit type by its name
        while not self.type.isalpha():
            self.type = self.type[:-1]

    def __repr__(self):
        return self.name


class State:
    def __init__(self, state, moves=0, parent=None):
        self.state = state
        self.moves = moves
        self.parent = parent

    def getDescendents(self):
        """
        Get child nodes of state by swapping 1
        """
        descendents = []
        # Swap any two fruit rows
        for i in range(3):
            for j in range(len(self.state[0])):
                for trailJ in range(j + 1, len(self.state[0])):
                    newArr = copy.deepcopy(self.state)
                    newArr[i][j], newArr[i][trailJ] = newArr[i][trailJ], newArr[i][j]
                    descendents.append(State(newArr, self.moves + 1, self))
        # Swap any two fruits in the same row
        for i in range(3):
            for j in range(len(self.state[0])):
                for trailI in range(i + 1, 3):
                    newArr = copy.deepcopy(self.state)
                    newArr[i][j], newArr[trailI][j] = newArr[trailI][j], newArr[i][j]
                    descendents.append(State(newArr, self.moves + 1, self))
        return descendents

    def isGoal(self):
        """
        Test if the state is a goal state or not
        """
        for i in range(3):
            fruit = self.state[i][0].type
            for j in range(len(self.state[0])):
                # If fruits not in the right row or not in order, then not goal
                # print(self.array[i][j], self.array[i][j+1])
                if (j < 9 and self.state[i][j].size > self.state[i][j + 1].size) \
                        or self.state[i][j].type != fruit:
                    return False
        return True
