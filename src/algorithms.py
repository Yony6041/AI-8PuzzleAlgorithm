from collections import deque
from src.environment import Environment

global GoalState, GoalNode, MaxSearchDeep, MaxFrontier
GoalNode = None  # at finding solution
GoalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
MaxSearchDeep= 0  # max deep
MaxFrontier= 0  # max frontier



# Depth First Search *****************************************************
def dfs(environment):
    global GoalState, GoalNode, MaxSearchDeep, MaxFrontier, initial_state
    boardVisited = set()
    stack = list([environment])
    
    initial_state = environment.state
    while stack:
        global GoalState
        node = stack.pop()
        boardVisited.add(node.map)
        print("What we want:", GoalState)
        print("What we have:", node.state)
        if node.state == GoalState:
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
    
