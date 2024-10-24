from listnode import ListNode


def deleteNode(node: ListNode):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    while node.next.next is not None:
        node.val = node.next.val
        node = node.next

    node.val = node.next.val
    node.next = None


def deleteNode2(node: ListNode):
    node.val, node.next = node.next.val, node.next.next
