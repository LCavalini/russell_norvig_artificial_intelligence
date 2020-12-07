class Node:

  def __init__(self, state, parent = None, action = None, pathCost = 0):
    self.state = state
    self.parent = parent
    self.action = action
    self.pathCost = pathCost

class Problem:

    def __init__(self, initial, goal, stateSpace):
      self.initial = initial
      self.goal = goal
      self.stateSpace = stateSpace

    def result(self, state, action):
      return stateSpace[state][action][0]

    def actionCost(self, state, action):
      return stateSpace[state][action][1]

    def actions(self, state):
      return list(self.stateSpace[state].keys())

    def frontier(self, state):
      return self.stateSpace[state].keys()

    def isGoal(self, state):
      return self.goal == state

def evaluate(nodes):
  return sorted(nodes, key = lambda item : item.pathCost)
    
def breadthFirstSearch(problem):
  node = Node(state=problem.initial)

  if problem.isGoal(node.state):
    return node

  frontier = [node]
  reached = set()

  while len(frontier) > 0:
    node = frontier.pop(0)
    
    for child in expand(problem, node):
      s = child.state
  
      if problem.isGoal(s):
        return child

      if s not in reached:
        reached.add(s)
        frontier.append(child)

  return None
    
def expand(problem, node):
  s1 = node.state
   
  for action in problem.actions(s1):
    s2 = problem.result(s1, action)
    cost = node.pathCost + problem.actionCost(s1, action)
    yield Node(state = s2, parent = node, action = action, pathCost = cost)
    
  

stateSpace = {"Oradea": {"Zerind": ["Zerind", 71], "Sibiu": ["Sibiu", 151]},
              "Zerind": {"Arad": ["Arad", 75], "Oradea": ["Oradea", 71]},
               "Arad": {"Zerind": ["Zerind", 75], "Sibiu": ["Sibiu", 140],
                  "Timisoara": ["Timisoara", 118]},
              "Timisoara": {"Arad": ["Arad", 118], "Lugoj": ["Lugoj", 111]}, 
              "Sibiu": {"Arad": ["Arad", 140], "Oradea": ["Oradea", 151],
                  "Fagaras": ["Fagaras", 99], "Rimnicu Vilcea": ["Rimnicu Vilcea", 80]},
              "Fagaras": {"Sibiu": ["Sibiu", 99], "Bucharest": ["Bucharest", 211]},
              "Rimnicu Vilcea": {"Sibiu": ["Sibiu", 80], "Pitesti": ["Pitesti",
                  97], "Craiova": ["Craiova", 146]}, 
              "Lugoj": {"Timisoara": ["Timisoara", 111], "Mehadia": ["Mehadia", 70]},
              "Mehadia": {"Lugoj": ["Lugoj", 70], "Drobeta": ["Drobeta", 75]},
              "Drobeta": {"Mehadia": ["Mehadia", 75], "Craiova": ["Craiova", 120]},
              "Craiova": {"Drobeta": ["Drobeta", 120], "Rimnicu Vilcea":
                  ["Rimnicu Vilcea", 146], "Pitesti": ["Pitesti", 138]},
              "Pitesti": {"Rimnicu Vilcea": ["Rimnicu Vilcea", 97], "Craiova":
                  ["Craiova", 138], "Bucharest": ["Bucharest", 101]}, 
              "Bucharest": {"Pitesti": ["Pitesti", 101], "Giurgiu": ["Giurgiu",
                  90], "Urziceni": ["Urziceni", 85], "Fagaras": ["Fagaras", 211]},
              "Giurgiu": {"Bucharest": ["Bucharest", 90]},
              "Urziceni": {"Bucharest": ["Bucharest", 85], "Hirsova":
                  ["Hirsova", 98], "Vaslui": ["Vaslui", 142]},
              "Hirsova": {"Urziceni": ["Urziceni", 98], "Eforie": ["Eforie",
                  86]},
              "Eforie": {"Hirsova": ["Hirsova", 86]},
              "Vaslui": {"Urziceni": ["Urziceni", 142], "Iasi": ["Iasi", 92]},
              "Iasi": {"Vaslui": ["Vaslui", 92], "Neamt": ["Neamt", 87]},
              "Neamt": {"Iasi": ["Iasi", 87]} }

problem = Problem("Arad", "Bucharest", stateSpace)

result = breadthFirstSearch(problem)
path = list()

if result == None:
  print("Não foi possível chegar ao destino!")
else:
  node = result
  path.append("Bucharest")
  while node.parent != None:
    node = node.parent
    path.append(node.state)

print(path[::-1])
