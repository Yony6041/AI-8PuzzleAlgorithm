from collections import deque
from src.environment import Environment

#Depth First Search *****************************************************
def dfs(environment: Environment):

    global startState, GoalState, MaxFrontier,GoalNode, MaxSearchDeep, subNodes
    boardVisited = set()
    stack = list([environment])
    while stack:
        node = stack.pop()
        boardVisited.add(node.map)
        if node.state == GoalState:
            GoalNode = node
            return stack
        #inverse the order of next paths for execution porpuses
        posiblePaths = reversed(environment.subNodes(node))
        for path in posiblePaths:
            if path.map not in boardVisited:
                stack.append(path)
                boardVisited.add(path.map)
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = 1 + MaxSearchDeep
        if len(stack) > MaxFrontier:
            MaxFrontier = len(stack)
    
