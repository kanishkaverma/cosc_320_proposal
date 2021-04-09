from queue import PriorityQueue
from graph_from_csv import makeGraph
import airport_graph as ag
from queue import PriorityQueue
import copy
import random
import time
import matplotlib.pyplot as plt

#graph = makeGraph('./flight_data_cleaned_final.csv', 10)
# add to currentime by flight time. when checking the weighting time, get difference between currenttime
#current time = deptime + air time
# def solution(flights, src, dst, s):
# 	pq = PriorityQueue()
# 	initState = State(src, s)
# 	pq.add(initState)
# 	visitedStates = []
# 	while pq not empty:
# 		currentState = pq.pop()
#         if currentState.currentAirport == dst:
#             return currentState.prevFlights
#         for flight in flights[currentState.currentAirport]:
#             if flight.startTime > currentState.currentTime and flight.dest not in currentState.prevFlights
#               newState = State(flight, currentState)
# If newState not in visitedStates
# pq.add(newState)
# 	visitedStates.append(new State)
# return null // In the event all possible states were checked and there was no possible flight

plotGrowthRate = False

def linkedState(G: ag.Graph, src: int, dst: int, startTime: int):
    if src not in G.airports or dst not in G.airports:
        if not plotGrowthRate: 
            print("The src and destination are not both in the graph")
        return []
    currentSolution = []
    linkedStateHelper(G, src, dst, startTime, currentSolution)
    return currentSolution

def linkedStateHelper(G: ag.Graph, currentLoc: int, dst: int, currentTime: int, currentSolution: list): # Returns a list of flights to take
    # We arrived where we trying to get
    if currentLoc == dst:
        return currentSolution
    # Update our network of airports for the current time, and reset visited
    G.updateAirports(currentTime)
    # Get the current shortest path
    djkstraSolution = djkstraPath(G, currentLoc, dst, currentTime)

    # There is no available path from the currentLocation in time to the solution: path is impossible
    if len(djkstraSolution) == 0:
        return None
    # Add our step we got to the current solution
    currentSolution.append(djkstraSolution[0])
    # Run function again, now from the new airport we are at
    linkedStateHelper(G, djkstraSolution[0].dst, dst, djkstraSolution[0].postFlightTime, currentSolution)

def djkstraPath(G: ag.Graph, src: int, dst: int, currentTime: int): # Returns an array of flights
    # Both src and dst are not in graph: solution is impossible
    if src not in G.airports or dst not in G.airports:
        if not plotGrowthRate: 
            print("The src and destination are not both in the graph")
        return []
    else:
        pq = PriorityQueue()
        currentAirport = G.airports[src]
        for flight in currentAirport.costFlightIntersections:
            pq.put(flight)
        while not pq.empty():
            currentFlightCostIntersection = pq.get()
            currentCost = currentFlightCostIntersection.cost
            # If we took a flight to our destination: we found our route
            if currentFlightCostIntersection.flight.dst == dst:
                return
            # If we could not find a solution, we are looking at invalid and impossible edges
            if currentCost == float("inf"): 
                return []
            # This is an intermediate airport to a possible solution: add current flights, flag as visited
            currentAirport = G.airports[currentFlightCostIntersection.flight.dst]
            if not currentAirport.visited: # Avoid visiting the same airport twice
                for flight in currentAirport.costFlightIntersections:
                    if flight.cost < float("inf"): # avoid adding to infinity for safety
                        flight.addCost(currentCost)
                        pq.put(flight)
                currentAirport.visited = True
            else: # For readability: if we visited this airport before, just skip it
                continue



def realSolutionHelper(G: ag.Graph, src: int, dst: int, startTime: int):
    ourSolution = realSolution(G,src,dst,startTime)
    # There was no solution
    if len(ourSolution) == 0:
        if not plotGrowthRate:
            print("There was no solution found")  
        return False  
    else: # There was a solution
        if not plotGrowthRate
            print(f"The solution from {src} to {dst} is ")
            for state in ourSolution:
                if state.flight != None:
                    print(state.flight)
            print(ourSolution[len(ourSolution)-1].cost)
        return True

def realSolution(G: ag.Graph, src: int, dst: int, startTime: int):
    # If our nodes are not both in the graph, obviously impossible
    if src not in G.airports or dst not in G.airports:
        if not plotGrowthRate: 
            print("The src and destination are not both in the graph")
        return []
    else:
        # Create an inital state, place in pq
        startState = ag.State(src,None,startTime,[], 0)
        pq = PriorityQueue()
        pq.put(startState)
        while not pq.empty():
            # Get the current state
            currentState = pq.get()
            # If we arrived at our destination, add current state to our solution, and return it
            if currentState.currentLoc == dst:
                currentState.pastStates.append(currentState)
                return currentState.pastStates
            else: # Intermediate node: add all the new states we can reach from this state
                # Get current airport, and copy the current states (so we can alter freely)
                currentAirport = G.airports[currentState.currentLoc]
                newPastStates = copy.deepcopy(currentState.pastStates)
                # Add current state to this states working solution
                newPastStates.append(currentState)
                # Add all the valid states from this airport at this point in time
                for flight in currentAirport.flights:
                    if flight.takeOffTime > currentState.endTime:
                        newState = ag.State(flight.dst,flight,currentState.endTime,copy.deepcopy(newPastStates), currentState.cost)
                        pq.put(newState)
        # There was no solution, we fully explored literally every state
        if not plotGrowthRate:
            print("There was no path that made a solution possible")
        return []

if __name__=="__main__":

    # First test case: can it find a direclty connecting edge?

    G = ag.Graph() # initialize graph
    f1 = ag.Flight(1,2,3,4,100) # add flight
    G.addAirport(1)
    G.addAirport(2)
    G.addFlight(f1)
    realSolutionHelper(G,1,2,1)
        
    

    if plotGrowthRate:
        upperBound = 500 # maximum number of flights to consider in loop
        lowerBound = 100
        step = 10
        calcTime = [] # stores timeDelta for finding solution
        inputSize = [] # stores the input size for the respective timeDelta
        src = 10980 # src airport id
        dst = 12896 # destination airport id
        
        for i in range(lowerBound, upperBound, step):
            GReal = makeGraph("flight_data_cleaned_final.csv", i)
            d = list(GReal.airports.keys())
            t0 = time.time()
            airportList = random.sample(d, 2)
            solutionFound = realSolutionHelper(GReal,airportList[0],airportList[1], 1000)
            t1 = time.time()
            if not solutionFound:
                calcTime.append(t1-t0)
                inputSize.append(i)
                print("Iteration: " + str(i))

        plt.plot(inputSize, calcTime)
        plt.title('Calculation Time VS Number of Flights Considered Per Node')
        plt.xlabel('Input')
        plt.ylabel('Calculation Time')
        plt.show()

    else:
        GReal = makeGraph("flight_data_cleaned_final.csv", 50)
        d = list(GReal.airports.keys())
        airportList = random.sample(d, 2)
        realSolutionHelper(GReal,airportList[0],airportList[1], 20000)

    