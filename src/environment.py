from src.helpers import *

"""
En el ambiente vamos a tener el entorno o bien el "mundo" en el que se encuentra el agente que en
nuestro caso es el tablero de 3x3


    Nuestro estado inicial es el siguiente:

    [1,0,2]
    [6,3,4]
    [7,5,8]

    El estado final es el siguiente:

    [1,2,3]
    [4,5,6]
    [7,8,0]
"""


class Environment():
    
    # Environment constructor ***********************************************
    def __init__(self, state, parent, depth):
        self.state = state
        self.parent = parent
        self.depth = depth
        if self.state:
            self.map = ''.join(str(e) for e in self.state)
    def __eq__(self, other):
        return self.map == other.map
    def __lt__(self, other):
        return self.map < other.map
    def __str__(self):
        return str(self.map)  

    """
        Actualiza el ambiente dependiendo de la accion que tomo el a gente.

        Argumentos
        ---------
        action : str
            La accion que tomo el agente
    """
            
    def move(self, direction: int):
        move(self.state, direction)
# Obtain Sub Nodes********************************************************
    def subNodes(node, state, parent, depth):

        global NodesExpanded
        NodesExpanded = NodesExpanded+1
        Environment.countNodes()

        print("NodesExpanded:", NodesExpanded)
        nextPaths = []
        nextPaths.append(Environment(move(state, 1), parent, depth + 1))
        nextPaths.append(Environment(move(state, 2), parent, depth + 1))
        nextPaths.append(Environment(move(state, 3), parent, depth + 1))
        nextPaths.append(Environment(move(state, 4), parent, depth + 1))
        nodes=[]
        for procPaths in nextPaths:
            if(procPaths.state!=None):
                nodes.append(procPaths)
        return nodes

# Obtain Nodes Expand Counter*********************************************

    countNodes = 0

    def countNodes():
        countNodes = NodesExpanded
        return countNodes