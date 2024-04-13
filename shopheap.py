import heapq

class ShopHeap:
    def __init__(self):
        self.heap = []
        self.counter = 0  

    def insert(self, shop):
        heapq.heappush(self.heap, (-shop.rating, self.counter, shop))
        self.counter += 1

    def pop(self):
        if not self.heap:
            raise IndexError("The heap is empty. Cannot pop from an empty heap.")
        _, _, shop = heapq.heappop(self.heap)
        return shop

    def clear(self):
        """Clears the heap."""
        self.heap = []

    def sort_shops(self, shops):
        """Sorts a list of shops by rating in descending order."""
        sorted_shops = []
        temp_heap = [(-shop.rating, shop) for shop in shops]
        heapq.heapify(temp_heap)
        
        while temp_heap:
            _, shop = heapq.heappop(temp_heap)
            sorted_shops.append(shop)

        return sorted_shops

    def rebuild_heap(self, shops):
        """Clears and rebuilds the heap using the provided list of shops."""
        self.clear()
        for shop in shops:
            self.insert(shop)

    def display_sorted(self, shops):
        """Displays the shops in sorted order by rating."""
        sorted_shops = self.sort_shops(shops)
        
        print("\nShops in Descending Order of Ratings:")
        print("--------------------------------------")
        for shop in sorted_shops:
            print(f"Shop Number: {shop.number}, Shop Name: {shop.name}, Rating: {shop.rating}")
        print("--------------------------------------\n")
        
    def display(self):
        if not self.heap:
            print("The heap is empty.")
            return

        print("\nShops in the Heap:")
        print("-------------------")
        for _, _, shop in self.heap:  
            print(f"Shop Number: {shop.number}, Shop Name: {shop.name}, Rating: {shop.rating}")
        print("-------------------\n")








