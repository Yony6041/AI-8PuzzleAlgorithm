global GoalState, GoalNode, MaxSearchDeep, MaxFrontier, moves, NodesExpanded, deep
GoalNode = None  # at finding solution
GoalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
MaxSearchDeep= 0  # max deep
MaxFrontier= 0  # max frontier
moves = []
NodesExpanded= 0  # total nodes visited= 0  # total nodes visited
deep = 0  # deep

# Sets initial board ****************************************************
def setInitialBoard(data: [str]):
    board = []
    for i in range(0, 9):
        board.append(int(data[i]))
    return board


"""
    Regresa una lista con las posibles acciones que puede tomar el agente
    dependiendo de la posicion en la que se encuentre y el estado del tablero.
    Argumentos
    ---------
    state : int
    direction : int
        El cuadro en el que se encuentra el agente
"""
# Move agent on board**************************************************************


def move(state: [int], direction: int):
    # generate a copy
    newState = state[:]

    # obtain poss of 0
    index = newState.index(0)

    if (index == 0):
        if (direction == 1):
            return None
        if (direction == 2):
            temp = newState[0]
            newState[0] = newState[3]
            newState[3] = temp
        if (direction == 3):
            return None
        if (direction == 4):
            temp = newState[0]
            newState[0] = newState[1]
            newState[1] = temp
        return newState
    if (index == 1):
        if (direction == 1):
            return None
        if (direction == 2):
            temp = newState[1]
            newState[1] = newState[4]
            newState[4] = temp
        if (direction == 3):
            temp = newState[1]
            newState[1] = newState[0]
            newState[0] = temp
        if (direction == 4):
            temp = newState[1]
            newState[1] = newState[2]
            newState[2] = temp
        return newState
    if (index == 2):
        if (direction == 1):
            return None
        if (direction == 2):
            temp = newState[2]
            newState[2] = newState[5]
            newState[5] = temp
        if (direction == 3):
            temp = newState[2]
            newState[2] = newState[1]
            newState[1] = temp
        if (direction == 4):
            return None
        return newState
    if (index == 3):
        if (direction == 1):
            temp = newState[3]
            newState[3] = newState[0]
            newState[0] = temp
        if (direction == 2):
            temp = newState[3]
            newState[3] = newState[6]
            newState[6] = temp
        if (direction == 3):
            return None
        if (direction == 4):
            temp = newState[3]
            newState[3] = newState[4]
            newState[4] = temp
        return newState
    if (index == 4):
        if (direction == 1):
            temp = newState[4]
            newState[4] = newState[1]
            newState[1] = temp
        if (direction == 2):
            temp = newState[4]
            newState[4] = newState[7]
            newState[7] = temp
        if (direction == 3):
            temp = newState[4]
            newState[4] = newState[3]
            newState[3] = temp
        if (direction == 4):
            temp = newState[4]
            newState[4] = newState[5]
            newState[5] = temp
        return newState
    if (index == 5):
        if (direction == 1):
            temp = newState[5]
            newState[5] = newState[2]
            newState[2] = temp
        if (direction == 2):
            temp = newState[5]
            newState[5] = newState[8]
            newState[8] = temp
        if (direction == 3):
            temp = newState[5]
            newState[5] = newState[4]
            newState[4] = temp
        if (direction == 4):
            return None
        return newState
    if (index == 6):
        if (direction == 1):
            temp = newState[6]
            newState[6] = newState[3]
            newState[3] = temp
        if (direction == 2):
            return None
        if (direction == 3):
            return None
        if (direction == 4):
            temp = newState[6]
            newState[6] = newState[7]
            newState[7] = temp
        return newState
    if (index == 7):
        if (direction == 1):
            temp = newState[7]
            newState[7] = newState[4]
            newState[4] = temp
        if (direction == 2):
            return None
        if (direction == 3):
            temp = newState[7]
            newState[7] = newState[6]
            newState[6] = temp
        if (direction == 4):
            temp = newState[7]
            newState[7] = newState[8]
            newState[8] = temp
        return newState
    if (index == 8):
        if (direction == 1):
            temp = newState[8]
            newState[8] = newState[5]
            newState[5] = temp
        if (direction == 2):
            return None
        if (direction == 3):
            temp = newState[8]
            newState[8] = newState[7]
            newState[7] = temp
        if (direction == 4):
            return None
        return newState

def findCero(state: [int]):
    for i in range(len(state)):
        if state[i] == 0:
            return i

# Python3 program to check if a given
# instance of 8 puzzle is solvable or not

# A utility function to count
# inversions in given array 'arr[]'


def getInvCount(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count


# This function returns true
# if given 8 puzzle is solvable.
def isSolvable(puzzle: [int]):
    
    puzzle = transformToArray(puzzle)

    # Count inversions in given 8 puzzle
    inv_count = getInvCount([j for sub in puzzle for j in sub])

    # return true if inversion count is even.
    return (inv_count % 2 == 0)


def transformToArray(state: [int]):
    return [[state[0], state[1], state[2]],
            [state[3], state[4], state[5]],
            [state[6], state[7], state[8]]]
