from data import *
import copy


def snake():
    variables = [] # The position in grid
    constraints = {}
    domains = list(string.ascii_uppercase)[:-1] #the letters
    vMap = {}

    for i, row in enumerate(grid):
        for j in range(5):
            if row[j] != '':
                domains.remove(row[j])
                constraints[(i, j)] = row[j]
            else:
                variables.append((i, j))

    print(variables)
    print(constraints)

    for v in variables:
        vConstraints = []
        flag = False
        if (v[0] + 1, v[1]) in constraints:
            flag = True
            vConstraints.append(constraints[(v[0] + 1, v[1])])
        if (v[0], v[1] + 1) in constraints:
            flag = True
            vConstraints.append(constraints[(v[0], v[1] + 1)])

        if (v[0] - 1, v[1]) in constraints:
            flag = True
            vConstraints.append(constraints[(v[0] - 1, v[1])])
        if (v[0], v[1] - 1) in constraints:
            flag = True
            vConstraints.append(constraints[(v[0], v[1] - 1)])

        vMap[v] = [[], [i for i in domains], vConstraints]
        #return variables, cMap, domains
        if flag:
            print(v, vMap[v])

    return variables, cMap, domains


class CSP:
    def __init__(self, variables, cMap, domains):
        self.variables = variables #The position in grid
        self.cMap = cMap #Each position and its information
        self.domains = domains #The total letters
        self.assigned = []

    def csp(variables, cMap, domains, assignment={}):
        if len(assignment) == len(variables):
            return assignment

        #select position to fill
        selected = self.selectPos()

        #Order the letters to choose
        orderedLetter = self.orderLetters()

        for letter in orderedLetter:
            if self.consistent(selected, letter, assignment):
                nMap = copy.deepcopy(self.cMap)
            #From project 2
            '''
            Project 2 stuff from here on
            '''
            if self.consistent(selected, color, assignment):
                # Make deep copy to return to original in leaf cases
                nGraph = copy.deepcopy(self.graph)

                # Assigning the color to the node
                assign = assignment.copy()
                assign[selected] = color
                self.graph[selected][0] = [color]
                #print("Assigning", selected, "with", color)

                print(assign)

                # Add to visited
                self.visited.append(selected)

                if self.ac3(selected):
                    result = self.solve(assign)
                    if result is not None:
                        return result

                # Return all values back
                self.graph = nGraph
                self.visited.remove(selected)

        return None

    def ac3(self, selected):
        for neighbor in self.graph[selected][1]:
            recheck = True
            if neighbor not in self.visited:
                if len(self.graph[neighbor][0]) == 1:
                    recheck = False
                if self.graph[selected][0][0] in self.graph[neighbor][0]:
                    self.graph[neighbor][0].remove(
                        self.graph[selected][0][0])
                if not self.graph[neighbor][0]:
                    print(neighbor, "has empty domain by forward checking")
                    return False
                if len(self.graph[neighbor][0]) == 1 and recheck:
                    print("Node", neighbor, "now has",
                          self.graph[neighbor][0])
                    return self.ac3(neighbor)

        # self.printGraph()
        return True

    def consistent(self, selected, color, assignment):
        for neighbor in self.graph[selected][1]:
            if assignment.get(neighbor) == color:
                return False
        return True

    def selectNode(self):
        # Choose based on most constraints, first choose one with least domain
        minDomain = len(
            min([v[0] for k, v in self.graph.items() if k not in self.visited],
                key=len))
        mcv = [(k, v[1])
               for k, v in self.graph.items() if len(v[0]) == minDomain and k not in self.visited]

        mcv.sort(key=lambda elem: len(elem[1]), reverse=True)
        #print("Selected node is:", mcv[0][0], "from", mcv)
        return mcv[0][0]

    def orderColor(self, node):
        colors = []
        for color in self.graph[node][0]:
            consistent = 0
            for neighbor in self.graph[node][1]:
                consistent += len([i for i in self.graph[neighbor]
                                  [0] if i != color])
            colors.append((color, consistent))

        # want to sort based on highest consistency ratings
        colors.sort(key=lambda elem: elem[1], reverse=True)

        return [i[0] for i in colors]


    '''
        def ac3(self, selected):
            # For now only do simple forward checking
            for neighbor in self.graph[selected][1]:
                if neighbor not in self.visited:
                    if self.graph[selected][0][0] in self.graph[neighbor][0]:
                        self.graph[neighbor][0].remove(
                            self.graph[selected][0][0])
                    if not self.graph[neighbor][0]:
                        print(neighbor, "has empty domain")
                        return False
    
            # self.printGraph()
            return True    
        
        def ac3(self, selected):
            # For now only do simple forward checking
            for neighbor in self.graph[selected][1]:
                if neighbor not in self.visited:
                    if self.graph[selected][0][0] in self.graph[neighbor][0]:
                        self.graph[neighbor][0].remove(
                            self.graph[selected][0][0])
                    if not self.graph[neighbor][0]:
                        print(neighbor, "has empty domain by forward checking")
                        return False
                    if len(self.graph[neighbor][0]) == 1:
                        for x in self.graph[neighbor][1]:
                            if x not in self.visited:
                                if self.graph[neighbor][0][0] in self.graph[x][0]:
                                    self.graph[x][0].remove(
                                        self.graph[neighbor][0][0])
                                if not self.graph[x][0]:
                                    print(x, "has empty domain by ac3")
                                    return False
    
            # self.printGraph()
            return True    
        
        
                        


def main():
    snake()


if __name__ == '__main__':
    main()
