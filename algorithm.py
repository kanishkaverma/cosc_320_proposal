from queue import PriorityQueue
from graph_from_csv import makeGraph
import airport_graph as ag
from queue import PriorityQueue
import copy

graph = makeGraph('./flight_data_cleaned_final.csv', 10)
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


def solution(graph, flights, src, dst, s):
    pq = PriorityQueue()
    initState = [] #State(src, flights, )
    pq.add(initState)
    visitedStates = []
    while pq.empty()== False: 
        currentState = pq.pop()
        if currentState.currentAirport == dst:
            return currentState.prevFlights 

def realSolutionHelper(G: ag.Graph, src: int, dst: int, startTime: int):
    ourSolution = realSolution(G,src,dst,startTime)
    if len(ourSolution) == 0:
        print("There was no solution found")    
    else:
        for state in ourSolution:
            print(state.flight)

def realSolution(G: ag.Graph, src: int, dst: int, startTime: int):
    if src not in G.airports or dst not in G.airports:
        print("The src and destination are not both in the graph")
        return []
    else:
        startState = ag.State(src, None, startTime, [])
        pq = PriorityQueue()
        pq.put(startState)
        while not pq.empty():
            currentState = pq.get()
            if currentState.currentLoc == dst:
                return currentState.pastStates
            else:
                currentAirport = G.airports[currentState.currentLoc]
                newPastStates = copy.deepcopy(currentState.pastStates)
                newPastStates.append(currentState)
                for flight in currentAirport.flights:
                    if flight.takeOffTime > currentState.endTime:
                        newState = ag.State(flight.dst,flight,currentState.endTime,copy.deepcopy(newPastStates))
                        pq.put(newState)
        print("There was no path that made a solution possible")
        return []

if __name__=="__main__":
    G = ag.Graph()
    f1 = ag.Flight(1,2,3,4,100)
    G.addAirport(1)
    G.addAirport(2)
    G.addFlight(f1)
    realSolutionHelper(G,1,2,1)