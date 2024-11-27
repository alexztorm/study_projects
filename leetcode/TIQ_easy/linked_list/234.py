from listnode import ListNode, list_to_listnode


def isPalindrome(head: ListNode) -> bool:
    if not head.next:
        return True

    listnode_list = []
    while head:
        listnode_list.append(head.val)
        head = head.next

    left, right = 0, len(listnode_list) - 1

    while left < right:
        if listnode_list[left] != listnode_list[right]:
            return False
        left += 1
        right -= 1

    return True


print(isPalindrome(list_to_listnode([1,2,2,1])))
print(isPalindrome(list_to_listnode([1,2])))
print(isPalindrome(list_to_listnode([1])))
print(isPalindrome(list_to_listnode([1, 1])))
print(isPalindrome(list_to_listnode([1, 2, 3, 1])))
