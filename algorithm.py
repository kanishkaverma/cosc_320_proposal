from queue import PriorityQueue

# def solution(flights, src, dst, s):
# 	pq = PriorityQueue(StateComparator())
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


def solution(flights, src, dst, s):
    pq = PriorityQueue()
    
