import argparse
import timeit
from src.environment import Environment
from src.algorithms import dfs
from src.helpers import *


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
    universe = Environment(initial_state, None, 0)
    print('Initial state of the Puzzle: ', universe.state)
    print('The agent is on index: ', findCero(initial_state))

    print('The AI is solving the puzzle...')
    
    if(isSolvable(universe.state)): 
        # Running Depth First Search algorithm
        dfs(universe)
        # '''
        # Results report

        # Todo: Path should contain the moves to get to the goal state
        print("path: ", moves)

        print("nodes expanded: ",str(NodesExpanded))
        print("search_depth: ",str(deep))
        print("MaxSearchDeep: ",str(MaxSearchDeep))
        print('The puzzle was solved in: ', time, ' seconds')
        print("running_time: ", format(time, '.8f'))
        # '''

    else:
        print("The puzzle is not solvable please try a different board setup")
    stop = timeit.default_timer()
    time = stop-start


  

if __name__ == '__main__':
    main()
