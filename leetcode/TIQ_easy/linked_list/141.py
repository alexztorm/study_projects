from listnode import ListNode, list_to_listnode


def hasCycle(self, head: ListNode) -> bool:
    if not head or not head.next:
        return False

    dummy = ListNode(0)

    prev, cur = head, head.next
    prev.next = dummy
    while cur.next:
        if cur.next == dummy:
            return True
        prev = cur
        cur = cur.next
        prev.next = dummy

    return False

