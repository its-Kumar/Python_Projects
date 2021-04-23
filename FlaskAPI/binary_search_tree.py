class Node:
    def __init__(self, data=None) -> None:
        """Node to store data

        Args:
            data (Any, optional): Data to be added. Defaults to None.
        """
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        """BinarySearch Tree Data Structure"""
        self.root = None

    def _insert_recursive(self, data, node):
        if data["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        elif data["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)
        else:
            return

    def insert(self, data):
        """Insert data in `BinarySearchTree`

        Args:
            data (Any): Data to be added

        Example:
            >>> bst = BinarySearchTree()
            >>> bst.insert({"id" : 1})
            >>> bst.insert({"id" : 3})
            >>> bst.insert({"id" : 2})
            >>> bst.root.data
            {'id': 1}
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _search_recursive(self, blog_post_id, node):
        if node.left == None and node.right == None:
            return False
        if blog_post_id == node.data["id"]:
            return node.data

        if blog_post_id < node.data["id"] and node.left is not None:
            if blog_post_id == node.left.data["id"]:
                return node.left.data
            return self._search_recursive(blog_post_id, node.left)

        if blog_post_id > node.data["id"] and node.right is not None:
            if blog_post_id == node.right.data["id"]:
                return node.right.data
            return self._search_recursive(blog_post_id, node.right)
        return False

    def search(self, blog_post_id):
        """Search data in `BinarySearchTree`

        Args:
            blog_post_id (int): id to search

        Returns:
            Any: searched data

        Example:
            >>> bst = BinarySearchTree()
            >>> bst.insert({"id" : 1})
            >>> bst.insert({"id" : 3})
            >>> bst.insert({"id" : 2})
            >>> bst.search(3)
            {'id': 3}
            >>> bst.search(4)
            False
        """
        blog_post_id = int(blog_post_id)
        if self.root is None:
            return False
        return self._search_recursive(blog_post_id, self.root)
