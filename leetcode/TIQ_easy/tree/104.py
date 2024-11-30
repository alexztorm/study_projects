def maxDepth(root) -> int:
    max_depth, cur_depth = 0, 1
    nodes_stack = []
    cur_node = root

    while nodes_stack or cur_node:
        if cur_node:
            nodes_stack.append((cur_node, cur_depth))
            cur_node = cur_node.left
            cur_depth += 1
        elif nodes_stack:
            tmp = nodes_stack.pop()
            max_depth = max(max_depth, tmp[1])
            cur_node = tmp[0].right
            cur_depth = tmp[1] + 1

    return max_depth


def maxDepth2(self, root) -> int:
    if not root:
        return 0

    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
