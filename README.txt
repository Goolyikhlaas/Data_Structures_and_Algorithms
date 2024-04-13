
# Shop Finding & Navigation System

## Description:
Users can manage and navigate shops in a mall-like environment with the aid of the Shop Finding & Navigation System. To efficiently store and retrieve shop information, the system incorporates a number of data structures, including graphs, heaps, and hash tables. Users can add, remove, update shop details, locate routes between shops, and sort shops according to customer reviews.

## File Structure:
- `graph.py`: Defines the `Graph` class for representing and manipulating the mall's shop layout.
- `shop.py`: Contains the `Shop` class to represent individual shops.
- `shophashtable.py`: Implements the `ShopHashTable` class for categorising shops based on their categories.
- `shopheap.py`: Introduces the `ShopHeap` class for managing shops based on their ratings.
- `main.py`: The main application file that integrates the above components and provides a user interface for interaction.
- `test_data.py`: Contains test cases using the `pytest` framework to ensure the functionality of the system.
- shops.csv: A CSV file containing details about each shop, such as shop number, name, category, location, and rating.
- edges.csv: A CSV file that defines connections between shops, facilitating the creation of the graph structure.

## Basic Usage:
1. Run the `main.py` script to start the application.
2. Follow the on-screen prompts to interact with the system.

## Testing:
1. Install `pytest` using pip: pip install pytest
2. Navigate to the directory containing `test_data.py`.
3. Run the tests using the command: pytest -s 

   
