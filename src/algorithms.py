from collections import deque
from src.environment import Environment

global GoalState, GoalNode, NodesExpanded, MaxSearchDeep, MaxFrontier
GoalNode = None  # at finding solution
GoalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
NodesExpanded= 0  # total nodes visited
MaxSearchDeep= 0  # max deep
MaxFrontier= 0  # max frontier


# Depth First Search *****************************************************
def dfs(environment: Environment):
    global GoalState, GoalNode, NodesExpanded, MaxSearchDeep, MaxFrontier
    boardVisited = set()
    stack = list([environment])
    while stack:
        global GoalState
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
            
    # Save total path result
    deep= GoalNode.depth
    moves = []
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
    
