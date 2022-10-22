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
    print("---------------------------------- Comienzo ----------------------------------")
    print('Estado inicial 8-Puzzle: ', universe.state)
    print('El agente esta en el indice ', findCero(initial_state))

    print('La IA esta resolviendo el puzzle...')
    
    if(isSolvable(universe.state)): 
        # Running Depth First Search algorithm
        dfs(universe)
        # '''
        # Results report
        # Todo: Path should contain the moves to get to the goal state
        stop = timeit.default_timer()
        time = stop-start
        print("Movimientos a seguir: ", getMoves())
        print("Nodos expandidos: ",str(Environment.countNodes()))
        print("Profundidad Nodo: ",str(getNodeDeep()))
        print("Maximo Nodo Profundo: ",str(getMaxSearchDeep()))
        print('El 8-puzzle se resolvio en: ', time, ' segundos')
        print("running_time: ", format(time, '.8f'))
        # '''

    else:
        print("\n")
        print("---------------------------------- RESULTADOS ----------------------------------")
        print("El puzzle no tiene solucion. Intenta con otro puzzle.")


  

if __name__ == '__main__':
    main()
