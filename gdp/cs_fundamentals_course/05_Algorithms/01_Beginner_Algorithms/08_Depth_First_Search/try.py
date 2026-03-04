

"""
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()             # initialize on first call

    visited.add(node)               # mark as visited
    print(node, end=" ")

    for neighbor in graph.get(node, []):
        print(neighbor)
        print()
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# --- Example graph (adjacency list) ---
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A')
# Output: A B D E F C
"""



graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : [],
}



"""
create the visited with data 
check if node has been visited 
 add more node to the visited set 
 compare the node to the target 

"""

"""

def dfs(graph, node , target, visited=None):
    if visited is None:
        visited = set()
   
    if node in visited:
        return  False 
    
    visited.add(node)

    if node == target:
        return True

    print(node)
    print()

    for n in graph.get(node,[]):
        if dfs(graph, n, target, visited):
            return True
    return False 




dfs(graph,"A", "E")

"""






"""
1 .state the visited and  create the datastructure
2 . check the element in the set if the node exist
3.   add node to visited 
4 . compare the node to the target 
"""
def dfs_search(g, node, target, visited=None)->bool :
    if visited is None:
        visited = set()
    
    if node in visited:
        return False 
    
    visited.add(node)

    if node == target:
        print("E exist")
        return True 
    
    for n in g.get(node, []):
        if dfs_search(g, n, target, visited):
            print("Found {target}")
            return True 
    return False 


graph = {
    'A': ["B", 'C'],
    'B' : ['D','E'],
    'C': ["F"],
    'D' : [],
    'E':['F'],
    'F' :[]
}
    
dfs_search(graph,"A","E")