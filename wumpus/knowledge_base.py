'''
Created on Nov 1, 2011

@author: andrewkittredge
'''
from wumpusworld import BREEZY, STENCH, neighboring_coords
 
from exceptions import NotImplementedError

class KnowledgeBase(object):
    def __init__(self, world):
        self.knowledge = {}
        
    def ask_ok(self, ok_coord, time):
        for coord in neighboring_coords(ok_coord):
            for t in range(t):
                percept = (coord, time)
                previous_percept = self.knowledge.get(percept, None)
                safe = (previous_percept and STENCH not in previous_percept and BREEZY not in previous_percept)
                if safe:
                    return True
        return False
            
    def ask_not_ok(self, not_ok_coord, time):
        
    def ask_visited(self, coord, t):
        return (coord, t) in self.knowledge
    
    
    def tell_percept(self, percept, coord, time):
        self.knowledge[(coord, time)] = percept
    def tell_action(self, action, t):
        raise NotImplementedError