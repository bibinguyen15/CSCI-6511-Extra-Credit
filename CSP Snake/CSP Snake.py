from data import *
import copy
import time


def snake():
    visited = []  # The position in grid
    constraints = {}
    domains = list(string.ascii_uppercase)[:-1]  # the letters
    variables = []
    empty = []  # Cells that have not been filled yet in the given prompt
    vMap = {}  # vMap is the map of each variable and its domain

    # Setting up problem
    for i, row in enumerate(grid):
        for j in range(5):
            if row[j] != '':
                domains.remove(row[j])
                constraints[(i, j)] = row[j]
                visited.append((i, j))
            else:
                variables.append((i, j))
            empty.append((i, j))

    for v in empty:
        neighbors = getNeighbors(v)
        required = []
        for nei in neighbors:
            if nei in constraints:
                required.append(constraints[nei])

        # vMap value is [domains, neighbors, constraints]
        if v in constraints:
            vMap[v] = [[constraints[v]], neighbors, required]
        else:
            vMap[v] = [[i for i in domains], neighbors, required]

    # Solving the CSP problem
    begin = time.time()
    csp = CSP(variables, vMap, visited)
    result = csp.solve()
    end = time.time()

    print(f"Time taken: {end - begin}s")

    # Printing results
    if result is None:
        print("No solutions")
    else:
        print("Solution is: ")
        printResult(result)
        # print(result)


def printResult(result):
    """
    Function to print result as a grid
    """
    for key, value in result.items():
        # print(key, value)
        grid[key[0]][key[1]] = value
    for row in grid:
        print(row)


class CSP:
    def __init__(self, variables, vMap, visited):
        self.variables = variables
        self.vMap = vMap
        # self.domains = domains
        self.visited = visited
        print(
            f"\nInitialization successful:\n{self.variables}\n{self.vMap}\n{self.visited}\n")

    def solve(self, assignment={}):
        """
        Main recursive solving function
        """
        # If assignment length is same as variables, then all variables have been assigned successfully
        if len(assignment) == len(self.variables):
            return assignment

        # Choose cell to fill according to MCV
        selected = self.selectCell()

        # Ordering the domain according to LCV
        orderedDomain = self.orderDomain(selected)

        for letter in orderedDomain:
            # print(f"Choosing letter {letter} for {selected}")
            # Check consistency
            if self.consistent(selected, letter):
                # Make deep copy to return original in leaf cases
                newMap = copy.deepcopy(self.vMap)
                assign = assignment.copy()

                # Assigning the letter to the cell
                assign[selected] = letter
                self.add(selected, letter)
                # self.printMap()

                if self.backCheck(selected, letter):
                    # Recursive call if backtrack checking is true
                    result = self.solve(assign)
                    if result is not None:
                        return result

                # Returning all values back
                # print(self.vMap, "\n", newMap)
                self.vMap = newMap
                self.visited.remove(selected)

        return None

    def backCheck(self, selected, letter):
        """
        Backtracking check to make sure that once a cell is filled completely, it's still consistent
        """
        # print("In backChecK for:", selected, self.vMap[selected])
        for nb in self.vMap[selected][1]:
            # print("Neighbor", nb, self.vMap[nb])
            # if all neighbors of neighbor is not filled yet
            if len(self.vMap[nb][1]) > len(self.vMap[nb][2]):
                continue

            # All neighbors of nb are filled
            elif len(self.vMap[nb][1]) == len(self.vMap[nb][2]):
                # print(f"All neighbors of {nb} are filled")
                required = []
                for c in self.vMap[nb][2]:
                    required += getLetters(c)
                # print(f"required {required}")

                # Since all neighbors of nb is filled, nb's domain is restricted
                self.vMap[nb][0] = [
                    i for i in self.vMap[nb][0] if i in required]
                if len(self.vMap[nb][0]) == 0:
                    return False
                else:
                    continue
        return True

    def add(self, selected, letter):
        """
        Function to add a letter to selected
        """
        self.vMap[selected][0] = [letter]
        self.visited.append(selected)

        # Update all domains
        for cell in self.variables:
            if cell not in self.visited and letter in self.vMap[cell][0]:
                self.vMap[cell][0].remove(letter)

        # Update constraints for neighboring cells
        for neighbor in self.vMap[selected][1]:
            self.vMap[neighbor][2].append(letter)

    def consistent(self, selected, letter):
        """
        Function checking consistency
        Consistent if either matches consistency requirements or there's still an empty cell
        """
        # print(f"Checking consistency")
        # If neighbors are not filled out
        if len(self.vMap[selected][1]) > len(self.vMap[selected][2]):
            return True

        for c in self.vMap[selected][2]:
            # Check if constraint satisfied
            if letter in getLetters(c):
                # print(f"Letter {letter} satisfied constraint for {c}")
                return True

        return False

    def selectCell(self):
        """
        Selecting cell according to one with the most constraints
        """
        mcv = [(k, v[2])
               for k, v in self.vMap.items() if k not in self.visited]

        # sort according to length of constraints
        mcv.sort(key=lambda elem: len(elem[1]), reverse=True)

        return mcv[0][0]

    def orderDomain(self, cell):
        """
        Ordering domain of a certain cell according to LCV
        The least constraining value is the one that satisfy the most constraints
        """
        # print(f"Cell {cell}: {self.vMap[cell]}")
        values = []
        constraints = []

        # All the values that cell could hold to satisfy constraints
        for c in self.vMap[cell][2]:
            constraints += getLetters(c)
        # print(constraints)

        # If a letter satisfy more constraints, it's ordered first
        for letter in self.vMap[cell][0]:
            consistent = 0
            for c in self.vMap[cell][2]:
                if letter in getLetters(c):
                    consistent += 1

            values.append((letter, consistent))
        values.sort(key=lambda k: k[1], reverse=True)

        return [i[0] for i in values]

    def printMap(self):
        """
        Function to print the vMap
        """
        for key in self.variables:
            print(key, self.vMap[key])


def getLetters(letter):
    """
    Function to return letters next to a certain letter
    """
    # print(alphabet)
    index = alphabet.index(letter)
    nextLetters = []
    if index > 0:
        nextLetters.append(alphabet[index - 1])
    if index < 24:
        nextLetters.append(alphabet[index + 1])
    # if letter == "J":
    # print(f"letter {letter} has {len(nextLetters)} letters next to it: {nextLetters}")
    return nextLetters


def getNeighbors(cell):
    """
    Function to return all the neighbors of a certain cell
    """
    nearby = []
    if cell[0] > 0:
        nearby.append((cell[0] - 1, cell[1]))
    if cell[1] > 0:
        nearby.append((cell[0], cell[1] - 1))
    if cell[0] < 4:
        nearby.append((cell[0] + 1, cell[1]))
    if cell[1] < 4:
        nearby.append((cell[0], cell[1] + 1))
    return nearby


def main():
    snake()


if __name__ == '__main__':
    main()
