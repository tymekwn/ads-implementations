# Node definition
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.colour = "white"  # Unvisited

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
        neighbor.neighbors.append(self)  # Simple undirected graph

    def set_colour(self, colour):
        self.colour = colour


def Check_Graph(graph):
    for node in graph:
        if node.colour == "white":
            BFS(node)


# BFS function
def BFS(start_node):
    queue = [start_node]
    start_node.set_colour("grey")

    while queue:
        print(f"Queue: {[(node.value, node.colour) for node in queue]}")
        current_node = queue.pop(0)
        print(f"Visiting node: {current_node.value}")

        for neighbor in current_node.neighbors:
            if neighbor.colour == "white":
                neighbor.set_colour("grey")  # Mark as visited
                queue.append(neighbor)

        current_node.set_colour("black")  # Mark as fully explored


# Example graph
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
graph = [n1, n2, n3, n4, n5, n6, n7, n8]

n1.add_neighbor(n2)
n1.add_neighbor(n3)
n2.add_neighbor(n4)
n2.add_neighbor(n5)
n4.add_neighbor(n3)
n5.add_neighbor(n7)
n8.add_neighbor(n6)

Check_Graph(graph)
