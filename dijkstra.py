# Dijkstra's algorithm

inf = float('inf') # Infinite value, if needed

def dijkstra(graph, start, end):
    nodes = list(graph.keys())
    distances = {}
    visited = []
    path = [end]
   
    currentNode = start
    currentNodeDistance = 0
    previousNode = None
    
    for item in nodes:
        distances[item] = [0, None]

    def getShortest():
        for item in nodes:
            if item not in visited and distances[item][0] != 0: #need to do it as actual shortest
                return item
            
    while currentNode:
        print(graph[currentNode])
        for adjacent in graph[currentNode]:
            if ((graph[currentNode][adjacent] + currentNodeDistance < distances[adjacent][0]) or distances[adjacent][0] == 0) and adjacent not in visited:
                distances[adjacent] = [graph[currentNode][adjacent] + currentNodeDistance, currentNode]
        previousNode = currentNode
        visited.append(currentNode)
        currentNode = getShortest()
        if currentNode == None: #or currentNode == end
            break
        currentNodeDistance = distances[currentNode][0]

    endDistance = distances[end][0]
    endNode = end
    while endDistance > 0:
        endNode = distances[endNode][1]
        endDistance = distances[endNode][0]
        path.append(endNode)
    path = list(reversed(path))
    ...
    return path

if __name__ == '__main__':
    
    from dijkstra_data import graphs
    
    while True:
        choice = input('Graph number? ')
        if not choice: break
        try:
            n = int(choice)
        except:
            continue
        if n >= len(graphs): continue
        print('Route is', dijkstra(*graphs[n]),'\n')
        