import argparse
import timeit
from src.helpers import setInitialBoard, findCero
from src.environment import Environment
from src.algorithms import dfs



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
