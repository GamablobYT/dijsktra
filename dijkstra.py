import sys

vertNum = int((input("Enter no. of vertices: ")))
adjMat = [[0 for i in range(vertNum)] for j in range(vertNum)]

try:
    while(True):
        print("Enter 0 to stop entering edges.")
        edge = list(map(int, input("Enter an edge in the format: node1 node2 distance: ").split()))
        
        #print("edge: ", edge)
        
        if edge == [0]:
            break
        else:
            adjMat[edge[0]][edge[1]] = edge[2]
            adjMat[edge[1]][edge[0]] = edge[2]
except:
    print("Encountered an error. Please check if all the edges have been added according to 0 based indexing")
    
distMat = [sys.maxsize for i in range(vertNum)]
pathTree = [False for i in range(vertNum)]

def minDistVert(distMat, pathTree):
    minDist = sys.maxsize
    
    for i in range(vertNum):
        if distMat[i] < minDist and pathTree[i] == False:
            minDist = distMat[i]
            minIndex = i
            
    return minIndex

def dijkstra(sourceVert, adjacencyMatrix, distanceMatrix, shortestPathTree):
    distanceMatrix[sourceVert] = 0
    
    for i in range(vertNum):
        minIndex = minDistVert(distMat, pathTree)
        pathTree[minIndex] = True    #visited
        
        for j in range(vertNum):
            if adjacencyMatrix[minIndex][j] > 0 and shortestPathTree[j] == False and distanceMatrix[j] > distanceMatrix[minIndex] + adjacencyMatrix[minIndex][j]:
                distanceMatrix[j] = distanceMatrix[minIndex] + adjacencyMatrix[minIndex][j] #third condition determines if there is a shorter path to the current node
                
    print("Vertex \t Distance from source")
    for vert in range(vertNum):
        print(vert, "\t", distanceMatrix[vert])
        
dijkstra(8, adjMat, distMat, pathTree)