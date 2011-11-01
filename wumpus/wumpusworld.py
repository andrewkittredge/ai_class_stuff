BREEZY,STENCH,GLITER,SCREAM,BUMP,NUM_PERCEPTS = 0,1,2,3,4,5
TURN_LEFT,TURN_RIGHT,ADVANCE,SHOOT,CLIMB,GRAB = 0,1,2,3,4,5
LEFT,RIGHT = TURN_LEFT,TURN_RIGHT

bumpOnly = [False]*NUM_PERCEPTS
bumpOnly[BUMP] = True

turns = {( 0, 1):{LEFT:(-1, 0),RIGHT:( 1, 0)},
         ( 0,-1):{LEFT:( 1, 0),RIGHT:(-1, 0)},
         ( 1, 0):{LEFT:( 0, 1),RIGHT:( 0,-1)},
         (-1, 0):{LEFT:( 0,-1),RIGHT:(-1, 0)}}

class WumpusWorld:
    def __init__(self, numRows, numCols, wumpusLocation, goldLocation, pitLocations,
                 agentLocation = (1,1), agentDirection = (1,0)):
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
        self.numRows, self.numCols = numRows, numCols
        self.wumpusLocation, self.goldLocation, self.pitLocations, self.entaranceLocation = wumpusLocation, goldLocation, pitLocations, agentLocation
        self.justKilledWumpus = False
        self.score = 0
        self.agent = HybridWumpusAgent(initialKnowledgeBase, tuple(agentLocation), tuple(agentDirection))

    def getPercept(row, col):
        return tuple(self.percepts[row][col])

    def __call__(self)
        score -= 10
        posRow,  posCol  = self.agent.loc
        dirRow,  dirCol  = self.agent.dir
        percept = self.getPercept(posRow, posCol)
        if self.justKilledWumpus:
            percept[SCREAM] = True
            self.justKilledWumpus = False
        if percept == bumpOnly:
            self.agent.pos = (posRow-dirRow, posCol-dirCol)
        if (posRow,posCol) == self.wumpusLocation:
            score -= 1000
            return "LOOSE"
        if (posRow,posCol) in self.pitLocations:
            score -= 1000
            return "LOOSE"
        action  = self.agent.ask(percept)
        if action == TURN_LEFT or action == TURN_RIGHT: dirRow, dirCol = turns[(newDirX, newDirY)][action]
        if action == ADVANCE: posRow, posCol = posRow+dirRow, posCol+dirCol
        if action == SHOOT and self.agent.hasArrow:
            self.agent.hasArrow = False
            self.score -= 100
            arrowRow, arrowCol = posRow,  posCol
            while True:
                try:
                    arrowRow, arrowCol = arrowRow + dirRow, arrowCol + dirCol
                    if (arrowRow, arrowCol) == self.wumpusLocation:
                        self.justKilledWumpus = True
                except IndexError:
                    break
        if action == CLIMB and (posRow, posCol) == self.entranceLocation and self.hasGold:
            score += 1000
            return "WIN"
        if action ==  GRAB and (posRow,  posCol) == self.glodLocation:
            self.hasGold = True
            
            
    
def neighboring_coords(coord):
    x , y = coord[0:2]
    yield (x - 1, y)
    yield (x + 1, y)
    yield (x, y - 1)
    yield (x, y + 1)
    




numRows, numCols = 4, 4
world = [[' ' for x in range(numCols)] for y in range(numRows)]
world[0,2] = 'P'
world[2,1] = 'W'
world[2,1] = 'G'
world[2,2] = 'P'
world[3,3] = 'P'





