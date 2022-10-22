import argparse
import timeit
from src.environment import Environment
from src.algorithms import *
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
    universe = Environment(initial_state, None, 0, 0)
    print("\n")
    print("---------------------------------- START ----------------------------------")
    print('Initial state of the Puzzle: ', universe.state)
    print('The agent is on index: ', findCero(initial_state))

    print('The AI is solving the puzzle...')
    
    if(isSolvable(universe.state)): 
        # Running Depth First Search algorithm
        dfs(universe)
        # '''
        # Results report
        # Todo: Path should contain the moves to get to the goal state
        stop = timeit.default_timer()
        time = stop-start
        print("path: ", getMoves())
        print("nodes expanded: ",str(Environment.countNodes()))
        print("search_depth: ",str(getNodeDeep()))
        print("MaxSearchDeep: ",str(getMaxSearchDeep()))
        print('The puzzle was solved in: ', time, ' seconds')
        print("running_time: ", format(time, '.8f'))
        # '''

    else:
        print("\n")
        print("---------------------------------- RESULTS ----------------------------------")
        print("The puzzle is not solvable. Try with another puzzle.")


  

if __name__ == '__main__':
    main()
