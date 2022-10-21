import argparse
import timeit
from src.helpers import setInitialBoard, findCero
from src.environment import Environment
from src.algorithms import dfs

global GoalState, GoalNode, NodesExpanded, MaxSearchDeep, MaxFrontier    
GoalNode = None  # at finding solution
GoalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
NodesExpanded= 0  # total nodes visited
MaxSearchDeep= 0  # max deep
MaxFrontier= 0  # max frontier


def main():
    
    global startState, GoalState, MaxFrontier, GoalNode, MaxSearchDeep, subNodes

    parser = argparse.ArgumentParser()
    parser.add_argument('initial_state', type=str,
                        help='Initial state of the puzzle')
    args = parser.parse_args()
    data = args.initial_state.split(',')

    # Start operations
    start = timeit.default_timer()



    # Build initial board state
    initial_state = setInitialBoard(data)

    # Inicializa el ambiente
    universe = Environment(initial_state, None, 0, findCero(initial_state))
    print('Initial state of the Puzzle: ', universe.state)
    print('The agent is on index: ', findCero(initial_state))

    print('The AI is solving the puzzle...')
    
    # Running Depth First Search algorithm
    dfs(universe)

    stop = timeit.default_timer()
    time = stop-start

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

    # '''
    # Results report
    print("path: ",moves)
    print("nodes expanded: ",str(NodesExpanded))
    print("search_depth: ",str(deep))
    print("MaxSearchDeep: ",str(MaxSearchDeep))
    print("running_time: ", format(time, '.8f'))
    # '''


if __name__ == '__main__':
    main()
