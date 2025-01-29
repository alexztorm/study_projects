from leetcode.TIQ_easy.linked_list.listnode import ListNode, list_to_listnode, print_listnodes


def deleteMiddle(head: ListNode) -> ListNode:
    if not head.next:
        return None

    slow, fast = ListNode(0, next_node=head), head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    if slow.next:
        slow.next = slow.next.next
    else:
        slow.next = None

    return head


if __name__ == '__main__':
    print_listnodes(deleteMiddle(list_to_listnode([1, 3, 4, 7, 1, 2, 6])))
    print_listnodes(deleteMiddle(list_to_listnode([1, 2, 3, 4])))
    print_listnodes(deleteMiddle(list_to_listnode([2, 1])))
    print_listnodes(deleteMiddle(list_to_listnode([1])))
