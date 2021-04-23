class Node:
    def __init__(self, data=None, next_node=None) -> None:
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self) -> None:
        """Queue Data Structure"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """Insert data into `Queue`

        Args:
            data (Any): data to be inserted

        Example:
            >>> q = Queue()
            >>> q.enqueue(1)
            >>> q.enqueue(2)
            >>> q.head.data
            1
            >>> q.tail.data
            2
        """
        if self.tail is None and self.head is None:
            self.tail = self.head = Node(data, None)
            return
        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node
        return

    def dequeue(self):
        """remove data from `Queue`

        Returns:
            Any: Queue data

        Example:
            >>> q = Queue()
            >>> q.enqueue(1)
            >>> q.enqueue(2)
            >>> q.dequeue().data
            1
        """
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        return removed
