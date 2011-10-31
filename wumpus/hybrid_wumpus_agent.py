'''
Created on Oct 30, 2011

@author: andrewkittredge
'''

from percept import make_percept_sentence

class Hybrid_Wumpus_Agent(object):
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.time = 0
        
    def __action__(self, percept):
        self.knowledge_base.tell(make_percept_sentence(percept, self.time))
        safe = self.knowledge_base.ask('ok x, y time = t')
        if self.knowledge_base.ask('glitter time=t'):
            plan = ['grab'] + plan_route(current, {[1, 1]}, safe) + ['climb']
        if not plan:
            unvisited = set()
            for coord in world.all_coords:
                if not any(self.knowledge_base.ask(coord, t) for t in range(self.time)):
                    unvisited.add(coord)
            plan = ?.plan_route(current, unvisited + safe, safe)
        if not plan and self.knowledge_base('Have Arrow', self.time):
            possible_wumpus = (coord for coord in world.all_cords if not self.knowledge_base.ask('not wumpus'))
            plan = ?.plan_shot(current, possible_wumpus, safe)
        if not plan: #take a risk
            not_unsafe = (coord for coord in world.all_coords if not self.knowledge_base.ask('not ok coord', t))
            plan = ?.plan_route(current, unvisited + not_unsafe, safe)
        if not plan:
            plan = ?.plan_route(current, {[1, 1]}, safe) + ['climb']
        action = plan.pop()
        self.knowledge_base.tell(?.make_action_sentence(action, t))
        self.time += 1
        return action
            