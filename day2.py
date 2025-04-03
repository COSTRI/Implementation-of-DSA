#Implementation of Hash, Graphs and Dictionaries

hash_table = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

# Accessing a value using its key
print(hash_table["key1"])  # Output: value1
# Adding a new key-value pair
hash_table["key4"] = "value4"
print(hash_table)  # Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
# Removing a key-value pair
hash_table.pop("key2")
print(hash_table)  # Output: {'key1': 'value1', 'key3': 'value3', 'key4': 'value4'}


#Extended implementation of Hashs
class HashTable:
    def __init__(self, size=7):
        self.size = size
        self.table = [[] for _ in range(size)]  # array of lists

    def hash_function(self, key):
        """Generate a hash for a given key."""
        return hash(key) % self.size

    def HashInsert(self, key, value):
        # Check if the key already exists
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value
                return
        # If the key does not exist, append the new key-value pair
        self.table[index].append([key, value])

    def HashSearch(self, key):
        # Search for a key in the table
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]  # returns the value associated with the key
        return None  # if the key is not found

    def HashDelete(self, key):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                self.table[index].remove(kv)
                return True
        return False  # if key not found

    def DeleteHashTable(self):
        self.table = [[] for _ in range(self.size)]
        # clears the table


# Example usage of HashTable class
hash_table = HashTable()

# Insert key-value pairs
hash_table.HashInsert("Kofi Manu", 241222334)
hash_table.HashInsert("Adwoa", 5241222334)
hash_table.HashInsert("Doe", 278891173)
hash_table.HashInsert("Joe", 244669895)
hash_table.HashInsert("Alimna", 201234567)
hash_table.HashInsert("Yal", 4789123456)
hash_table.HashInsert("Maku", 509962278)

#print the indices
print(hash_table.hash_function("Kofi Manu"))  # Output: index
print(hash_table.hash_function("Adwoa"))      # Output: index
print(hash_table.hash_function("Doe"))         # Output: index
print(hash_table.hash_function("Joe"))         # Output: index
print(hash_table.hash_function("Alimna"))      # Output: index
print(hash_table.hash_function("Maku"))        # Output: index
print(hash_table.hash_function("Yal"))         # Output: index

# Search for keys
print(hash_table.HashSearch("Adwoa"))  # Output: 5241222334
print(hash_table.HashSearch("Doe"))    # Output: 278891173

# Delete a key
hash_table.HashDelete("Joe")
print(hash_table.HashSearch("Joe"))    # Output: None (key deleted)

# Clear the entire hash table
hash_table.DeleteHashTable()
print(hash_table.table)  # Output: [[], [], [], [], [], [], []]


# Implementation of Graphs

# Example implementation of adjacency matrix
class GraphAjacencyMatrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[0] * vertices for _ in range(vertices)]  # initialize a matrix

    def add_edge(self, u, v):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:  # Ensure valid indices
            self.matrix[u][v] = 1  # for unweighted 
            self.matrix[v][u] = 1  # if graph is undirected
        else:
            print(f"Error: Invalid vertices {u}, {v}")

    def display(self):
        for row in self.matrix:
            print(row)

# Example usage
graph = GraphAjacencyMatrix(4)  # Create a graph with 4 vertices

# Add edges
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

# Display the adjacency matrix
print("Adjacency Matrix:")
graph.display()

# Output:
# Adjacency Matrix:
# [0, 1, 1, 0]
# [1, 0, 1, 0]
# [1, 1, 0, 1]
# [0, 0, 1, 0]


#Adjacency List
class GraphAdjacencyList:
    def __init__(self):
        self.graph = {}  # Dictionary to hold the graph

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)  # For unweighted graphs
        self.graph[v].append(u)  # If the graph is undirected

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

# Example usage
graph_list = GraphAdjacencyList()
graph_list.add_edge(0, 1)
graph_list.add_edge(0, 4)
graph_list.add_edge(1, 2)
graph_list.add_edge(1, 3)
graph_list.add_edge(1, 4)
graph_list.add_edge(2, 3)
graph_list.add_edge(3, 4)

graph_list.display()