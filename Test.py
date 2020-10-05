from automaton import *

class Enemy(Automaton):
    """
    this Enemy class can be defined as the following rst table:
    ========  ======  =============
    Source    Dest    Event
    ========  ======  =============
    attack    Aid     healthLow
    attack    wander  playerNotNear
    Aid       wander  healthFull
    wander    attack  playerNear
    ========  ======  =============
    """
    playerNear = Event("wander","attack")
    playerNotNear = Event("attack","wander")
    healthLow = Event("attack","Aid")
    healthFull = Event("Aid","wander")
terry = Enemy(initial_state="wander")
assert terry.state == "wander"
terry.event("playerNear")
terry.event("healthLow")
print(terry.state)


#print(stategraph(Enemy, fmt='plantuml'))