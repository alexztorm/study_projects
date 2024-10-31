from listnode import ListNode, print_listnodes, list_to_listnode


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    start = ListNode(0)
    last = start

    while list1 is not None or list2 is not None:
        if list1 is None:
            last.next = list2
            return start.next
        elif list2 is None:
            last.next = list1
            return start.next
        else:
            if list1.val <= list2.val:
                last.next = list1
                last = last.next
                list1 = list1.next
            else:
                last.next = list2
                last = last.next
                list2 = list2.next

    return start.next


print_listnodes(mergeTwoLists(list_to_listnode([1, 2, 4]), list_to_listnode([1, 3, 4, 6])))
print_listnodes(mergeTwoLists(list_to_listnode([]), list_to_listnode([])))
print_listnodes(mergeTwoLists(list_to_listnode([]), list_to_listnode([0])))
