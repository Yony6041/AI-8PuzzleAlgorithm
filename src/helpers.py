# Sets initial board ****************************************************
def setInitialBoard(data: [str]):
    board = []
    for i in range(0, 9):
        board.append(int(data[i]))
    return board

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


"""
    Regresa una lista con las posibles acciones que puede tomar el agente
    dependiendo de la posicion en la que se encuentre y el estado del tablero.
    Argumentos
    ---------
    agent_location : int
        El cuadro en el que se encuentra el agente
"""
def class_possible_actions(agent_location: int):

    possible_actions = ['up', 'down', 'left', 'right']

    if agent_location[0] == 0:
        return [(1, 'left', 0), (3, 'up', 0)]
    elif agent_location[1] == 0:
        return [(0, 'right', 1), (2, 'left', 1), (4, 'up', 1)]
    elif agent_location[2] == 0:
        return [(1, 'right', 2), (5, 'up', 2)]
    elif agent_location[3] == 0:
        return [(0, 'down', 3), (4, 'left', 3), (6, 'up', 3)]
    elif agent_location[4] == 0:
        return [(1, 'down', 4), (3, 'right', 4), (5, 'left', 4), (7, 'up', 4)]
    elif agent_location[5] == 0:
        return [(2, 'down', 5), (4, 'right', 5), (8, 'up', 5)]
    elif agent_location[6] == 0:
        return [(3, 'down', 6), (7, 'left', 6)]
    elif agent_location[7] == 0:
        return [(4, 'down', 7), (6, 'right', 7), (8, 'left', 7)]
    else:
        return [(5, 'down', 8), (7, 'right', 8)]

def findCero(state: [int]):
    for i in range(len(state)):
        if state[i] == 0:
            return i
