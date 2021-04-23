class Node:
    """Node to store data"""

    def __init__(self, data=None, next_node=None):
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


class LinkedList:
    """Linked list to store data as list of nodes"""

    def __init__(self):
        """Linked list

        Example:
            >>> ll = LinkedList()
            >>> print(ll.head)
            None
            >>> print(ll.last_node)
            None
        """
        self.head = None
        self.last_node = None

    def print_ll(self):
        """Print entire linked list

        Example:
            >>> ll = LinkedList()
            >>> ll.print_ll()
            None
            <BLANKLINE>
        """
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f" {str(node.data)} ->"
            if node.next_node is None:
                ll_string += " None"
            node = node.next_node
        print(ll_string)

    def insert_beginning(self, data):
        """Insert node at beginning of the linked list

        Args:
            data ([type]): data to store in node

        Returns:
            bool: [description]

        Example:
            >>> ll = LinkedList()
            >>> ll.insert_beginning("Data 1")
            True
            >>> ll.insert_beginning("Data 2")
            True
            >>> ll.head.data
            'Data 2'
        """
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head

        new_node = Node(data, self.head)
        self.head = new_node
        return True

    def insert_at_end(self, data):
        """Insert node at the end of the linked list

        Args:
            data ([type]): data to store in node

        Returns:
            bool: [description]

        Example:
            >>> ll = LinkedList()
            >>> ll.insert_at_end("Data 1")
            True
            >>> ll.insert_at_end("Data 2")
            True
            >>> ll.head.data
            'Data 1'
            >>> ll.last_node.data
            'Data 2'
        """
        if self.head is None:
            self.insert_beginning(data)

        if self.last_node is None:
            node = self.head

            while node.next_node:
                node = node.next_node
            node.next_node = Node(data, None)
            self.last_node = node.next_node

        else:
            self.last_node.next_node = Node(data, None)
            self.last_node = self.last_node.next_node

        return True

    def to_list(self) -> "list":
        """return linked list as python list

        Returns:
            list[Any]: list containing data from nodes
        """
        lst = []
        if self.head is None:
            return lst

        node = self.head
        while node:
            lst.append(node.data)
            node = node.next_node
        return lst

    def get_user_by_id(self, user_id):
        """return user data stored in linked list by id

        Args:
            user_id (int): user id

        Returns:
            data: user data
        """
        node = self.head
        while node:
            if node.data["id"] == int(user_id):
                return node.data
            node = node.next_node
        return None
