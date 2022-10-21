import numpy as np
"""
Construye el agente. 
Este necesita recordad las acciones que tomo y las recompensas que obtuvo
asi como el estado actual y lugares por los que paso.
"""


class Agent():
    def __init__(self, square, environment=None, debug=False):

        self.square = square
        self.environment = environment

        self.observations = []
        self.actions = []
        self.rewards = []
        self.debug = debug

    def take_step(self):
        """
        Toma un paso en el ambiente.
        """
        if (self.debug):
            print(f'Initial Position: {self.square}')

        self.observations.append(
            [self.square, self.environment.puzzle[self.square]])

        possible_actions = self.environment.possible_actions(self.square)

        if (self.debug):
            print(f'Possible actions: {possible_actions}')

        # Agente toma una accion aleatoria
        action = np.random.choice(possible_actions)

        if (self.debug):
            print(f'Action: {action}')

        self.environment.update_environment(action, self.square)

        if (self.debug):
            print(f'Current position: {self.square}')
            
        reward = (self.environment.return_reward(action))
        
            
        if (self.debug):
            print(f'Reward: {self.reward}')
        
        self.actions.append(action)
        self.reward.append(reward)
        
        if (self.debug):
            print(f'Total reward: {np.array(self.rewards).sum()}')
            
            
        if (self.debug):
            print(f'Environment state: {self.environment.puzzle}')
        pass

