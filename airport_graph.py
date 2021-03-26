
# First, Vertex and Graph classes for directed graphs

# Constants we are going to use
PRICE_PER_DISTANCE = 0
PRICE_PER_FLIGHT_TIME = 0
PRICE_PER_WAIT_TIME = 0

class Airport:
    def __init__(self, airPortId):
        self.flights = []
        self.airportId = airPortId
        # useful for DFS
        self.status = "unvisited"
        
    def hasFlight(self,dst):
        for flight in self.flights:
            if flight.dst == dst:
                return True
        return False
        
    def addFlight(self, flight: Flight):
        self.flights.append(flight)
    
    def __str__(self):
        return str(self.airportId) 
        
# This is a directed graph class for use in this course.
# It can also be used as an undirected graph by adding edges in both directions.
class Graph:
    def __init__(self):
        self.airports = {}

    def addAirport(self, airportId: int) -> bool:
        if airportId in self.airports:
            print("Airport already added")
            return False
        else:
            newAirport = Airport(airportId)
            self.airports[airportId] = newAirport
            return True
        
    # add a flight to the graph
    def addFlight(self,flight: Flight) -> bool:
        if flight.src not in self.airports:
            print("Could not add flight because src not in graph")
            return False
        else:
            self.airports[flight.src].addFlight(flight)

    
    def __str__(self):
        returnStr = "Airports are: \n"
        returnStr += str(self.airports.keys())
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
        self.cost = self.getCost()
    
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
