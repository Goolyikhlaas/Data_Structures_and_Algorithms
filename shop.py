class Shop:
    def __init__(self, number, name, category, location, rating):
        if not 1 <= rating <= 5:
            raise ValueError("Rating should be between 1 and 5!")
    
        self.number = number
        self.name = name
        self.category = category
        self.location = location
        self.rating = rating

    def __hash__(self):
        #Returns a hash value for the Shop object.
        return hash((self.number, self.name, self.category, self.location, self.rating))

    def __eq__(self, other):
        #Checks if two Shop objects are equal based on their attributes.
        if isinstance(other, Shop):
            return (self.number, self.name, self.category, self.location, self.rating) == \
                   (other.number, other.name, other.category, other.location, other.rating)
        return False

    def __str__(self):
        #Returns a string representation of the Shop object.
        return f"Shop Number: {self.number}, Name: {self.name}, Category: {self.category}, Location: {self.location}, Rating: {self.rating}"

        