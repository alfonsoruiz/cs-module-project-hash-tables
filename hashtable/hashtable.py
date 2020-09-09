class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, key, value):
        current_node = HashTableEntry(key, value)

        if self.head is not None:
            current_node.next = self.head

        self.head = current_node

    def get(self, key):
        current_node = self.head

        while current_node is not None:
            if current_node.key == key:
                return current_node

            current_node = current_node.next

        return None

    def delete(self, key):
        current_node = self.head

        # If hash table is empty
        if current_node is None:
            return None

        # If specified item is in the head position
        if current_node.key == key:
            self.head = current_node.next
            return current_node
        # If specified item is not in the head position
        else:
            previous_node = current_node
            current_node = current_node.next

            while current_node is not None:
                # If node with specified key is found
                if current_node.key == key:
                    # Remove bindings from specified node
                    previous_node.next = current_node.next
                    # Return deleted node
                    return current_node
                else:
                    previous_node = current_node
                    current_node = current_node.next
            # If nothing was found
            return None


# Hash table can't have less than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Hash table length can not be smaller than specified values
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity

        # Create hash table with specified capacity
        self.hash_table = [None] * self.capacity
        # Keep Track of items to calculate load factor
        self.items_in_hash_table = 0

        # Set and point to a linked list at every index in hash table
        for n in range(self.capacity):
            self.hash_table[n] = LinkedList()

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """

        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.items_in_hash_table / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash_result = 5381
        key_bytes = key.encode()

        for byte in key_bytes:
            hashed_result = ((hash_result << 5) + hash_result) + byte

        return hashed_result

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # Resize hash table if load factor is above 0.7
        load_factor = self.get_load_factor()

        if load_factor > 0.7:
            self.resize(self.capacity * 2)

        # Hash key, get index
        hashed_idx = self.hash_index(key)
        # Check for existence of node with specified key
        node = self.hash_table[hashed_idx].get(key)

        # If node with specified key exists
        if node is not None:
            # Overwrite value of node with specified key
            node.value = value
        else:
            # Insert node to hash table at specified index
            self.hash_table[hashed_idx].add_to_head(key, value)
            # Increase counter
            self.items_in_hash_table += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Hash key, get index
        hashed_idx = self.hash_index(key)

        # Delete node from hash table
        node = self.hash_table[hashed_idx].delete(key)

        if node is None:
            print('Warning key not found')
        else:
            self.items_in_hash_table -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Hash key, get index
        hashed_idx = self.hash_index(key)

        # Get node with specified key at specified index
        node = self.hash_table[hashed_idx].get(key)

        # If node does not exist
        if node is None:
            return None

        # Eles return the nodes value
        return node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Refrence to current table
        old_table = self.hash_table
        # Make new array with 2X capcity
        new_hash_table = [None] * new_capacity

        # Point every index to linked list
        for n in range(new_capacity):
            new_hash_table[n] = LinkedList()

        # Overwrite existing hash table
        self.hash_table = new_hash_table
        # Overwrite existing capcaity to new capacity
        self.capacity = new_capacity
        # Re-set items in hash table
        self.items_in_hash_table = 0

        for idx in old_table:
            current_node = idx.head

            while current_node is not None:
                self.put(current_node.key, current_node.value)
                current_node = current_node.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
