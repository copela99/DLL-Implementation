"""
Austin Copeland
DLL.py
"""

from typing import TypeVar, List

# for more information on typehinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)


# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


class Node:
    """
    Implementation of a doubly linked list node.
    Do not modify.
    """
    __slots__ = ["value", "next", "prev"]

    def __init__(self, value: T, next: Node = None, prev: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        """
        self.next = next
        self.prev = prev
        self.value = value

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        return repr(self)

    # MODIFY BELOW #

    def empty(self) -> bool:
        """
        Return boolean indicating whether DLL is empty.

        Required time & space complexity (respectively): O(1) & O(1).

        :return: True if DLL is empty, else False.
        """
        if self.size == 0:
            return True
        return False

    def push_back(self, val: T) -> None:
        """
        Function to add a node to the back of a linked list
        """
        new_node = Node(value=val)
        if self.empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1
        return

    def push_front(self, val: T) -> None:
        """
        Function to add a node to the front of a linked list
        """
        new_node = Node(value=val)
        if self.empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return

    def push(self, val: T, back: bool = True) -> None:
        """
        Create Node containing `val` and add to back (or front) of DLL. Increment size by one.

        Required time & space complexity (respectively): O(1) & O(1).

        Note: You might find it easier to implement this as a push_back and
            push_front function first.

        :param val: value to be added to the DLL.
        :param back: if True, add Node containing value to back (tail-end) of DLL;
            if False, add to front (head-end).
        :return: None.
        """
        if back:
            self.push_back(val)
            return
        self.push_front(val)
        return

    def pop(self, back: bool = True) -> None:
        """
        Remove Node from back (or front) of DLL. Decrement size by 1. If DLL is empty, do nothing.

        Required time & space complexity (respectively): O(1) & O(1).

        :param back: if True, remove Node from (tail-end) of DLL;
            if False, remove from front (head-end).
        :return: None.
        """
        if self.empty():
            return
        elif self.size == 1:
            self.head = self.tail = None
            self.size -= 1
            return
        if back:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        return

    def from_list(self, source: List[T]) -> None:
        """
        Construct DLL from a standard Python list.

        Required time & space complexity (respectively): O(n) & O(n).

        :param source: standard Python list from which to construct DLL.
        :return: None.
        """
        if len(source) == 0:
            return
        for i in range(len(source)):
            self.push(source[i])
        return

    def to_list(self) -> List[T]:
        """
        Construct standard Python list from DLL.

        Required time & space complexity (respectively): O(n) & O(n).

        :return: standard Python list containing values stored in DLL.
        """
        res = []
        if self.empty():
            return []
        node = self.head
        if self.size == 1:
            res.append(node.value)
            return res
        while node.next is not None:
            res.append(node.value)
            node = node.next
        res.append(node.value)
        return res

    def find(self, val: T) -> Node:
        """
        Find first instance of `val` in the DLL and return associated Node object.

        Required time & space complexity (respectively): O(n) & O(1).

        :param val: value to be found in DLL.
        :return: first Node object in DLL containing `val`.
            If `val` does not exist in DLL, return None.
        """
        node = self.head
        if self.empty():
            return None
        if self.size == 1:
            if self.head.value == val:
                return self.head
        while node.next is not None:
            if node.value == val:
                return node
            node = node.next
        if node.value == val:
            return node
        return None

    def find_all(self, val: T) -> List[Node]:
        """
        Find all instances of `val` in DLL and return Node objects in standard Python list.

        Required time & space complexity (respectively): O(n) & O(n).

        :param val: value to be searched for in DLL.
        :return: Python list of all Node objects in DLL containing `val`.
            If `val` does not exist in DLL, return empty list.
        """
        res = []
        node = self.head
        if self.empty():
            return res
        if self.size == 1:
            if self.head.value == val:
                res.append(node)
                return res
        while node.next is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        if node.value == val:
            res.append(node)
        return res

    def _remove_node(self, to_remove: Node) -> None:
        """
        Given a node in the linked list, remove it.
        Should only be called from within the DLL class.

        Required time & space complexity (respectively): O(1) & O(1).

        :param to_remove: node to be removed from the list
        :return: None
        """
        if self.empty():
            Exception('Trying to remove from an empty list')
            return
        if to_remove == self.head:
            self.pop(back=False)
            return
        if to_remove == self.tail:
            self.pop()
            return
        to_remove.prev.next = to_remove.next
        to_remove.next.prev = to_remove.prev
        to_remove.prev = None
        to_remove.next = None
        self.size -= 1
        return

    def delete(self, val: T) -> bool:
        """
        Delete first instance of `val` in the DLL. Must call _remove_node.

        Required time & space complexity (respectively): O(n) & O(1).

        :param val: value to be deleted from DLL.
        :return: True if Node containing `val` was deleted from DLL; else, False.
        """
        if self.empty():
            Exception('Tying to remove from an empty list')
            return False
        curr_node = self.head
        if self.size == 1:
            if curr_node.value == val:
                self._remove_node(curr_node)
                return True
        while curr_node.next is not None:
            if curr_node.value == val:
                self._remove_node(curr_node)
                return True
            curr_node = curr_node.next
        if curr_node == self.tail:
            if curr_node.value == val:
                self._remove_node(curr_node)
                return True
        return False

    def delete_all(self, val: T) -> int:
        """
        Delete all instances of `val` in the DLL. Must call _remove_node.

        Required time & space complexity (respectively): O(n) & O(1).

        :param val: value to be deleted from DLL.
        :return: integer indicating the number of Nodes containing `val` deleted from DLL;
                 if no Node containing `val` exists in DLL, return 0.
        """
        count = 0
        if self.empty():
            Exception('Tying to remove from an empty list')
            return 0
        curr_node = self.head
        if self.size == 1:
            if curr_node.value == val:
                self._remove_node(curr_node)
                count += 1
                return True
        while curr_node.next is not None:
            if curr_node.value == val:
                temp_node = curr_node
                curr_node = curr_node.next
                self._remove_node(temp_node)
                count += 1
                continue
            curr_node = curr_node.next
        if curr_node == self.tail:
            if curr_node.value == val:
                self._remove_node(curr_node)
                count += 1
        return count

    def reverse(self) -> None:
        """
        Reverse DLL in-place by modifying all `next` and `prev` references of Nodes in the
        DLL and resetting the `head` and `tail` references.
        Must be implemented in-place for full credit. May not create new Node objects.

        Required time & space complexity (respectively): O(n) & O(1).

        :return: None.
        """
        temp = None
        current = self.head
        self.tail = current
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.head = temp.prev


def flurricane(dll: DLL, delta: float) -> DLL:
    x_sum = num_x = 0
    res = DLL()
    if dll.empty():
        Exception('Empty DLL')
        return res
    if dll.size == 1:
        curr_node = dll.head
        res.push((curr_node.value[0], curr_node.value[1]))
        return res
    working_node = dll.tail
    node = dll.tail.prev
    t = working_node.value[0]
    interval = (t - delta, t)
    while node is not None:
        if interval[0] <= node.value[0] <= interval[1]:
            x_sum += node.value[1]
            num_x += 1
        if node == dll.head:
            x_sum += working_node.value[1]
            num_x += 1
            res.push((t, (float(x_sum / num_x) if num_x > 0 else working_node.value[1])))
            working_node = working_node.prev
            node = working_node.prev
            t = working_node.value[0]
            interval = (t - delta, t)
            x_sum = num_x = 0
            continue
        node = node.prev

    if working_node == dll.head:
        res.push((working_node.value[0], working_node.value[1]))
        res.reverse()
    return res
