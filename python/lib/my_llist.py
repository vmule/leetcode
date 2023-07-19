class ListNode:
    """
    Linked List node definition.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    """
    Linked list python implementation.
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        _llist = []
        temp_pointer_node = self.head
        while temp_pointer_node:
            _llist.append(temp_pointer_node.val)
            temp_pointer_node = temp_pointer_node.next
        if len(_llist) > 0:
            return " ".join(str(i) for i in _llist)
        return "[]"

    def insert(self, val):
        newNode = ListNode(val)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
