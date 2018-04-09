class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        self.root = None
        self.size = 0

    def _last(self):
        if not self.root:
            return None

        current = self.root
        while current.next:
            current = current.next

        return current

    def add(self, data):
        node = Node(data)
        self.size += 1
        if not self.root:
            self.root = node
            return

        last = self._last()
        last.next = node

    def reverse(self):
        if self.size in (0, 1):  # nothing to reverse
            return

        current = self.root
        while current.next:
            next_node = current.next  # save onto the one in front

        pass


ll = LinkedList()
