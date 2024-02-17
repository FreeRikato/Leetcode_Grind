class Hashmap:
    # The Hashmap class uses separate chaining to handle collisions
    # We define a simple hash function and use a list of lists to store key-value pairs which can also be done using a linked list
    def __init__(self, size=10):
        # Initialize the Hashmap with a default size of 10 and a list of empty lists
        self.size = size
        self.buckets = [[] for _ in range(self.size)]  
        # Create a list of empty lists for separate chaining, we use list comprehension instead of [[]] * size to avoid the shallow copy issue that is when we append value to one list, it will be appended to all the lists (call by reference issue)

    def hash_function(self, key):
        return hash(key) % self.size  
        # Simple hash function: modulus of the built-in hash

    def put(self, key, value):
        hash_index = self.hash_function(key)
        # Get the bucket corresponding to the hash index
        bucket = self.buckets[hash_index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  
                # Update the key-value pair if key is found
                return
        bucket.append((key, value))  # Add a new key-value pair if key is not found
        # Since bucket = self.buckets[hash_index] is a reference to the list, any changes made to bucket will be reflected in self.buckets[hash_index]

    def get(self, key):
        hash_index = self.hash_function(key)
        bucket = self.buckets[hash_index]

        for k, v in bucket:
            if k == key:
                return v  # Return the value if the key is found
        return None  # Return None if the key is not found

    def remove(self, key):
        hash_index = self.hash_function(key)
        bucket = self.buckets[hash_index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]  # Delete the key-value pair if the key is found
                return

# Example usage
hashmap = Hashmap()

# Insert some key-value pairs
hashmap.put("key1", "value1")
hashmap.put("key2", "value2")
hashmap.put("key3", "value3")

# Retrieve a value
print(hashmap.get("key2"))  # Output: value2

# Remove a key-value pair
hashmap.remove("key2")

# Try to retrieve a value for a removed key or a non-existent key
print(hashmap.get("key2"))  # Output: None
