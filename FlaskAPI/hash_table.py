class Node:
    """Node to store data"""

    def __init__(self, data=None, next_node=None) -> None:
        """create a Node datatype

        Args:
            data ([type], optional): data to store. Defaults to None.
            next_node ([type], optional): pointer to next Node. Defaults to None.

        Example:
            >>> node = Node("data", None)
            >>> node.data
            'data'
            >>> print(node.next_node)
            None
        """
        self.data = data
        self.next_node = next_node


class Data:
    """Store data as key, value pair"""

    def __init__(self, key, value) -> None:
        """Store data as key, value pair

        Args:
            key ([type]): key
            value ([type]): value

        Example:
            >>> d = Data("key", "val")
            >>> d.key
            'key'
            >>> d.value
            'val'
        """
        self.key = key
        self.value = value


class HashTable:
    """Hash Table to store data as key,value pairs"""

    def __init__(self, table_size) -> None:
        """Hashtable

        Args:
            table_size (int): size of the table

        Example:
            >>> ht = HashTable(10)
            >>> ht.hash_table
            [None, None, None, None, None, None, None, None, None, None]
        """
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        """calculate hash for the given key (hash_function)

        Args:
            key ([type]): given key

        Returns:
            [type]: hashed key

        Example:
            >>> ht = HashTable(5)
            >>> ht.custom_hash('key')
            1
        """
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            hash_value = (hash_value * ord(i)) % self.table_size
        return hash_value

    def add_key_value(self, key, value):
        """Adds key,value pair into `HashTable`

        Args:
            key ([type]): key to store
            value ([type]): value to store
        """
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            node = self.hash_table[hashed_key]
            while node.next_node:
                node = node.next_node
            node.next_node = Node(Data(key, value), None)

    def get_value(self, key):
        """Get value corresponde to the given `key`

        Args:
            key ([type]): given key

        Returns:
            Any: value for the given key
        """
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            if node.next_node is None:
                return node.data.value
            while node.next_node:
                if key == node.data.key:
                    return node.data.value
                node = node.next_node

            if key == node.data.key:
                return node.data.value

        return None

    def print_table(self):
        """Prints the whole `HashTable`"""
        print("{")
        for i, val in enumerate(self.hash_table):
            if val is not None:
                llist_string = ""
                node = val
                if node.next_node:
                    while node.next_node:
                        llist_string += (
                            str(node.data.key) + " : " +
                            str(node.data.value) + " --> "
                        )
                        node = node.next_node
                    llist_string += (
                        str(node.data.key) + " : " +
                        str(node.data.value) + " --> "
                    )
                    print(f"    [{i}] {llist_string}")
                else:
                    print(f"    [{i}] {val.data.key} : {val.data.value}")
            else:
                print(f"    [{i}] {val}")
        print("}")


if __name__ == "__main__":
    ht = HashTable(4)
    ht.add_key_value("hi", "there")
    ht.add_key_value("hii", "there")
    ht.add_key_value("hi", "there")
    ht.add_key_value("heyy", "there")
    ht.print_table()
