import pattern  # Path: src/helpers/pattern.py
import nup


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

    def __init__(self, puzzle):
        self.puzzle = puzzle

        """
        Regresa una lista con las posibles acciones que puede tomar el agente
        dependiendo de la posicion en la que se encuentre y el estado del tablero.

        Argumentos
        ---------
        agent_location : int
            El cuadro en el que se encuentra el agente
        """

    def possible_actions(self, agent_location):

        possible_actions = ['up', 'down', 'left', 'right']

        def switch(agent_location):

            if agent_location in [6, 7, 8]:
                possible_actions.remove('up')
            if agent_location in [6, 7, 8]:
                possible_actions.remove('down')
            if agent_location in [0, 3, 6]:
                possible_actions.remove('left')
            if agent_location in [2, 5, 8]:
                possible_actions.remove('right')
            return possible_actions

    def update_environment(self, action):
        """
        Actualiza el ambiente dependiendo de la accion que tomo el a gente.

        Argumentos
        ---------
        action : str
            La accion que tomo el agente
        """
        if action == 'up':
            self.agent_location -= 3
        elif action == 'down':
            self.agent_location += 3
        elif action == 'left':
            self.agent_location -= 1
        elif action == 'right':
            self.agent_location += 1
            
            
    def return_reward(self, agent_location):
        """
        Regresa la recompensa que obtuvo el agente dependiendo de la posicion
        en la que se encuentra.

        Argumentos
        ---------
        agent_location : int
            El cuadro en el que se encuentra el agente
        """
        if self.puzzle[agent_location] == 0:
            return 10
        else:
            return -1
    def is_finished(self, agent_location):
        """
        Regresa True si el agente se encuentra en el estado final.

        Argumentos
        ---------
        agent_location : int
            El cuadro en el que se encuentra el agente
        """
        if self.puzzle[agent_location] == 0:
            return True
        else:
            return False