
# First, Vertex and Graph classes for directed graphs
from functools import cmp_to_key
# Constants we are going to use
PRICE_PER_DISTANCE = 0
PRICE_PER_FLIGHT_TIME = 0
PRICE_PER_WAIT_TIME = 0

class Flight:
    def __init__(self, src: int, dst: int, takeOffTime, airTime: int, dist: int):
        self.src = src
        self.dst = dst
        self.takeOffTime = takeOffTime
        self.airTime = airTime
        self.dist=dist

class Airport:
    def __init__(self, airPortId: int):
        self.flights = []
        self.airportId = airPortId
        # useful for DFS
        self.status = "unvisited"
        
    def hasFlight(self,dst: int):
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
    def addFlight(self, flight: Flight) -> bool:
        if flight.src not in self.airports:
            print("Could not add flight because src not in graph")
            return False
        else:
            self.airports[flight.src].addFlight(flight)

    
    def __str__(self):
        returnStr = "Airports are: \n"
        returnStr += str(self.airports.keys())
        return returnStr

class State:
    def __init__(self, currentLoc: int, flight: Flight, currentTime):
        self.flight = flight
        self.currentTime = currentTime
        self.currentLoc = currentLoc
        self.cost = self.getCost()

        def __repr__(self):
            return {'cost':self.getCost}
    
    def getCost(self):
        waitCost = (self.flight.takeOffTime-self.currentTime)*PRICE_PER_WAIT_TIME
        flightTimeCost = (self.flight.airTime)*PRICE_PER_FLIGHT_TIME 
        distCost = self.flight.dist * PRICE_PER_DISTANCE
        return  waitCost + flightTimeCost + distCost

    def comparator(a, b):
        if a.cost < b.cost:
            return -1
        if a.cost > b.cost:
            return 1
        return 0

if __name__ == "__main__":
    print("Hello")
    data = []

    currentLoc = 1111
    src = 1111
    dst = 2222
    takeoffTime = 1980
    airTime = 121
    dist = 30
    currentTime = 1940

    flight = Flight(src, dst, takeoffTime, airTime, dist)
    state = State(currentLoc, flight, currentTime)
    data.append(state)

    currentLoc_ = 1111
    src_ = 1111
    dst_ = 2222
    takeoffTime_ = 1980
    airTime_ = 400
    dist_ = 100
    currentTime_ = 1940

    flight = Flight(src_, dst_, takeoffTime_, airTime_, dist_)
    state = State(currentLoc_, flight, currentTime_)
    data.append(state)

    data = sorted(data, key=cmp_to_key(State.comparator))
    for i in data:
        print(i.flight.airTime)

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
