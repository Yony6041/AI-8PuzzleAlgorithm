from src.helpers import move

"""
En el ambiente vamos a tener 2 cosas:
1. El entorno o bien el "mundo" en el que se encuentra el agente que en
nuestro caso es el tablero de 3x3

1. El entorno en el cual se encuentra el agente.
2. La variable agent_location,nos da la posicion del agente en el entorno.

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
    def __init__(self, state, parent, depth, agent_location):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.agent_location = agent_location
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

    def update_environment(self, action):
        if action == 'up':
            self.agent_location -= 3
        elif action == 'down':
            self.agent_location += 3
        elif action == 'left':
            self.agent_location -= 1
        elif action == 'right':
            self.agent_location += 1

    """
        Regresa True si el agente se encuentra en el estado final.

        Argumentos
        ---------
        agent_location : int
            El cuadro en el que se encuentra el agente
    """
    #The agent has accomplished the desired state ********************************
    def finished(self, agent_location):

        if self.state[agent_location] == 8:
            return True
        else:
            return False
        
    #Obtain Sub Nodes********************************************************
    def subNodes(node):

        global NodesExpanded
        NodesExpanded = NodesExpanded+1

        nextPaths = []
        nextPaths.append(Environment(move(node.state, 1), node, 1, node.depth + 1, 0))
        nextPaths.append(Environment(move(node.state, 2), node, 2, node.depth + 1, 0))
        nextPaths.append(Environment(move(node.state, 3), node, 3, node.depth + 1, 0))
        nextPaths.append(Environment(move(node.state, 4), node, 4, node.depth + 1, 0))
        nodes=[]
        for procPaths in nextPaths:
            if(procPaths.state!=None):
                nodes.append(procPaths)
        return nodes
