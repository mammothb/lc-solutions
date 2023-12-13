from typing import List, Optional


class TreeNode:
    def __init__(self, val=0):
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None
        self.val = val


def create_tree_from_list(array: List[Optional[int]]) -> Optional[TreeNode]:
    if not array:
        return None

    def build_tree(array: List[Optional[int]], index: int) -> Optional[TreeNode]:
        if index >= len(array) or array[index] is None:
            return None
        node = TreeNode(array[index])
        node.left = build_tree(array, 2 * index + 1)
        node.right = build_tree(array, 2 * index + 2)
        return node

    return build_tree(array, 0)


def print_tree(root: Optional[TreeNode], depth: int = 0) -> None:
    r"""Given a tree:
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
    Print:
            7
        3
            6
    1
            5
        2
            4
    """
    if root is None:
        return
    print_tree(root.right, depth + 1)
    print(f"{'    ' * depth}{root.val}")
    print_tree(root.left, depth + 1)


##########
# Traversals
##########


def inorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    def traverse(node, result):
        if node.left is not None:
            traverse(node.left, result)
        result.append(node.val)
        if node.right is not None:
            traverse(node.right, result)

    result = []
    traverse(root, result)
    return result


def inorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = []
    while stack or root is not None:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.val)
        root = root.right
    return result


def preorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    def traverse(node, result):
        result.append(node.val)
        if node.left is not None:
            traverse(node.left, result)
        if node.right is not None:
            traverse(node.right, result)

    result = []
    traverse(root, result)
    return result


def preorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = [root]
    while stack:
        root = stack.pop()
        result.append(root.val)
        if root.right is not None:
            stack.append(root.right)
        if root.left is not None:
            stack.append(root.left)
    return result


def postorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    def traverse(node, result):
        if node.left is not None:
            traverse(node.left, result)
        if node.right is not None:
            traverse(node.right, result)
        result.append(node.val)

    result = []
    traverse(root, result)
    return result


def postorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = []
    while stack or root is not None:
        while root is not None:
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
            root = root.left
        root = stack.pop()
        # The current node has an unprocessed right child
        if root.right is not None and (stack and stack[-1] == root.right):
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            result.append(root.val)
            root = None
    return result


def validate_bst(root: Optional[TreeNode]) -> bool:
    # Check via inorder traversal, it should be strictly ascending
    curr = None
    stack = []
    while stack or root is not None:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if curr is not None and curr >= root.val:
            return False
        curr = root.val
        root = root.right
    return True


def insert_into_bst_recursive(
    root: Optional[TreeNode], value: int
) -> Optional[TreeNode]:
    if root is None:
        return TreeNode(value)
    if root.val == value:
        return root
    if root.val < value:
        root.right = insert_into_bst_recursive(root.right, value)
    else:
        root.left = insert_into_bst_recursive(root.left, value)
    return root


def insert_into_bst_iterative(
    root: Optional[TreeNode], value: int
) -> Optional[TreeNode]:
    new_node = TreeNode(value)
    if root is None:
        return new_node
    node = root
    while True:
        if node.val == value:
            break
        if node.val < value:
            if node.right is None:
                node.right = new_node
                break
            node = node.right
        else:
            if node.left is None:
                node.left = new_node
                break
            node = node.left

    return root


def delete_from_bst_recursive(
    root: Optional[TreeNode], value: int
) -> Optional[TreeNode]:
    if root is None:
        return None
    if root.val < value:
        root.right = delete_from_bst_recursive(root.right, value)
        return root
    if root.val > value:
        root.left = delete_from_bst_recursive(root.left, value)
        return root

    # Have to delete root node
    if root.left is None:
        new_root = root.right
        del root
        return new_root
    if root.right is None:
        new_root = root.left
        del root
        return new_root

    # Both children exist
    parent = root
    curr = parent.right
    while curr.left is not None:
        parent = curr
        curr = curr.left
    root.val, curr.val = curr.val, root.val
    if parent == root:
        parent.right = curr.right
    else:
        parent.left = curr.right
    del curr
    return root


def count_tree_nodes_recursive(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return (
        1
        + count_tree_nodes_recursive(root.left)
        + count_tree_nodes_recursive(root.right)
    )


def count_tree_nodes_iterative(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    stack = [root]
    count = 0
    while stack:
        root = stack.pop()
        if root.left is not None:
            stack.append(root.left)
        if root.right is not None:
            stack.append(root.right)
        count += 1
    return count


def is_in_bst_recursive(root: Optional[TreeNode], value: int) -> bool:
    if root is None:
        return False
    if root.val == value:
        return True
    if root.val < value:
        return is_in_bst_recursive(root.right, value)
    return is_in_bst_recursive(root.left, value)


def is_in_bst_iterative(root: Optional[TreeNode], value: int) -> bool:
    if root is None:
        return False
    stack = [root]
    while stack:
        root = stack.pop()
        if root.val == value:
            return True
        if root.val < value and root.right is not None:
            stack.append(root.right)
        if root.val > value and root.left is not None:
            stack.append(root.left)
    return False


def get_height_recursive(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    l_height = 0 if root.left is None else get_height_recursive(root.left)
    r_height = 0 if root.right is None else get_height_recursive(root.right)
    return 1 + max(l_height, r_height)


def get_min(root: Optional[TreeNode]) -> int:
    if root is None:
        return -1
    while root.left is not None:
        root = root.left
    return root.val


def get_max(root: Optional[TreeNode]) -> int:
    if root is None:
        return -1
    while root.right is not None:
        root = root.right
    return root.val


if __name__ == "__main__":
    #  root = create_tree_from_list([0, 1, 2, 3, None, None, 6])
    root = create_tree_from_list(list(range(1, 8)))
    print_tree(root)
    print(inorder_traversal_recursive(root))
    print(inorder_traversal_iterative(root))
    print(preorder_traversal_recursive(root))
    print(preorder_traversal_iterative(root))
    print(postorder_traversal_recursive(root))
    print(postorder_traversal_iterative(root))

    bst_root = create_tree_from_list([100, 20, 500, 10, 30])
    print_tree(bst_root)
    print(validate_bst(root))
    print(validate_bst(bst_root))
    bst_root = insert_into_bst_recursive(bst_root, 15)
    bst_root = insert_into_bst_iterative(bst_root, 8)
    print_tree(bst_root)
    bst_root = delete_from_bst_recursive(bst_root, 30)
    print_tree(bst_root)
    print(count_tree_nodes_recursive(bst_root))
    print(count_tree_nodes_iterative(bst_root))
    print(is_in_bst_recursive(bst_root, 15))
    print(is_in_bst_recursive(bst_root, 16))
    print(is_in_bst_iterative(bst_root, 15))
    print(is_in_bst_iterative(bst_root, 16))
    print(get_height_recursive(bst_root))
    print(get_min(bst_root))
    print(get_max(bst_root))
