from queue import PriorityQueue
from collections import defaultdict


graph = defaultdict(list)
hn = {'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dorbeta': 242, 'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
      'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}



def best_first_search(source, target, n):

    explored = []
    frontier = PriorityQueue()
    frontier.put((0, source))
    hnv = hn[source]
    while frontier.empty() == False:
        u = frontier.get()[1]

        # Displaying the path having lowest cost
        print(u, end="-> ")
        if u == target:
            break

        for v, c in graph[u]:
            if hn[v] < hnv:
                hnv = hn[v]
                if v not in explored:
                    explored.append(v)
                    frontier.put((c, v))
            else:
                continue

# Function for adding edges to graph


def generate_edges():
    edges = []

    # for each node in graph
    for node in graph:

        # for each neighbour node of a single node
        for neighbour, cost in graph[node]:

            # if edge exists then append
            edges.append((node, neighbour, cost))
    return edges


def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

addedge('Zerind', 'Arad', 75)
addedge('Zerind', 'Oradea', 71)
addedge('Oradea', 'Sibiu', 151)
addedge('Arad', 'Sibiu', 140)
addedge('Arad', 'Timisoara', 118)
addedge('Sibiu', 'Fagaras', 99)
addedge('Sibiu', 'Rimnicu Vilcea', 146)
addedge('Timisoara', 'Lugoj', 111)
addedge('Lugoj', 'Mehadia', 70)
addedge('Mehadia', 'Drobeta', 75)
addedge('Drobeta', 'Craiova', 120)
addedge('Rimnicu Vilcea', 'Craiova', 138)
addedge('Rimnicu Vilcea', 'Pitesti', 97)
addedge('Pitesti', 'Bucharest', 101)
addedge('Pitesti', 'Craiova', 138)
addedge('Fagaras', 'Bucharest', 211)
addedge('Bucharest', 'Giurgiu', 90)
addedge('Bucharest', 'Urziceni', 85)
addedge('Urziceni', 'Hirsova', 98)
addedge('Urziceni', 'Vaslui', 142)
addedge('Hirsova', 'Eforie', 86)
addedge('Vaslui', 'Iasi', 92)
addedge('Iasi', 'Neamt', 87)

generate_edges()
best_first_search('Zerind', 'Bucahrest', v)

