import random 
from ImageProcessing import ImageProcessing
class PRM(object):
    def __init__(self): 
        #represent graph as Ajacency list
        # to get all neighbors, just call self.graph[index]
        self.graph = None
        self.vertex = None
        #Vertex Set, vertex as form (index, (x, y), grayscale), remember to get value of (x,y)
        #vertex[0] := index, vertex[1] := (x,y), vertex[2]: grayscale
        #need to do G[y][x], index from 0 to numberOfPoints, easy to get. 
        self.edge = None #Edge Set, may not be neccessary 
        self.2DMatrix = None
        self.botRadius = 0
    def isWayBlocked((x1, y1), (x2, y2)): 
        x1 = float(x1) 
        x2 = float(x2)     
        y1 = float(y1)  
        y2 = float(y2)  
        slope = (y2 - y1)/(x2 - x1)
        for currentX in range(int(x1), int(x2)):
            currentY = int(y1 + slope * (currentX - x1))
            for offset in range(-self.botRadius+1, self.botRadius+1):
                if  self.2DMatrix[currentY][currentX] > 200: 
                    return True

        return False                 

    def initialize(imageName, numberOfPoints, botRadius):
        #extract value from image
        ImgMatrix = ImageProcessing.TranformJPGto2DArray(imageName)
        self.2DMatrix = ImgMatrix
        height = len(ImgMatrix)
        width = len(ImgMatrix[0])
        for i in range(numberOfPoints):
            x = random.(0, width)
            y = random.(0, height)
            #if on obstacle 
            if self.vertex[i][2] > 200:
                #decrease index for consistency 
                i = i-1
            else:
                self.vertex.append((i, (x,y), ImgMatrix[y][x]))

        for i in range(numberOfPoints):
            neighbors = []
            for j in range(numberOfPoints):
                if self.vertex[i][2] > 200 || self.vertex[j][2] > 200
                    print "for debugging, this shouldn't happen"    
                elif i = j: 
                    pass        
                elif isWayBlocked(self.vertex[i][2], self.vertex[j][2]):
                    pass
                else:
                    if i < j:
                        #add to Edge set
                        neighbors.append(self.vertex[j])
                        edges.append(self.vertex[i], self.vertex[j])
                    else: 
                        #already in edge set, just add to neighbors 
                        neighbors.append(self.vertex[j])
            
            self.append(neighbors)   
        return 0                                       