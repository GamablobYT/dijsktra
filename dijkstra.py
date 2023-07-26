import sys

try:
    vertNum = int((input("Enter no. of vertices: ")))
    adjMat = [[0 for column in range(vertNum)] for row in range(vertNum)] #adjacency matrix: contains distances of each vertex from its adjacent vertex with 0 indicating no edge
    while(True):
        print("Enter 0 to stop entering edges.")
        edge = list(map(int, input("Enter an edge in the format: node1 node2 distance: ").split()))
        
        #print("edge: ", edge)
        
        if edge == [0]:
            break
        elif edge[2] < 1:
            raise Exception("Negative and zero distances are not allowed 😡")
        elif edge[0] not in [i for i in range(vertNum)] or edge[1] not in [i for i in range(vertNum)]:
            raise Exception("node1 and node2 can only be integers in the range of 0 to numOfVertices - 1")
        else:
            adjMat[edge[0]][edge[1]] = edge[2] #assuming undirected graph for simplicity
            adjMat[edge[1]][edge[0]] = edge[2]
    
    distMat = [sys.maxsize for i in range(vertNum)] #distance of each vertex from source
    pathTree = [False for i in range(vertNum)]      #building shortest path to each final node, false indicates node has not been visited
    
    def minDistVert(distMat, pathTree): #returns index of nearest node to current node
        minDist = sys.maxsize           #sys.maxsize = maximum value that python allows
        
        for i in range(vertNum):
            if distMat[i] < minDist and pathTree[i] == False:  #if node i has not been visited and shorter path to it than the current recorded distance has been found
                minDist = distMat[i]
                minIndex = i
                
        return minIndex
    
    def dijkstra(sourceVert, adjacencyMatrix, distanceMatrix, shortestPathTree):
        distanceMatrix[sourceVert] = 0
        
        for i in range(vertNum):                      #traverse to nearest node
            minIndex = minDistVert(distanceMatrix, pathTree)
            pathTree[minIndex] = True    #visited
            
            for j in range(vertNum):                  #traverse all adjacent nodes to nearest node
                if adjacencyMatrix[minIndex][j] > 0 and shortestPathTree[j] == False and distanceMatrix[j] > distanceMatrix[minIndex] + adjacencyMatrix[minIndex][j]:
                    distanceMatrix[j] = distanceMatrix[minIndex] + adjacencyMatrix[minIndex][j] #third condition determines if there is a shorter path to the current node
                    
        print("Vertex \t Distance from source")
        for vert in range(vertNum):
            print(vert, "\t\t", distanceMatrix[vert])
            
    srcVert = int(input("Enter source vertex range 0-noOfVertices: "))
    dijkstra(srcVert, adjMat, distMat, pathTree)  
except Exception as e:
    print("Encountered an error. Please check if all the edges have been added according to 0 based indexing")
    print(e)
    
exitt = input("Enter anything to continue...")