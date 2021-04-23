class Node:
    """Node to store data"""

    def __init__(self, data, next_node=None) -> None:
        """create a Node datatype

        Args:
            data ([type], optional): data to store.
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


class Stack:
    """Stack Data Structure"""

    def __init__(self) -> None:
        """Stack Data Structure"""
        self.top = None

    def peek(self):
        return self.top

    def push(self, data):
        """Insert data on top of `Stack`

        Args:
            data ([type]): data to be added

        Example:
            >>> s = Stack()
            >>> s.push("Data 1")
            >>> s.push("Data 2")
            >>> s.top.data
            'Data 2'
        """
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top

    def pop(self):
        """remove item from on top of `Stack`

        Returns:
            Any: data removed

        Example:
            >>> s = Stack()
            >>> s.push("Data 1")
            >>> s.push("Data 2")
            >>> s.pop().data
            'Data 2'

        """
        if self.top is None:
            return None
        removed = self.top
        self.top = self.top.next_node
        return removed
