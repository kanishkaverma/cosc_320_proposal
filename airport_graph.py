
# First, Vertex and Graph classes for directed graphs
from functools import cmp_to_key
from queue import PriorityQueue
# Constants we are going to use
PRICE_PER_DISTANCE = 2.80/40
PRICE_PER_FLIGHT_TIME = 13
PRICE_PER_WAIT_TIME = 10
OFFLOADTIME = 10*60

class Flight:
    def __init__(self, src: int, dst: int, takeOffTime, airTime: int, dist: int):
        self.src = src
        self.dst = dst
        self.takeOffTime = takeOffTime
        self.airTime = airTime
        self.dist=dist

    def __str__(self):
        return f"src: {self.src} dst: {self.dst} takeOffTime: {self.takeOffTime} airTime: {self.airTime} distance: {self.dist}\n"

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

    # def __repr__(self):
    #     return {'name':self.name}
    
    def __str__(self):
        outputStr = f"AirportID:: {self.airportId} \n"
        for flight in self.flights:
            outputStr += f"\t {flight.__str__()}"
        return outputStr

    def sortByTakeOffTime(self):
        def comparator(a, b):
            if a.takeOffTime < b.takeOffTime:
                return -1
            if a.takeOffTime > b.takeOffTime:
                return 1
            return 0
        self.flights = sorted(self.flights, key=cmp_to_key(comparator))
        
# This is a directed graph class for use in this course.
# It can also be used as an undirected graph by adding edges in both directions.
class Graph:
    def __init__(self):
        self.airports = {}

    def addAirport(self, airportId: int) -> bool:
        if airportId in self.airports:
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
        outputStr = "For this entire graph, the airports are: \n\n\n"
        for airportId in self.airports.keys():
            outputStr += f"{self.airports[airportId].__str__()}\n"
        return outputStr

class State:
    # "Counstructor" for inital state
    def startState(self, currentLoc: int, currentTime: int):
        self.flight = None
        self.currentTime = None
        self.currentLoc = currentLoc
        self.waitTime = 0
        self.cost = 0
        self.pastStates = []
        self.endTime = currentTime

    def __init__(self, currentLoc: int, flight: Flight, currentTime: int, pastStates: list, currentCostTotal: float):
        if flight == None:
            self.startState(currentLoc, currentTime)
            return
        self.flight = flight
        self.currentTime = currentTime
        self.currentLoc = currentLoc
        self.waitTime = flight.takeOffTime - currentTime
        self.cost = currentCostTotal + self.getCost()
        self.pastStates = pastStates
        self.endTime = self.currentTime + self.waitTime + OFFLOADTIME

    def __eq__(self, other):
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost
    
    def getCost(self):
        waitCost = (self.waitTime/60/60)*PRICE_PER_WAIT_TIME
        flightTimeCost = (self.flight.airTime/60/60)*PRICE_PER_FLIGHT_TIME 
        distCost = self.flight.dist * PRICE_PER_DISTANCE
        return  waitCost + flightTimeCost + distCost
    
    def __str__(self):
        return ""

if __name__ == "__main__":
    airportOne = Airport(1234)

    src = 1111
    dst = 2222
    takeoffTime = 3980
    airTime = 400
    dist = 100
    flight = Flight(src, dst, takeoffTime, airTime, dist)
    airportOne.addFlight(flight)

    src = 1111
    dst = 2222
    takeoffTime = 1980
    airTime = 400
    dist = 100
    flight = Flight(src, dst, takeoffTime, airTime, dist)
    airportOne.addFlight(flight)

    src = 1111
    dst = 2222
    takeoffTime = 2980
    airTime = 400
    dist = 100
    flight = Flight(src, dst, takeoffTime, airTime, dist)
    airportOne.addFlight(flight)

    airportOne.sortByTakeOffTime()
    print(airportOne.flights[2].takeOffTime)


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
