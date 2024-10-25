from listnode import ListNode, list_to_listnode, print_listnodes


def removeNthFromEnd(head: ListNode, n: int):
    count = 0
    node = head

    if node is None:
        return None

    while node is not None:
        count += 1
        node = node.next

    dummy = ListNode(0, head)
    node = dummy
    for i in range(count - n):
        node = node.next

    if node.next is None:
        return None
    elif node.next.next is None:
        node.next = None
    else:
        node.next = node.next.next

    return dummy.next


def removeNthFromEnd2(head: ListNode, n: int):
    dummy = ListNode(0, head)
    left, right = dummy, dummy
    distance = 0

    while right is not None:
        if distance <= n:
            right = right.next
            distance += 1
        else:
            right = right.next
            left = left.next

    if left.next is not None:
        left.next = left.next.next
    else:
        return None

    return dummy.next


print_listnodes(removeNthFromEnd2(list_to_listnode([1, 2, 3, 4, 5]), 2))
print_listnodes(removeNthFromEnd2(list_to_listnode([1]), 1))
print_listnodes(removeNthFromEnd2(list_to_listnode([1, 2]), 2))
