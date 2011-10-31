
BREEZY,STENCH,GLITER,SCREAM,BUMP,NUM_PERCEPTS = 0,1,2,3,4,5
TURN_LEFT,TURN_RIGHT,ADVANCE,SHOOT = 0,1,2,3
LEFT,RIGHT = 0,1
bumpOnly = [False]*NUM_PERCEPTS
bumpOnly[BUMP] = True

turns = {( 0, 1):{LEFT:(),RIGHT:()},
         ( 0,-1):{LEFT:(),RIGHT:()},
         ( 1, 0):{LEFT:(),RIGHT:()},
         (-1, 0):{LEFT:(),RIGHT:()},}

class WumpusWorld:
    def __init__(self, numRows, numCols, wumpusLocation, goldLocation, pitLocations,
                 agentLocation = (0,0), agentDirection = (1,0)):
        self.percepts = [[[False]*NUM_PERCEPTS for x in range(numCols+2)] for y in range(numRows+2)]
        for percept,(row,col) in zip([STENCH        ] + [BREEZY]*len(pitLocations),
                                     [wumpusLocation] + list(pitLocations)):
            self.percepts[row+1][col][percept] = True
            self.percepts[row-1][col][percept] = True
            self.percepts[row][col+1][percept] = True
            self.percepts[row][col-1][percept] = True
        percept, (row,col) = GLITER, goldLocation
        self.percepts[row][col][percept] = True
        for (row,col) in sum([((row,0),(row,-1)) for row in range(numRows+2)] +
                             [((0,col),(-1,col)) for col in range(numCols+2)]):
            self.percepts[row][col-1] = bumpOnly
        self.agent = Agent(tuple(agentLocation), tuple(agentDirection),
                           self.getPercept(*agentLocation), 0, 0)
        self.time  = 0
        self.score = 0

    def getPercept(row, col):
        return tuple(self.percepts[row][col])

    def __call__(self)
        time  += 1
        score -= 10
        action = self.agent.ask()
        newRow,  newCol  = self.agent.location
        newDirX, newDirY = self.agent.agentDirection
        percept = self.getPercept(newRow, newCol)
        if action == TURN_LEFT:  newDirX, newDirY = turns[(newDirX, newDirY)][LEFT]
        if action == TURN_RIGHT: newDirX, newDirY = turns[(newDirX, newDirY)][RIGHT]
        if action == ADVANCE:
            newRow, newCol, percept = newRow+newDirX, newCol+newDirY, self.getPercept(newRow,newCol)
        if newRow == 0 or newCol == 0 or newRow == self.numRows-1 or newCol == self.numCols-1:
            newRow, newCol, percept = newRow - newDirX, newCol - newDirY, bumpOnly
        if action == SHOOT:
        if action == GRAB: 
    
def getPercept(world, (row, col)):
    current = world[row][col]
    neighbors = 



numRows, numCols = 4, 4
world = [[' ' for x in range(numCols)] for y in range(numRows)]
world[0,2] = 'P'
world[2,1] = 'W'
world[2,1] = 'G'
world[2,2] = 'P'
world[3,3] = 'P'





