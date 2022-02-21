class Graph:
    
    # init class
    def _init_(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    # create undirected graph by adding symmetric edges
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist

    # add link from A and B of given distance, and also add the inverse link if the graph is undirected
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance

    # get neighbors or a neighbor
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    # return list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

class Node:

    # init class
    def _init_(self, name, parent):
        self.name = name
        self.parent = parent
        self.g = 0 # distance to start node
        self.h = 0 # distance to goal node
        self.f = 0 # total cost

    # compare nodes
    def _eq_(self, other):
        return self.name == other.name

    # sort nodes
    def _lt_(self, other):
         return self.f < other.f

    # print node
    def _repr_(self):
        return ('({0},{1})'.format(self.name, self.f))



def astar_search(graph, heuristics, start, end):
    
    # lists for open nodes and closed nodes
    open = []
    closed = []

    # a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)

    # add start node
    open.append(start_node)
    
    # loop until the open list is empty
    while len(open) > 0:

       
        open.sort()                                 # sort open list to get the node with the lowest cost first
        current_node = open.pop(0)                  # get node with the lowest cost
        closed.append(current_node)                 # add current node to the closed list
        
        # check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
            path.append(start_node.name + ': ' + str(start_node.g))
            return path[::-1]

        
        neighbors = graph.get(current_node.name)    # get neighbours
        
        # loop neighbors
        for key, value in neighbors.items():
            neighbor = Node(key, current_node)      # create neighbor node
            if(neighbor in closed):                 # check if the neighbor is in the closed list
                continue

            # calculate full path cost
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h

            # check if neighbor is in open list and if it has a lower f value
            if(add_to_open(open, neighbor) == True):

                # everything is green, add neighbor to open list
                open.append(neighbor)

    # return None, no path is found
    return None
    
    
# check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True


# create a graph
graph = Graph() # user-based input for edges will be updated in the upcoming days
# create graph connections (Actual distance)
graph.connect('Oradea', 'Zerind', 71)
graph.connect('Oradea', 'Sibiu', 151)
graph.connect('Zerind', 'Arad', 75)
graph.connect('Arad', 'Sibiu', 140)
graph.connect('Arad', 'Timisoara', 118)
graph.connect('Sibiu', 'Fagaras', 99)
graph.connect('Sibiu', 'Rimnicu Vilcea', 80)
graph.connect('Rimnicu Vilcea', 'Craiova', 146)
graph.connect('Rimnicu Vilcea', 'Pitesti', 97)
graph.connect('Craiova', 'Pitesti', 138)
graph.connect('Fagaras', 'Bucharest', 211)
graph.connect('Pitesti', 'Bucharest', 101)
graph.connect('Timisoara', 'Lugoj', 111)
graph.connect('Lugoj', 'Mehadia', 70)
graph.connect('Mehadia', 'Dobreta', 75)
graph.connect('Dobreta', 'Craiova', 120)
graph.connect('Bucharest', 'Giurgiu', 90)
graph.connect('Bucharest', 'Urziceni', 85)
graph.connect('Urziceni', 'Hirsova', 98)
graph.connect('Hirsova', 'Eforie', 86)
graph.connect('Urziceni', 'Vaslui', 142)
graph.connect('Vaslui', 'lasi', 92)
graph.connect('lasi', 'Neamt', 87)
# make graph undirected, create symmetric connections
graph.make_undirected()
# create heuristics (straight-line distance, air-travel distance)
heuristics = {}
heuristics['Arad'] = 366
heuristics['Bucharest'] = 0
heuristics['Craiova'] = 160
heuristics['Dobreta'] = 242
heuristics['Eforie'] = 161
heuristics['Fagaras'] = 178
heuristics['Giurgiu'] = 77
heuristics['Hirsova'] = 151
heuristics['lasi'] = 226
heuristics['Lugoj'] = 244
heuristics['Mehadia'] = 241
heuristics['Neamt'] = 234
heuristics['Oradea'] = 380
heuristics['Pitesti'] = 98
heuristics['Rimnicu Vilcea'] = 193
heuristics['Sibiu'] = 253
heuristics['Timisoara'] = 329
heuristics['Urziceni'] = 80
heuristics['Vaslui'] = 199
heuristics['Zerind'] = 374


# run the search algorithm
path = astar_search(graph, heuristics, 'Lugoj', 'Bucharest')
print("Path:", path)