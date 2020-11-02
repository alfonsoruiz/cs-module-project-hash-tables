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

    # Return node with specified value
    # Runtime: O(n) n = length of linked list
    def find(self, key):
        current_node = self.head

        while current_node != None:
            if current_node.key == key:
                return current_node
            current_node = current_node.next

        return None

    # Delete node w/ specified value and return value
    # Runtime: O(n) n = length of linked list
    def delete(self, key):
        current_node = self.head
        prev = None

        # If value to be deleted is head on LL
        if current_node.key == key:
            self.head = current_node.next
            current_node.next = None
            return current_node

        while current_node != None:
            if current_node.key == key:
                prev.next = current_node.next
                current_node.next = None
                return current_node
            else:
                prev = current_node
                current_node = current_node.next

        return None

    # Runtime: O(1)
    def insert_head(self, node):
        node.next = self.head
        self.head = node

    # Runtime: O(n)
    def insert_head_or_overwrite(self, node):
        existing_node = self.find(node.value)

        if existing_node != None:
            existing_node.value = node.value
        else:
            self.insert_head(node)


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity

        self.hash_table = [LinkedList()] * self.capacity
        self.size = 0

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
        return self.size / self.capacity

    def djb2(self, key):
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
        load_factor = self.get_load_factor()

        if load_factor > 0.7:
            self.resize(self.capacity * 2)

        idx = self.hash_index(key)
        node = HashTableEntry(key, value)
        self.hash_table[idx].insert_head(node)
        self.size += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        idx = self.hash_index(key)
        node = self.hash_table[idx].delete(key)

        if node is None:
            print(f'Item with {key} not found in hashtable')
        else:
            self.size -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        idx = self.hash_index(key)
        node = self.hash_table[idx].find(key)

        if node is None:
            return None
        else:
            return node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """

        # old_table = self.hash_table
        # new_hash_table = [LinkedList()] * new_capacity
        # self.hash_table = new_hash_table
        # self.capacity = new_capacity
        # self.size = 0

        # # Re-hash all items in old hash table into new hash table
        # for idx in old_table:
        #     current_node = idx.head

        #     # Loop through LL Insert re-hashed item into new hash table
        #     while current_node is not None:
        #         self.put(current_node.key, current_node.value)
        #         current_node = current_node.next
        pass


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
