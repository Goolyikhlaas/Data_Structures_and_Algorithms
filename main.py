from graph import Graph
from shop import Shop
from shophashtable import ShopHashTable
from shopheap import ShopHeap
import copy


class MainApp:
        def __init__(self):
            #Initialize the main application with a graph, hash table, and heap.
            self.graph = Graph()
            self.shop_table = ShopHashTable()
            self.shop_heap = ShopHeap()
            
        #Display the main menu and handle user choices.
        def menu(self):
            while True:
                try:
                    print("\n----- SHOP FINDING & NAVIGATION SYSTEM -----")
                    print("GRAPH OPERATIONS:")
                    print("1.  Add Shop")
                    print("2.  Delete Shop")
                    print("3.  Update Shop Details")
                    print("4.  Add Connection Between Shops")
                    print("5.  Delete Connection")
                    print("6.  Find Path Between Shops (DFS/BFS)")
                    print("7.  Display Shortest Path (DFS/BFS)")
                    print("8.  Compare Paths (DFS vs BFS)")
                    print("9. Display All Shops")
                    
                    print("\nHASH TABLE OPERATIONS:")
                    print("10. Search Shop By Category")
                    print("11. Display Shops by Category")
                    
                    print("\nHEAP OPERATIONS:")
                    print("12.View Rated Shops by Category")
                    print("13. Display All Shops in Heap")
                    
                    print("\nEXIT:")
                    print("14. Exit")
                    print("\nHint:Press Ctrl+C to interrupt and enter your choice below.")
                    choice = input("Enter your choice: ")
    
                    if choice == "1":
                        self.add_shop()
                    elif choice == "2":
                        self.delete_shop()
                    elif choice == "3":
                        self.update_shop()
                    elif choice == "4":
                        self.add_connection()
                    elif choice == "5":
                        self.delete_connection()
                    elif choice == "6":
                        self.find_path()
                    elif choice == "7":
                        self.display_shortest_path()
                    elif choice == "8":
                        self.compare_path_lengths() 
                    elif choice == "9":
                        self.display_all_shops()
                    elif choice == "10":
                        self.search_shop()
                    elif choice == "11":
                        self.shop_table.display()
                    elif choice == "12":
                        self.display_shops_by_rating()
                    elif choice == "13":
                        self.shop_heap.display()
                    elif choice == "14":
                        print("Thank you for using the system!")
                        break
                    else:
                        print("Invalid choice! Please select a valid option.")
        
                except ValueError as ve:
                    print(f"An error occurred: {ve}")
                except KeyboardInterrupt:
                    print("\nYou interrupted the operation. Please choose an option from the menu or press 14 to exit.")

        #Add a new shop to the graph, hash table, and heap.
        def add_shop(self):
            while True:
                try:
                    number = int(input("Enter Shop Number: "))
                
                # Check if shop with given number already exists
                    if self.graph.has_vertex(number):
                        print(f"Shop {number} already exists! Please use a different number.")
                        continue
                    
                    break
                except ValueError:
                    print("Please enter a valid shop number.")

            name = input("Enter Shop Name: ")
            category = input("Enter Shop Category: ")
            location = input("Enter Shop Location: ")

            while True:
                try:
                    rating = float(input("Enter Shop Rating (1-5): "))
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("Rating must be between 1 and 5.")
                except ValueError:
                    print("Please enter a valid rating between 1 and 5.\n")
                
            shop = Shop(number, name, category, location, rating)

            self.graph.add_vertex(shop)
            self.shop_table.insert(shop)
            self.shop_heap.insert(shop)

            print(f"Shop {name} added successfully!")

        #Remove a shop from the graph and hash table.
        def delete_shop(self):
            number = int(input("Enter Shop Number to Delete: "))
            shop = self.graph.shops.get(number)
            if not shop:
                print("Shop not found!")
                return

            self.graph.remove_vertex(number)
            self.shop_table.delete(shop)

            print(f"Shop {shop.name} deleted successfully!")
            
        #Update details of an existing shop in the graph, hash table, and heap.   
        def update_shop(self):
            number = int(input("Enter Shop Number to Update: "))
            shop = self.graph.shops.get(number)
            if not shop:
                print("Shop not found!")
                return
        
            old_shop_copy = copy.deepcopy(shop)

            print("Enter new details (leave blank to keep current value):")
            name = input(f"Current Name ({shop.name}): ") or shop.name
            category = input(f"Current Category ({shop.category}): ") or shop.category
            location = input(f"Current Location ({shop.location}): ") or shop.location

            while True:  # Ensure a valid rating is provided
                try:
                    rating_input = input(f"Current Rating ({shop.rating}): ")
                    rating = float(rating_input) if rating_input else shop.rating
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("Rating must be between 1 and 5.")
                except ValueError:
                    print("Please enter a valid rating between 1 and 5.")

            self.graph.update_shop(number, "name", name)
            self.graph.update_shop(number, "category", category)
            self.graph.update_shop(number, "location", location)
            self.graph.update_shop(number, "rating", rating)

        # If the shop's category has changed, update it in the hashtable
            if old_shop_copy.category != category:
                try:
                    self.shop_table.delete(old_shop_copy)
                except ValueError as e:
                    print(f"An error occurred: {e}")
                self.shop_table.insert(self.graph.shops.get(number))  # get the updated shop from the graph

        # If the shop's rating has changed, clear the heap and reinsert all shops
            if old_shop_copy.rating != rating:
                self.shop_heap.clear()
                for shop in self.graph.shops.values():
                    self.shop_heap.insert(shop)

            print(f"Shop {number} updated successfully!")


        #Add a connection between two shops in the graph.
        def add_connection(self):
            try:
                source = int(input("Enter Source Shop Number: "))
                dest = int(input("Enter Destination Shop Number: "))
                self.graph.add_edge(source, dest)
                print(f"Connection between Shop {source} and Shop {dest} has been added!")
            except ValueError as e:
                print(e)
            except Exception as e:
                print(f"An error occurred: {e}")
                
        #Remove a connection between two shops from the graph.
        def delete_connection(self):
            try:
                source = int(input("Enter Source Shop Number: "))
                dest = int(input("Enter Destination Shop Number: "))

                self.graph.remove_edge(source, dest)
                print(f"Connection between Shop {source} and Shop {dest} removed!")
            except ValueError as e:
                print(f"Error: {e}")  # Display the error message from the raised exception.
            except Exception as e:
                print(f"An unexpected error occurred: {e}")  # For other unexpected errors.

        #Search for shops by their category in the hash table.
        def search_shop(self):
            category = input("Enter category to search: ")
            shops = self.shop_table.search(category)
            if not shops:
                print(f"No shops found in the category '{category}'.")
                return

            print(f"\nShops in the category '{category}':")
            print("-" * 40)
            for shop in shops:
                print(f"Shop Number: {shop.number}")
                print(f"Shop Name: {shop.name}")
                print(f"Location: {shop.location}")
                print(f"Rating: {shop.rating}")
                print("-" * 40)

        #Display shops in a specific category, sorted by their ratings, using the heap.
        def display_shops_by_rating(self):
            category = input("Enter category to display shops by rating: ")
            shops = self.shop_table.search(category)
            if not shops:
                print(f"No shops found in the category '{category}'.")
                return

            sorted_shops = self.shop_heap.sort_shops(shops)

            print(f"\nShops in the category '{category}' sorted by rating:")
            print("-" * 50)
            for shop in sorted_shops:
                print(f"Shop Number: {shop.number}")
                print(f"Shop Name: {shop.name}")
                print(f"Location: {shop.location}")
                print(f"Rating: {shop.rating}")
                print("-" * 50)

        #Display details of all shops present in the graph.
        def display_all_shops(self):
            if not self.graph.shops:
                print("No shops are currently in the system.")
                return

            print("\nAll Shops:")
            print("-----------------")
            for shop_number, shop in self.graph.shops.items():
                print(f"Shop Number: {shop.number}")
                print(f"Shop Name: {shop.name}")
                print(f"Category: {shop.category}")
                print(f"Location: {shop.location}")
                print(f"Rating: {shop.rating}\n")
                print("-----------------")
         
        #Find a path between two shops using either DFS or BFS methods in the graph.
        def find_path(self):
            source = int(input("Enter Source Shop Number: "))
            dest = int(input("Enter Destination Shop Number: "))
            
            method = input("Choose a method (dfs/bfs): ")
            if method == "dfs":
                path = self.graph.dfs(source, dest)
            else:
                path = self.graph.bfs(source, dest)

            print("Path:")
            for p in path:
                print(p, end=" -> ")
            print("End")
         
        #Display the shortest path between two shops in the graph.
        def display_shortest_path(self):
            source = int(input("Enter Source Shop Number: "))
            dest = int(input("Enter Destination Shop Number: "))

            path = self.graph.shortest_path(source, dest)
            
            if not path:
                print("No path found between the two shops!")
                return

            print("Shortest Path:")
            for p in path:
                print(p, end=" -> ")
            print("End")
         
        #Compare the lengths of paths obtained using DFS and BFS in the graph.
        def compare_path_lengths(self):
            try:
                source = int(input("Enter Source Shop Number: "))
                dest = int(input("Enter Destination Shop Number: "))
                
                comparison = self.graph.compare_paths(source, dest)
                print(comparison)
            except ValueError as e:
                print(e)
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    app = MainApp()
    app.menu()




