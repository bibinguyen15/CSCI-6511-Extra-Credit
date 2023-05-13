import time
from data import *
import heapdict
from fruit import *


def astar(state, fruitOrder, shortestCost):
    # print(fruitOrder)
    sizeGoal = setGoal(fruitOrder, state)
    closedStates = []
    openStates = heapdict.heapdict()
    openStates[(0, state)] = 0

    # Iterate until the open states list is empty or the goal state is found
    while openStates:
        # Pop the state with the lowest score from the unvisited set
        cost, currentState = openStates.popitem()[0]

        #Check if there is another cost that is shorter, then stop
        if cost > shortestCost:
            return [], cost

        # Check if the goal state has been reached
        if currentState.isGoal():
            # Reconstruct the path from the initial state to the goal state
            # print("this is it-\n", currentState.array)
            path = []
            while currentState:
                path.append(currentState.state)
                currentState = currentState.parent
            path.reverse()
            return path, cost

        # Add the current state to the closedStates set
        visitedArray = currentState.state
        closedStates.append(visitedArray)
        # Generate the neighboring states and add them to the open state set
        for child in currentState.getDescendents():
            # Check if the child is already in the closedStates set
            if child.state not in closedStates:
                # update its score
                heuristic = heuristics(cost, child, fruitOrder, sizeGoal)
                openStates[(cost + 1, child)] = heuristic

    # Return None if the goal state is not reachable
    return None


def heuristics(cost, child, fruitOrder, sizeGoal):
    """
    Heuristics to give an estimation score for each state
    """
    score = 0

    # Check every fruit position in the child state
    for i in range(3):
        for j in range(len(child.state[0])):
            fruit, size = child.state[i][j].type, child.state[i][j].size
            # If not in the right basket
            if fruitOrder[i] != fruit:
                score += 1
            # If not the right size
            if fruit == "apple":
                if int(size) != sizeGoal[0][j]:
                    score += 1
            elif fruit == "banana":
                if int(size) != sizeGoal[2][j]:
                    score += 1
            else:
                if int(size) != sizeGoal[1][j]:
                    score += 1
    return score + cost


def setGoal(fruitOrder, state):
    """
    Generating goal state
    """
    apple, banana, orange = [], [], []
    goal = []
    for i in range(3):
        for j in range(10):
            fruit, size = state.state[i][j].type, state.state[i][j].size
            if fruit == "banana":
                banana.append(size)
            elif fruit == "orange":
                orange.append(size)
            else:
                apple.append(size)

    for fruitType in fruitOrder:
        if fruit == "banana":
            goal.append(sorted(banana))
        elif fruit == "orange":
            goal.append(sorted(orange))
        else:
            goal.append(sorted(apple))

    return goal


def main():
    shortestPath, shortestOrdering, shortestCost = [], [], float('inf')

    start = time.time()

    initialState = State(randomBasket)

    # Iterating through all orders to find the order with the least swaps
    for order in fruitOrdering:
        # print(f"Calculating costs for {order}.")

        #Passing shortestCost through to hopefully shortcircuit the calculations
        path, cost = astar(initialState, order, shortestCost)
        if path:
            print(f"Cost for {order} is {cost} swaps.")
        else:
            print(f"{order} is shortcircuited and stopped at {cost} swaps.")
        if shortestCost > cost:
            shortestOrdering = order
            shortestPath = path
            shortestCost = cost

    end = time.time()

    if shortestPath is not None:
        print(f"It took {shortestCost} swaps to get to goal in this fruit ordering: {shortestOrdering}.")
        if input("Do you want to see path? (leave empty if not)"):
            for p in shortestPath:
                print(p)
    else:
        print(path)

    print(f"Time take: {end - start}s")


if __name__ == '__main__':
    main()
