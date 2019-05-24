import math

"""
File: linkedbst.py
Author: Ken Lambert
"""
from abstractcollection import AbstractCollection
from bstnode import BSTNode
from linkedstack import LinkedStack



class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s

        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self._root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right != None:
                    stack.push(node.right)
                if node.left != None:
                    stack.push(node.left)

    def num_of_node(self):
        '''
        Countes the number of nodes
        :return: int
        '''
        num = 0
        for el in self:
            num += 1
        return num

    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        lyst = list()
        for el in self:
            lyst.append(el)
        return lyst

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        inorder_lyst = list()

        def recurse(node):
            if node != None:
                recurse(node.left)
                inorder_lyst.append(node.data)
                recurse(node.right)

        recurse(self._root)
        return iter(inorder_lyst)

    def create_inordered_list(self):
        """
        Creates a list of inordered nodes.
        :return: list
        """
        inorder_lyst = list()
        for el in self.inorder():
            inorder_lyst.append(el)
        return inorder_lyst

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        if p:
            for c in [p.left, p.right]:  # for each child c
                for other in self._subtree_postorder(c):  # do postorder of c's subtree
                    yield other  # yielding each to our caller
            yield p

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        if not self.isEmpty():
            for p in self._subtree_postorder(self._root):  # start recursion
                yield p.data

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        # Base Case
        if self._root is None:
            return
        # Create an empty queue for level order traversal
        queue = []
        # Enqueue Root and initialize height
        queue.append(self._root)
        while (len(queue) > 0):
            # Print front of queue and remove it from queue
            yield queue[0].data
            node = queue.pop(0)
            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)
                # Enqueue right child
            if node.right is not None:
                queue.append(node.right)

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) != None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""

        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

        return recurse(self._root)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None
        self._size = 0

    def isEmpty(self):
        '''
        Returns True if the tree is empty.
        :return: bool
        '''
        return self._root == None and self._size == 0

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item's position
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal,
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
                # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self._root)
        self._size += 1

    def remove(self, item):
        """Precondition: 3item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree.""")

        # Helper function to adjust placement of an item
        def liftMaxInLeftSubtreeToTop(top):
            # Replace top's datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top's left subtree
            #       has been removed
            # Post: top.data = maximum value in top's left subtree
            parent = top
            currentNode = top.left
            while not currentNode.right == None:
                parent = currentNode
                currentNode = currentNode.right
            top.data = currentNode.data
            if parent == top:
                top.left = currentNode.left
            else:
                parent.right = currentNode.left

        # Begin main part of the method
        if self.isEmpty():
            return None

        # Attempt to locate the node containing the item
        itemRemoved = None
        preRoot = BSTNode(None)
        preRoot.left = self._root
        parent = preRoot
        direction = 'L'
        currentNode = self._root
        while not currentNode == None:
            if currentNode.data == item:
                itemRemoved = currentNode.data
                break
            parent = currentNode
            if currentNode.data > item:
                direction = 'L'
                currentNode = currentNode.left
            else:
                direction = 'R'
                currentNode = currentNode.right

        # Return None if the item is absent
        if itemRemoved == None: return None

        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node's value with the maximum value in the
        #         left subtree
        #         Delete the maximium node in the left subtree
        if not currentNode.left == None \
                and not currentNode.right == None:
            liftMaxInLeftSubtreeToTop(currentNode)
        else:

            # Case 2: The node has no left child
            if currentNode.left == None:
                newChild = currentNode.right

                # Case 3: The node has no right child
            else:
                newChild = currentNode.left

                # Case 2 & 3: Tie the parent to the new child
            if direction == 'L':
                parent.left = newChild
            else:
                parent.right = newChild

        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection's size counter
        #            Return the item
        self._size -= 1
        if self.isEmpty():
            self._root = None
        else:
            self._root = preRoot.left
        return itemRemoved

    def replace(self, item, newItem):
        """
        If item is in self, replaces it with newItem and
        returns the old item, or returns None otherwise."""
        probe = self._root
        while probe != None:
            if probe.data == item:
                oldData = probe.data
                probe.data = newItem
                return oldData
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    def height(self):
        '''
        Finds the height of the tree
        :return: int
        '''

        def height1(top):
            if top is None:
                top = self._root
            if top.left and top.right:
                return 1 + max(height1(c) for c in [top.left, top.right])
            elif top.left:
                return height1(top.left) + 1
            elif top.right:
                return height1(top.right) + 1
            return 1

        return height1(None)

    def isBalanced(self):
        '''
        Return True if tree is balanced
        :return:bool
        '''
        return self.height() < 1.44 * math.log((self.num_of_node()), 2)

    def rangeFind(self, low, high):
        '''
        Returns a list of the items in the tree, where low <= item <= high."""
        :param low:int
        :param high:int
        :return:list
        '''
        range_lst = []
        for el in self.create_inordered_list():
            if low <= el <= high:
                range_lst.append(el)
        return range_lst

    def rebalance(self):
        '''
        Rebalances the tree.
        :return:None
        '''
        inordered_list = self.create_inordered_list()
        self.clear()

        def recurse(lst=inordered_list):
            if len(lst):
                lyy = [lst[:len(lst) // 2], lst[(len(lst) // 2) + 1:]]
                for el in lyy:
                    if el:
                        self.add(el[len(el) // 2])
                        if len(el) != 1:
                            recurse(el)

        self.add(inordered_list[len(inordered_list) // 2])
        recurse()

    def successor(self, item):
        """
        Returns the smallest item that is larger than
        item, or None if there is no such item.
        :param item:element of an inordered_list
        :type item:int or str
        :return:element of an inordered_list
        :rtype:int or str
        """
        for el in self.create_inordered_list():
            if el > item:
                return el

    def predecessor(self, item):
        """
        Returns the largest item that is smaller than
        item, or None if there is no such item.
        :param item:element of an inordered_list
        :type item:int or str
        :return:element of an inordered_list
        :rtype:int or str
        """
        for el in self.create_inordered_list()[::-1]:
            if el < item:
                return el
