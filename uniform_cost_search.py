import csv
import sys
from queue import PriorityQueue


class CityNotFoundError(Exception):
    def __init__(self, city):
        print("%s does not exist" % city)

graph = {}

def build_graph(path):
    start = path[0]
    end = path[1]
    distance = path[2]

    if start not in graph:
        graph[start] = []
    if end not in graph:
        graph[end] = []
    
    graph[start].append((end,distance))
    graph[end].append((start,distance))
    


def uniform_cost_search(graph, start, end):

    if start not in graph or end not in graph:
        raise CityNotFoundError(start if start not in graph else end)
    
    queue = PriorityQueue()
    queue.put((0, start, [start]))
    visited = set()
    while queue:
        cost, node, path = queue.get()
        if node not in visited:
            visited.add(node)
            if node == end:
                print("Minimum distance between " , start , " and " , end , " is : ", cost)
                print("Path is " ,*path, sep = "-> ")
                return path
                    

            for neighbor, distance in graph[node]:
                if neighbor not in visited:
                    queue.put((cost+int(distance), neighbor, path+[neighbor]))
    raise CityNotFoundError(end)



if __name__ == "__main__":
    with open(sys.argv[1], newline='',encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if not row[0].startswith("city"): 
                path = row[0].split(",")
            
                build_graph(path)

    uniform_cost_search(graph,sys.argv[2],sys.argv[3])
    



