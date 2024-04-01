



class Node:
    def __init__(self, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.up = None
        self.down = None
        self.label = None


class Agent:
    def __init__(self, initialNode):
        self.currentNode = initialNode
        self.goalFound = False




class Wall:
    def __init__(self, initialNode):
        self.currentNode = initialNode
       


class Goal:
    def __init__(self, initialNode):
        self.currentNode = initialNode




class GridWorld:
    def __init__(self, rows, columns, agentPosition, goalPosition):
        self.rows = rows
        self.columns = columns
        self.agent = None
        self.goal = None
        self.grid = self.createGrid(agentPosition, goalPosition)



    def createGrid(self, agentPosition , goalPosition):
        grid = [[Node() for _ in range(self.columns)]for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.columns):
                if i > 0:
                    grid[i][j].up = grid[i - 1][j]
                if i < self.rows - 1:
                    grid[i][j].down = grid[i + 1][j]
                if j > 0:
                    grid[i][j].prev = grid[i][j - 1]
                if j < self.columns - 1:
                    grid[i][j].next = grid[i][j + 1]

        agentX, agentY = agentPosition
        goalX, goalY = goalPosition
        goalPos = grid[goalX][goalY]
        agentPos = grid[agentX][agentY]
        self.agent = Agent(agentPos)
        self.goal = Goal(goalPos)
        return grid





    def displayGrid(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j] == self.agent.currentNode:
                    print("--[X]--",end="|")
                elif self.grid[i][j] == self.goal.currentNode:
                    print("--[G]--",end="|")

                else:
                    print("--[-]--", end="|")
            print("\n" + '-' *(self.columns * 8-1))




if __name__ == "__main__":
    rows, columns = 5, 5
    goalPosition = (4,4)
    agentPosition = (2,2)
    grid = GridWorld(rows,columns, agentPosition ,goalPosition)
    grid.displayGrid()
                    



            



















            
