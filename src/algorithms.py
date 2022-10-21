from collections import deque
from src.environment import Environment
from src.helpers import *


# Depth First Search *****************************************************
def dfs(environment):
    global GoalState, GoalNode, MaxSearchDeep, MaxFrontier, initial_state
    boardVisited = set()
    stack = list([environment])
    initial_state = environment.state
    while stack:
        node = stack.pop()
        boardVisited.add(node.map)
        print("What we want:", GoalState)
        print("What we have:", node.state)
        if node.state == GoalState:
            print("\n")
            print("---------------------------------- RESULTS ----------------------------------")
            print("We got the right answer!")
            GoalNode = node
            return stack
        #inverse the order of next paths for execution porpuses
        print("node:", node.depth)
        posiblePaths = reversed(environment.subNodes(node.state, node, node.depth))
        for path in posiblePaths:
            if path.map not in boardVisited:
                stack.append(path)
                boardVisited.add(path.map)
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = 1 + MaxSearchDeep
        if len(stack) > MaxFrontier:
            
            MaxFrontier = len(stack)
            
    # Path result
    print("We got the wrong answer!")
    
    while initial_state != GoalNode.state:
        if GoalNode.move == 1:
            path = 'Up'
        if GoalNode.move == 2:
            path = 'Down'
        if GoalNode.move == 3:
            path = 'Left'
        if GoalNode.move == 4:
            path = 'Right'
        moves.insert(0, path)
        GoalNode = GoalNode.parent

# Return Goal Node Depth*****************************************************
def getNodeDeep():
    return GoalNode.depth

# Return the Deepest Node Explored*******************************************
def getMaxSearchDeep():
    return MaxSearchDeep
    
