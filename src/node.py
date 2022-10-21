class Node(object):

  def _init_(self):
    self.state = 0
    self.parent = None
    self.action = None
    self.depth = 0
    
# Función para expandir cada nodo según la estructura del problema de búsqueda.
  def expand(problem, node):
    """
    Función para expandir los nodos dado el problema.
    
    Argumentos
    ---------
    problem : objeto
        Problema de búsqueda.
    node : objeto
        Nodo que se va a expandir.
        
    Salida
    ------
    childs :generator
        Generador con los hijos del nodo.
    """
    #Nodo en el que se inicia
    s = node.state

    for action in problem.actions(s):
      #Ejecuta la acción
      new_s = problem.act(s, action)

      #Genera un nuevo nodo
      new_node = Node()
      new_node.state = new_s
      new_node.parent = node
      new_node.action = action
      new_node.depth = node.depth + 1

      yield new_node

      
  # Algoritmo de Depth-First-Search para un problema de búsqueda.
  def dfs (problem):
    #Almacenamiento de nodos
    nodes = []
    #Nodo inicial
    node = Node()
    node.state = problem.initial
    #Frontera con cola de prioridad
    frontier = PriorityQueue()
    frontier.push(node)
    #Nodos alcanzados
    reached = {problem.initial:node}

    #Mientras la frontera no esté vacía
    while frontier.isEmpty() == False:
        #Pop en frontera
        node = frontier.pop()
        #Guarda el nodo en la lista
        nodes.append(node)
        #Si llega a un nodo final se detiene 
        #y regresa el camino de nodos
        if node.state in problem.goal:
            return nodes
        #Expande el nodo actual
        for child in expand(problem, node):
            #Guarda estado de los hijos
            state = child.state
          #Falta
          
          
    #Si no logra llegar a un nodo final
    #El algoritmo regresa mensaje de error
    return "No se ha logrado llegar a un estado final."
