from Queue import PriorityQueue
import math
class AStar(object):
    @staticmethod
    def run(graph, start, end, outfile):
        resultRoad = []
        fo = open(outfile, "w")
        def e_dis((cx,cy),(endx, endy)):
            return math.sqrt((endx-cx)*(endx-cx) + (endy-cy)*(endy-cy))

        def recursive_print(currentS):
        
            if currentS[1] == 0 :
                return
            else:
                recursive_print(currentS[3])
                resultRoad.append(currentS[2])
                fo.write(currentS[2]) 
                
        pq = PriorityQueue()
        startS = (e_dis(start,end), 0.0, start, None)
        pq.put(startS);
        popNumber = 0 
        while not pq.empty() : 
            currentS = pq.get()
            popNumber = popNumber+1
            (index, (cx,cy)) = currentS[2]
            cost = currentS[1]
            if (cx,cy) == end: 
                fo.write(str(popNumber))
                fo.write("\n")
                recursive_print(currentS)
                fo.close()
                return resultRoad 
            else: 
                for neighbor in graph[index]:     
                    h = e_dis(neighbor[1], end)
                    newcost = cost+e_dis(neighbor[1], (cx,cy))
                    f = h+g
                    pq.put((f, newcost, neighbor,currentS[2]))
  
        #this shouldn't happen    
        return -1    

