file1 = open('data.txt', 'r')
Lines = file1.readlines()

grid = []
S = (0,0)
E = (0,0)
for line in Lines:
    line = line.strip()
    grid.append(list(line))
    for c in grid[-1]:
        if c == 'S':
            S = (len(grid)-1, grid[-1].index(c))
        if c == 'E':
            E = (len(grid)-1, grid[-1].index(c))

grid[S[0]][S[1]] = 'a'
grid[E[0]][E[1]] = 'z'

possible_starts = []
shortest_path_len = 999999
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'a':
            possible_starts.append((i,j))

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

# create graph
graph = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        elevation = ord(grid[i][j])
        graph[(i,j)] = {}
        if i > 0 and ord(grid[i-1][j]) - elevation <= 1:
            graph[(i,j)][(i-1,j)] = 1
        if i < len(grid)-1 and ord(grid[i+1][j]) - elevation <= 1:
            graph[(i,j)][(i+1,j)] = 1
        if j > 0 and ord(grid[i][j-1]) - elevation <= 1:
            graph[(i,j)][(i,j-1)] = 1
        if j < len(grid[0])-1 and ord(grid[i][j+1]) - elevation <= 1:
            graph[(i,j)][(i,j+1)] = 1

#print(graph)
# find shortest path
path = dijkstra(graph, S, E)
print(len(path)-1)

# Part 2
for s in possible_starts:
    path = dijkstra(graph, s, E)
    if path == "Route Not Possible":
        continue
    if len(path)-1 < shortest_path_len:
        shortest_path_len = len(path)-1

print(shortest_path_len)