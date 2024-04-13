class ShopHashTable:
    def __init__(self):
        #Initializes a ShopHashTable, which is a hashtable storing shops categorized by their categories.
        self.table = {}

    def insert(self, shop):
#Inserts a shop into the hashtable under its category.
#Args: shop (Shop): The shop object to insert.

        if shop.category not in self.table:
            self.table[shop.category] = []
        self.table[shop.category].append(shop)

    def delete(self, shop):
# Deletes a shop from the hashtable.
#Args:shop (Shop): The shop object to delete.
#Raises:ValueError: If the category does not exist or the shop is not found.
        if shop.category in self.table:
            if shop in self.table[shop.category]:
                self.table[shop.category].remove(shop)
                
                # Check if the category list is now empty, and if so, remove the category.
                if not self.table[shop.category]:
                    del self.table[shop.category]
            else:
                # Shop not found in category, so we  exit the method
                return
        else:
            raise ValueError(f"Category {shop.category} does not exist.")

    def search(self, category):
        # Searches for shops in a specific category.
        shops_in_category = self.table.get(category, [])
        
        # If no shops are found for the given category
        if not shops_in_category:
            print(f"No shops found for category '{category}'!")
            return []
        
        # Displaying the shops in a user-friendly format
        print(f"Shops in category '{category}':")
        for shop in shops_in_category:
            print(f"Shop Number: {shop.number}")
            print(f"Shop Name: {shop.name}")
            print(f"Location: {shop.location}")
            print(f"Rating: {shop.rating}\n")
        
        return shops_in_category

    def update(self, old_shop, new_shop):
        #Updates a shop in the hashtable by removing the old shop and inserting the new shop.
        # If the category has changed, remove the shop from the old category first
        if old_shop.category != new_shop.category:
            if old_shop not in self.table.get(old_shop.category, []):
                # Shop not found in category, so we silently exit the method
                return
        
            self.table[old_shop.category].remove(old_shop)
            # Check if the category list of old shop is now empty, and if so, remove the category.
            if not self.table[old_shop.category]:
                del self.table[old_shop.category]

        # Now add the shop to the new category
        self.insert(new_shop)

    def display(self):
        #Displays all the shops in the hashtable, grouped by category.
        if not self.table:
            print("No shops to display!")
            return
        
        for category, shops in self.table.items():
            print(f"Category: {category}")
            for shop in shops:
                print(f"\tShop Name: {shop.name}, Rating: {shop.rating}")




   

        



