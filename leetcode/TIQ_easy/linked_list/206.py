from listnode import ListNode, print_listnodes, list_to_listnode


def reverseList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    end = None

    while head is not None:
        new_node = ListNode(head.val, end)
        end = new_node
        head = head.next

    return end


print_listnodes(reverseList(list_to_listnode([1, 2, 3, 4, 5])))
print_listnodes(reverseList(list_to_listnode([1, 2])))
print_listnodes(reverseList(list_to_listnode([])))
