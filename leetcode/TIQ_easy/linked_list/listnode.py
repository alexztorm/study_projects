class ListNode:
    def __init__(self, x, next_node=None):
        self.val = x
        self.next = next_node


def list_to_listnode(vals: list) -> ListNode:
    new_node, next_node = None, None

    for i in range(len(vals) - 1, -1, -1):
        new_node = ListNode(vals[i], next_node)
        next_node = new_node

    return new_node


def listnode_to_list(head: ListNode) -> list:
    output = []

    while head is not None:
        output.append(head.val)
        head = head.next

    return output


def print_listnodes(head: ListNode) -> None:
    print(listnode_to_list(head))
