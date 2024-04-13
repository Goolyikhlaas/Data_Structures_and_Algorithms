import pytest
from shop import Shop
from graph import Graph
from shophashtable import ShopHashTable
from shopheap import ShopHeap
import csv

# Setup fixture to create a graph object for each test
@pytest.fixture
def setup_graph():
    graph = Graph()

    # Using relative paths for CSV files
    with open("./shops.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            shop = Shop(int(row['number']), row['name'], row['category'], row['location'], int(row['rating']))
            graph.add_vertex(shop)
    
    with open("./edges.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            graph.add_edge(int(row['source']), int(row['destination']))

    return graph

def test_add_vertex(setup_graph):
    print("Adding a new shop (ShopF) to the graph...")
    shop = Shop(6, "ShopF", "Toys", "Northeast", 3)
    setup_graph.add_vertex(shop)
    assert setup_graph.has_vertex(6) == True
    print("ShopF added successfully!")

def test_remove_vertex(setup_graph):
    print("Removing shop (ShopA) from the graph...")
    setup_graph.remove_vertex(1)
    assert setup_graph.has_vertex(1) == False
    print("ShopA removed successfully!")

def test_add_edge(setup_graph):
    print("Adding an edge between ShopD and ShopE...")
    setup_graph.add_edge(4, 5)
    # To verify, check if 5 is a neighbour of 4 and vice-versa
    assert 5 in setup_graph.adj_list[4]
    assert 4 in setup_graph.adj_list[5]
    print("Edge between ShopD and ShopE added successfully!")

def test_remove_edge(setup_graph):
    print("Removing edge between ShopA and ShopB...")
    setup_graph.remove_edge(1, 2)
    # To verify, check if 2 is no longer a neighbour of 1 and vice-versa
    assert 2 not in setup_graph.adj_list[1]
    assert 1 not in setup_graph.adj_list[2]
    print("Edge between ShopA and ShopB removed successfully!")

def test_update_shop(setup_graph):
    print("Updating name of ShopA to NewShopA...")
    old_shop, new_shop = setup_graph.update_shop(1, "name", "NewShopA")
    assert old_shop.name == "ShopA"
    assert new_shop.name == "NewShopA"
    print("Name of ShopA updated to NewShopA successfully!")

def test_dfs_path(setup_graph):
    print("Finding a path using DFS from ShopA to ShopE...")
    path = setup_graph.dfs(1, 5)
    # Just a basic check to ensure path starts at 1 and ends at 5
    assert path[0] == 1
    assert path[-1] == 5
    print(f"Path found using DFS: {path}")

def test_bfs_path(setup_graph):
    print("Finding a path using BFS from ShopA to ShopE...")
    path = setup_graph.bfs(1, 5)
    assert path[0] == 1
    assert path[-1] == 5
    print(f"Path found using BFS: {path}")

def test_shortest_path(setup_graph):
    print("Finding the shortest path from ShopA to ShopE...")
    path = setup_graph.shortest_path(1, 5)
    assert path[0] == 1
    assert path[-1] == 5
    print(f"Shortest path found: {path}")

def test_compare_paths(setup_graph):
    print("Comparing DFS and BFS paths from ShopA to ShopE...")
    result = setup_graph.compare_paths(1, 5)
    assert "DFS Path" in result or "BFS Path" in result or "Both paths have the same length" in result
    print(f"Comparison result: {result}")

def test_add_existing_vertex(setup_graph):
    print("Trying to add an existing shop (ShopA) to the graph...")
    shop = Shop(1, "ShopA", "Books", "West", 4)
    with pytest.raises(ValueError):
        setup_graph.add_vertex(shop)
    print("Expected error raised for adding existing shop!")

def test_remove_non_existent_vertex(setup_graph):
    print("Trying to remove a non-existent shop (Shop100) from the graph...")
    with pytest.raises(ValueError):
        setup_graph.remove_vertex(100)
    print("Expected error raised for removing non-existent shop!")

def test_remove_non_existent_edge(setup_graph):
    print("Trying to remove a non-existent edge (ShopA to Shop100) from the graph...")
    with pytest.raises(ValueError):
        setup_graph.remove_edge(1, 100)
    print("Expected error raised for removing non-existent edge!")

def test_non_existent_dfs_path(setup_graph):
    print("Trying to find a DFS path from ShopA to a non-existent shop (Shop100)...")
    with pytest.raises(ValueError):
        setup_graph.dfs(1, 100)
    print("Expected error raised for finding DFS path to non-existent shop!")

def test_non_existent_bfs_path(setup_graph):
    print("Trying to find a BFS path from ShopA to a non-existent shop (Shop100)...")
    with pytest.raises(ValueError):
        setup_graph.bfs(1, 100)
    print("Expected error raised for finding BFS path to non-existent shop!")

@pytest.fixture
def setup_hash_table():
    shop_hash = ShopHashTable()

    # Reading from shops.csv
    with open("./shops.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            shop = Shop(int(row['number']), row['name'], row['category'], row['location'], int(row['rating']))
            shop_hash.insert(shop)
    
    return shop_hash

def test_hash_table_insert_shop(setup_hash_table):
    shop_f = Shop(6, "ShopF", "Toys", "Center", 3) # Adding a new shop for testing
    print(f"\nInserting {shop_f.name} into hash table...")
    setup_hash_table.insert(shop_f)
    assert shop_f in setup_hash_table.search(shop_f.category)

def test_hash_table_delete_shop(setup_hash_table):
    shop_b = Shop(2, "ShopB", "Clothing", "West", 3)
    print(f"\nDeleting {shop_b.name} from hash table...")
    setup_hash_table.delete(shop_b)
    assert shop_b not in setup_hash_table.search(shop_b.category)

def test_hash_table_search_category(setup_hash_table):
    shop_a = Shop(1, "ShopA", "Electronics", "East", 4)
    print(f"\nSearching for category {shop_a.category}...")
    shops = setup_hash_table.search(shop_a.category)
    assert shop_a in shops

def test_hash_table_update_shop_category(setup_hash_table):
    shop_a = Shop(1, "ShopA", "Electronics", "East", 4)
    new_shop_a = Shop(1, "ShopAUpdated", "Music", "East", 4) # Updated name and category for demonstration
    print(f"\nUpdating {shop_a.name}'s category from {shop_a.category} to {new_shop_a.category}...")
    setup_hash_table.update(shop_a, new_shop_a)
    assert shop_a not in setup_hash_table.search(shop_a.category)
    assert new_shop_a in setup_hash_table.search(new_shop_a.category)

def test_hash_table_display(setup_hash_table):
    print("\nDisplaying hash table content...")
    setup_hash_table.display()

@pytest.fixture
def setup_shop_heap():
    heap = ShopHeap()

    # Reading shops from shops.csv
    with open("./shops.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            shop = Shop(int(row['number']), row['name'], row['category'], row['location'], int(row['rating']))
            heap.insert(shop)

    return heap

def test_heap_insert_and_pop(setup_shop_heap):
    """Test the insert and pop functionalities of the ShopHeap."""
    print("\n[Test: Insert and Pop]")
    
    # Insert a new shop with a low rating
    shop = Shop(6, "ShopF", "Toys", "Center", 1)
    setup_shop_heap.insert(shop)

    print(f"-> Inserted shop: {shop.name} with rating: {shop.rating}")

    # When we pop, we should get the shop with the highest rating first.
    top_shop = setup_shop_heap.pop()
    print(f"-> Popped shop: {top_shop.name} with rating: {top_shop.rating}")
    assert top_shop.name in ["ShopC", "ShopE"], f"Expected ShopC or ShopE but got {top_shop.name}"

def test_heap_sort_shops(setup_shop_heap):
    """Test the sorting mechanism of the ShopHeap."""
    print("\n[Test: Sort Shops]")

    sorted_shops = setup_shop_heap.sort_shops([Shop(1, "ShopA", "Electronics", "East", 4.5),
                                               Shop(2, "ShopB", "Clothing", "West", 3.5),
                                               Shop(3, "ShopC", "Books", "North", 5),
                                               Shop(4, "ShopD", "Food", "South", 2.5),
                                               Shop(5, "ShopE", "HomeGoods", "Center", 4)])

    # Ensure the sorted order is correct based on rating
    print(f"-> Top rated shop after sorting: {sorted_shops[0].name} (Rating: {sorted_shops[0].rating})")
    print(f"-> Lowest rated shop after sorting: {sorted_shops[-1].name} (Rating: {sorted_shops[-1].rating})")
    assert sorted_shops[0].rating == 5  # Highest rating
    assert sorted_shops[-1].rating == 2.5  # Lowest rating

def test_heap_rebuild(setup_shop_heap):
    """Test the rebuild_heap method of the ShopHeap."""
    print("\n[Test: Rebuild Heap]")

    # Creating new shops for testing
    new_shops = [Shop(5, "ShopE", "HomeGoods", "Center", 4.5),
                 Shop(6, "ShopF", "Hardware", "Northeast", 4)]
    setup_shop_heap.rebuild_heap(new_shops)

    # After rebuilding, the top shop should be ShopE as it has the highest rating among the new shops
    top_shop = setup_shop_heap.pop()
    print(f"-> Popped shop after rebuilding: {top_shop.name} (Rating: {top_shop.rating})")
    assert top_shop.name == "ShopE", f"Expected ShopE but got {top_shop.name}"








