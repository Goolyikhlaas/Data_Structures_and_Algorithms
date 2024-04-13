from collections import deque
from shop import Shop
import copy

class Graph:
    def __init__(self):
        # Adjacency list representation of the graph
        self.adj_list = {}
        # Stores information about each shop
        self.shops = {}

    def add_vertex(self, shop: Shop):
        # Check if the shop is already present
        if shop.number in self.adj_list:
            raise ValueError(f"Shop {shop.number} already exists!")
        # Add the shop to the adjacency list and shops dictionary
        self.adj_list[shop.number] = []
        self.shops[shop.number] = shop

    def remove_vertex(self, shop_number):
        # Remove the shop and its connections
        if shop_number not in self.adj_list:
            raise ValueError(f"Shop {shop_number} doesn't exist!")
        for vertex in self.adj_list:
            if shop_number in self.adj_list[vertex]:
                self.adj_list[vertex].remove(shop_number)
        self.adj_list.pop(shop_number)
        self.shops.pop(shop_number)

    def add_edge(self, source, destination):
        # Function to add a bidirectional edge between source and destination shops
        if source == destination:
            raise ValueError("A shop cannot be connected to itself.")
        if source not in self.adj_list:
            raise ValueError(f"Shop {source} doesn't exist!")
        if destination not in self.adj_list:
            raise ValueError(f"Shop {destination} doesn't exist!")
        if destination in self.adj_list[source]:
            raise ValueError(f"A connection between Shop {source} and Shop {destination} already exists!")
        self.adj_list[source].append(destination)
        self.adj_list[destination].append(source)
        
    def remove_edge(self, source, dest):
        # Remove the edge between the source and destination shops
        if source not in self.adj_list:
            raise ValueError(f"Shop {source} doesn't exist!")
        if dest not in self.adj_list:
            raise ValueError(f"Shop {dest} doesn't exist!")
        if dest not in self.adj_list[source]:
            raise ValueError(f"No edge exists from Shop {source} to Shop {dest}")
        self.adj_list[source].remove(dest)
        self.adj_list[dest].remove(source)


    def update_shop(self, shop_number, attribute, new_value):
        # Update a specific attribute of a shop and return the old and new shop details
        if shop_number not in self.shops:
            raise ValueError(f"Shop {shop_number} doesn't exist!")
    
        old_shop = copy.deepcopy(self.shops[shop_number])
    
        if attribute == "name":
            self.shops[shop_number].name = new_value
        elif attribute == "category":
            self.shops[shop_number].category = new_value
        elif attribute == "location":
            self.shops[shop_number].location = new_value
        elif attribute == "rating":
            if 1 <= new_value <= 5:
                self.shops[shop_number].rating = new_value
            else:
                raise ValueError("Rating should be between 1 and 5!")
        else:
            raise ValueError(f"Invalid attribute: {attribute}")
    
        new_shop = self.shops[shop_number]
    
        return old_shop, new_shop

    
    def has_vertex(self, shop_number):
        # Checks if a particular shop exists in the graph
        return shop_number in self.adj_list


    def dfs(self, start, end):
        # Depth-first search function to find a path from start to end
        if start not in self.adj_list:
            raise ValueError(f"Shop {start} doesn't exist!")
        if end not in self.adj_list:
            raise ValueError(f"Shop {end} doesn't exist!")
        
        stack = [start]
        visited = set()
        prev_nodes = {start: None}
    
        while stack:
            vertex = stack.pop()
            if vertex == end:
                break
            if vertex not in visited:
                visited.add(vertex)
                for neighbour in self.adj_list[vertex]:
                    if neighbour not in visited:
                        stack.append(neighbour)
                        prev_nodes[neighbour] = vertex
    
        if end not in prev_nodes:
            return []  # Returning empty list instead of raising an error
        
        path = []
        while end:
            path.append(end)
            end = prev_nodes[end]
        path.reverse()
        
        return path
    
    def bfs(self, start, end):
        # Breadth-first search function to find the shortest path from start to end
        if start not in self.adj_list:
            raise ValueError(f"Shop {start} doesn't exist!")
        if end not in self.adj_list:
            raise ValueError(f"Shop {end} doesn't exist!")
        
        queue = deque([start])
        visited = {start}  # Start is marked visited as soon as it's added to the queue
        prev_nodes = {start: None}
    
        while queue:
            vertex = queue.popleft()
            if vertex == end:
                break
            for neighbour in self.adj_list[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    prev_nodes[neighbour] = vertex
    
        if end not in prev_nodes:
            return []  # Returning empty list instead of raising an error
            
        path = []
        while end:
            path.append(end)
            end = prev_nodes[end]
        path.reverse()
    
        return path


    #Use both DFS and BFS to find the path and return the shorter one
    def shortest_path(self, start, end):
        path_dfs = self.dfs(start, end)
        path_bfs = self.bfs(start, end)
    
        if not path_dfs and not path_bfs:
            return []
        elif not path_dfs:
            return path_bfs
        elif not path_bfs:
            return path_dfs
        else:
            return path_dfs if len(path_dfs) < len(path_bfs) else path_bfs
        
    # Compare the paths found by DFS and BFS
    def compare_paths(self, start, end):
        if start not in self.adj_list:
            raise ValueError(f"Shop {start} doesn't exist!")
        if end not in self.adj_list:
            raise ValueError(f"Shop {end} doesn't exist!")

        path_dfs = self.dfs(start, end)
        path_bfs = self.bfs(start, end)

        length_dfs = len(path_dfs)
        length_bfs = len(path_bfs)

        if not path_dfs:
            return f"BFS Path is shorter with length {length_bfs}."
        elif not path_bfs:
            return f"DFS Path is shorter with length {length_dfs}."
        elif length_dfs == length_bfs:
            return f"Both paths have the same length of {length_dfs}."
        else:
            return f"DFS Path has length {length_dfs} and BFS Path has length {length_bfs}."





