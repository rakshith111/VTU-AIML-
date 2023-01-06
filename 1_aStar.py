'''
Implement A* Search algorithm.
'''
from queue import PriorityQueue
pk = PriorityQueue()


def a_star(graph, H_dist, start, end):
    # Set up data structures
    memory = {start: 0}
    prev = {}
    queue = PriorityQueue()
    queue.put((0, start))
    # Loop until the queue is empty
    while not queue.empty():
        current = queue.get()

        # Check if we've reached the end node
        if current[1] == end:
            # Generate the path by following the prev pointers
            path = []
            curr = current[1]
            while curr != start:
                path.append(curr)
                curr = prev[curr]
            path.append(start)
            return path[::-1]

      # Explore neighbors
        for neighbor, cost in graph[current[1]]:
            total_cost = memory[current[1]] + cost
            if neighbor not in memory or total_cost < memory[neighbor]:
                memory[neighbor] = total_cost
                priority = total_cost + H_dist.get(neighbor)
                prev[neighbor] = current[1]
                queue.put((priority, neighbor))

    print("No path found")


H_dist = {
    'A': 10,
    'B': 5,
    'C': 1,
    'D': 7,
    'E': 1,
}
Graph_nodes = {
    'A': [('B', 6), ('E', 3),],
    'B': [('D', 2), ('E', 5), ('C', 1)],
    'C': [('D', 1), ],
    'D': [('E', 8)],
    'E': [('C', 2), ('B', 3)]
}

print(a_star(Graph_nodes, 'A', 'C'))
H_dist = {
    'A': 10,
    'B': 4,
    'C': 5,
    'D': 300,
    'E': 3,
    'F': 1,
}
Graph_nodes = {
    'A': [('B', 3), ('C', 5),],
    'B': [('D', 4)],
    'C': [('E', 1), ],
    'D': [('F', 1)],
    'E': [('F', 1)]
}
print(a_star(Graph_nodes, 'A', 'F'))
