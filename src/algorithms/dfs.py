#BFS**************************************************************
def bfs(startState):

    global MaxFrontier, GoalNode, MaxSearchDeep

    boardVisited= set()
    Queue = deque([PuzzleState(startState, None, None, 0, 0, 0)])

    while Queue:
        node = Queue.popleft()
        boardVisited.add(node.map)
        if node.state == GoalState:
            GoalNode = node
            return Queue
        posiblePaths = subNodes(node)
        for path in posiblePaths:
            if path.map not in boardVisited:
                Queue.append(path)
                boardVisited.add(path.map)
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = MaxSearchDeep + 1
        if len(Queue) > MaxFrontier:
            QueueSize = len(Queue)
            MaxFrontier = QueueSize