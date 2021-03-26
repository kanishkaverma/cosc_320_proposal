
# First, Vertex and Graph classes for directed graphs

# Constants we are going to use
PRICE_PER_DISTANCE = 0
PRICE_PER_FLIGHT_TIME = 0
PRICE_PER_WAIT_TIME = 0

class Airport:
    def __init__(self, v):
        self.flights = []
        self.airportId = v
        # useful for DFS
        self.inTime = None
        self.outTime = None
        self.status = "unvisited"
        
    def hasOutNeighbor(self,v):
        if v in self.outNeighbors:
            return True
        return False
        
    def getOutNeighbors(self):
        return self.flights
        
    def addOutNeighbor(self,v):
        self.flights.append(v)
    
    def __str__(self):
        return str(self.airportId) 
        
# This is a directed graph class for use in this course.
# It can also be used as an undirected graph by adding edges in both directions.
class Graph:
    def __init__(self):
        self.vertices = []

    def addVertex(self,n):
        self.vertices.append(n)
        
    # add a directed edge from CS161Node u to CS161Node v
    def addDiEdge(self,u,v):
        u.addOutNeighbor(v)
        v.addInNeighbor(u)
        
    # add edges in both directions between u and v
    def addBiEdge(self,u,v):
        self.addDiEdge(u,v)
        self.addDiEdge(v,u)
        
    # get a list of all the directed edges
    # directed edges are a list of two vertices
    def getDirEdges(self):
        ret = []
        for v in self.vertices:
            ret += [ [v, u] for u in v.outNeighbors ]
        return ret
    
    def __str__(self):
        ret = "Graph with:\n"
        ret += "\t Vertices:\n\t"
        for v in self.vertices:
            ret += str(v) + ","
        ret += "\n"
        ret += "\t Edges:\n\t"
        for a,b in self.getDirEdges():
            ret += "(" + str(a) + "," + str(b) + ") "
        ret += "\n"
        return ret

class Flight:
    def __init__(self, src, dst, takeoffTime, airTime, dist):
        self.src = src
        self.dst = dst
        self.takeoffTime = takeoffTime
        self.airTime = airTime
        self.dist=dist

class State:
    def __init__(self, currentLoc, flight: Flight, currentTime):
        self.flight = flight
        self.currentTime = currentTime
        self.currentLoc = currentLoc
    
    def getCost(self):
        waitCost = (self.flight.takeoffTime-self.currentTime)*PRICE_PER_WAIT_TIME
        flightTimeCost = (self.flight.airTime)*PRICE_PER_FLIGHT_TIME 
        distCost = self.flight.dist * PRICE_PER_DISTANCE
        return  waitCost + flightTimeCost + distCost

def create_aiport_graph(dairport):
    airport_graph = Graph() 
    for index, row in  dairport.iterrows():
        print(row['OriginAirportID'])
        airport_vertex = Vertex(row['OriginAirportID'])
        airport_graph.addVertex(airport_vertex)

    return airport_graph

if __name__ == "__main__":
    print("Hello")

"""
import pandas as pd 

df = pd.read_csv('flight_data_cleaned.csv')
df.head()



dg = df.sample(50, axis=0)
dairport = dg.drop_duplicates(subset=["OriginAirportID"],inplace= False)
# dg.head()
# dairport.head()
print(create_aiport_graph(dairport))


"""
