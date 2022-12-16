file1 = open('data.txt', 'r')
Lines = file1.readlines()

valves = []
for line in Lines:
    line = line.strip()
    valve = line.split(" ")[1]
    rate = int(line.split("=")[1].split(";")[0])
    lead = line.split(" ")[9:]
    lead = [x.replace(",", "") for x in lead]
    # valve name, its rate, where it leads to, and if it is open
    valves.append((valve, rate, lead, False))

def dijkstra(graph, start, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph[current_node][next_node] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

# Create a graph
graph = {}
for valve in valves:
    graph[valve[0]] = {}
    for lead in valve[2]:
        graph[valve[0]][lead] = 1

pressure = 0
cur_pressure = 0
time = 0
path = []
cur_valve = "AA"
while time < 30:
    time += 1
    print("Minute ", time)
    print("Releasing pressure: ", cur_pressure)
    pressure += cur_pressure
    if len(path) == 0:
        # find valves that are closed
        closed_valves = [x for x in valves if x[3] == False]
        # find the path to all closed valves and calculate path length
        updated_valves = []
        for valve in closed_valves:
            p = dijkstra(graph, cur_valve, valve[0])
            if p == "Route Not Possible":
                valve = (valve[0], 0, valve[2], valve[3])
            else:
                # update valve with how much pressure it would release
                rem_time = 30 - time - len(p) + 1
                possible_pressure = rem_time * valve[1]
                print("possible pressure of valve ", valve[0], " is ", possible_pressure, " with path ", p)
                updated_valves.append((valve[0], possible_pressure, valve[2], valve[3]))
        # sort by path length
        updated_valves = sorted(updated_valves, key=lambda x: x[1])
        # find the path to the closest valve
        path1 = dijkstra(graph, cur_valve, updated_valves[-1][0])
        print("Finding path to valve ", updated_valves[-1][0], " with rate ", updated_valves[-1][1], " with path ", path1)
        path2 = []
        path3 = []
        if len(updated_valves) > 1 and updated_valves[-2][1] > 0.5*updated_valves[-1][1]:
            path2 = dijkstra(graph, cur_valve, updated_valves[-2][0])
            print("Finding path to valve ", updated_valves[-2][0], " with rate ", updated_valves[-2][1], " with path ", path2)
        if len(updated_valves) > 2 and updated_valves[-3][1] > 0.5*updated_valves[-1][1]:
            path3 = dijkstra(graph, cur_valve, updated_valves[-3][0])
            print("Finding path to valve ", updated_valves[-3][0], " with rate ", updated_valves[-3][1], " with path ", path3)
        # get the shortest path
        path = path1
        if len(path2) < len(path) and len(path2) > 0:
            path = path2
        if len(path3) < len(path) and len(path3) > 0:
            path = path3
        print("Generated new path: ", path)

    if len(path) > 0:
        if path[0] == cur_valve:
            path.pop(0)
            if len(path) == 0:
                print("Opening valve ", cur_valve)
                # open the valve, we are in destination
                for i in range(len(valves)):
                    if valves[i][0] == cur_valve:
                        valves[i] = (valves[i][0], valves[i][1], valves[i][2], True)
                        cur_pressure += valves[i][1]
                        break
            else:
                cur_valve = path[0]
                print("Moving to ", cur_valve)

print(pressure)

