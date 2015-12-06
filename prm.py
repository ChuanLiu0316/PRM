from ImageProcessing import ImageProcessing
from AStar import AStar
import random
class PRM(object):
    def __init__(self): 
        #represent graph as Ajacency list
        # to get all neighbors, just call self.graph[index]
        self.graph = []
        self.vertex = []
        #Vertex Set, vertex as form (index, (x, y), grayscale), remember to get value of (x,y)
        #vertex[0] := index, vertex[1] := (x,y), vertex[2]: grayscale
        #need to do G[y][x], index from 0 to numberOfPoints, easy to get. 
        self.edge = [] #Edge Set, may not be neccessary 
        self.TwoDMatrix = None
        self.botRadius = 0

    # isWayBlocked : ((int, int), (int, int)) -> bool
    # isWayBlocked, given two point in the Image, check if the line between 
    # the two point is blocked by obstacles  
    def isWayBlocked(self, (x1, y1), (x2, y2)): 
        x1 = float(x1) 
        x2 = float(x2)     
        y1 = float(y1)  
        y2 = float(y2)  
        slope = (y2 - y1)/(x2 - x1)
        for currentX in range(int(x1), int(x2)):
            currentY = int(y1 + slope * (currentX - x1))
            for offset in range(-self.botRadius+1, self.botRadius+1):
                if  self.TwoDMatrix[currentY][currentX] > 200: 
                    return True

        return False                 


    #initialize : (file, int, int) -> 0  (if no problem)
    # initialize, given a imageFilename, and how many points you want to generate
    # for the PRM, and the botRadius, initialize all the values of the instance,
    # especially, an ajacency list to represent a graph spreading whole image,
    # if there is no obstacle between two vertex, then there is an edge bewteen them 
    def initialize(self, imageName, numberOfPoints, botRadius):
        #extract value from image
        ImgProInstance = ImageProcessing()
        ImgMatrix = ImgProInstance.TranformJPGto2DArray(imageName)
        self.TwoDMatrix = ImgMatrix
        height = len(ImgMatrix)
        width = len(ImgMatrix[0])
        i = 0
        while (i < 1000):
            x = random.randint(0, width-1)
            y = random.randint(0, height-1)
            #if on obstacle 
            if self.TwoDMatrix[y][x] > 200:
                #decrease index for consistency 
                i = i -1
            else:
                self.vertex.append((i, (x,y), ImgMatrix[y][x]))
            i = i+1       

        for i in range(numberOfPoints):
            neighbors = []
            for j in range(numberOfPoints):
                if self.vertex[i][2] > 200 or self.vertex[j][2] > 200:
                    print "for debugging, this shouldn't happen"    
                elif i == j: 
                    pass        
                elif self.isWayBlocked(self.vertex[i][1], self.vertex[j][1]):
                    pass
                else:
                    if i < j:
                        #add to Edge set
                        neighbors.append(self.vertex[j])
                        self.edge.append((self.vertex[i], self.vertex[j]))
                    else: 
                        #already in edge set, just add to neighbors 
                        neighbors.append(self.vertex[j])
            
            self.append(neighbors)   
        return 0 

    # findWay ((x,y), (x,y))
    # findWay, given a source coordinates, based on the Probabilistic Road Map,
    # using A* algorithm      
    def findWay(self, source, target): 
        AstarInstance = Astar()
        resultRoad = AstarInstance.run(self.graph, source, target, "temp.txt")
        return resultRoad
                                                  