<a name="br1"></a>**Project Definition**

Project Title: Implementation of Uniform Cost Search Algorithm in Python



**Introduction**

The purpose of this project is to implement the Uniform Cost Search algorithm in Python. The
algorithm enables finding the shortest path between two cities by considering the distances
between them. The project takes inputs such as a CSV file containing city distances and the
names of the start and end cities. The implementation involves building a graph from the
given data and performing a uniform cost search to determine the shortest path.

**Inputs**

1\. Cities: A CSV file containing the distances between two cities in a tabular format.

2\. Start: The name of the start city (string).

3\. End: The name of the end city (string)

**Methods**

**1. build\_graph(path):**

Parameters:

• path: A list representing a path containing the start city, end city, and

the distance between them.

Implementation:

• This method checks if the start and end cities are already in the graph

(initialized globally).

• If not found, it adds the start and end cities to the graph along with the

distance between them.

**2. uniform\_cost\_search(graph, start, end):**

Parameters:

• graph: A dictionary representing the graph of cities and the distances

between them.

• start: The name of the start city (string).
• end: The name of the end city (string).




<a name="br2"></a>Implementation:

• This method performs a uniform cost search on the given graph to find
 the shortest path between the start and end cities.
• If either the start or end city is not present in the graph, it raises an
 exception.

• It utilizes a priority queue to explore nodes based on their cost.
• Nodes are visited and expanded until the destination city is reached or
 all possible paths are explored.

• Once the destination is found, it prints the minimum distance and the

path taken to reach the destination.

• If the destination is not found, it raises a custom exception

(CityNotFoundError).

**3. main():**

Parameters: None.

Implementation:

• This method serves as the entry point of the program.
• It reads a CSV file, extracts paths from the rows, builds a graph using
 the extracted paths, and performs a uniform cost search on the graph
 based on the provided command-line arguments.

**Conclusion**

In conclusion, this project implements the Uniform Cost Search algorithm in Python to find
the shortest path between two cities. By utilizing a priority queue and graph representation,
the algorithm efficiently explores different paths to determine the optimal route. The
implementation successfully reads a CSV file, builds the graph, and performs the uniform cost
search to provide the minimum distance and path between the start and end cities.
