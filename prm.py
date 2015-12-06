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
        def outOfIndex(x,y):
            height = len(self.TwoDMatrix)
            width = len(self.TwoDMatrix[0])
            if x < 0 or x >= width: 
                return True
            if y < 0 or y >= height:
                return True
            return False        

        x1 = float(x1) 
        x2 = float(x2)     
        y1 = float(y1)  
        y2 = float(y2)
        if x1==x2 and y1==y2:
            return False

        if x1 == x2:     
            slopeXY = (x2 - x1)/(y2 - y1)            
            for currentY in range(int(y1), int(y2)):
                currentX = int(x1 + slopeXY * (currentY - y1))
                for offset in range(-self.botRadius+1, self.botRadius+1):
                    if outOfIndex(currentX+offset, currentY):
                        pass 
                    elif  self.TwoDMatrix[currentY][currentX+offset] > 200: 
                        return True  
                    else:
                        pass
        elif y1 == y2: 
            slopeYX = (y2 - y1)/(x2 - x1)
            for currentX in range(int(x1), int(x2)):
                currentY = int(y1 + slopeYX * (currentX - x1))
                for offset in range(-self.botRadius+1, self.botRadius+1):
                    if outOfIndex(currentX, currentY+offset): 
                        pass
                    elif  self.TwoDMatrix[currentY+offset][currentX] > 200: 
                        return True
                    else:
                        pass    
        else:    
            slopeYX = (y2 - y1)/(x2 - x1)
            for currentX in range(int(x1), int(x2)):
                currentY = int(y1 + slopeYX * (currentX - x1))
                for offset in range(-self.botRadius+1, self.botRadius+1):
                    if outOfIndex(currentX, currentY+offset): 
                        pass
                    elif  self.TwoDMatrix[currentY+offset][currentX] > 200: 
                        return True
                    else:
                        pass 
            slopeXY = (x2 - x1)/(y2 - y1)            
            for currentY in range(int(y1), int(y2)):
                currentX = int(x1 + slopeXY * (currentY - y1))
                for offset in range(-self.botRadius+1, self.botRadius+1):
                    if outOfIndex(currentX+offset, currentY):
                        pass 
                    elif  self.TwoDMatrix[currentY][currentX+offset] > 200: 
                        return True  
                    else:
                        pass         

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
                    (tmpIndex, (tempX, tempY), NotImportant) = self.vertex[j] 
                    if i < j:
                        #add to Edge set
                        neighbors.append((tmpIndex, (tempX, tempY)))
                        self.edge.append((self.vertex[i], self.vertex[j]))
                    else: 
                        #already in edge set, just add to neighbors 
                        neighbors.append((tmpIndex, (tempX, tempY)))
            
            self.graph.append(neighbors)   
        return 0 

    # findWay ((x,y), (x,y))
    # findWay, given a source coordinates, based on the Probabilistic Road Map,
    # using A* algorithm      
    def findWay(self, source, target): 
        AstarInstance = Astar()
        resultRoad = AstarInstance.run(self.graph, source, target, "temp.txt")
        return resultRoad
                                                  