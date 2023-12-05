import math

from binary_tree import TreeNode, print_tree


def rotate_l(grand_parent, parent):
    if parent is None:
        return
    if parent.right is None:
        return
    tmp = parent
    parent = parent.right
    tmp.right = parent.left
    parent.left = tmp
    grand_parent.right = parent


def rotate_r(grand_parent, parent):
    if parent is None:
        return
    if parent.left is None:
        return
    tmp = parent
    parent = parent.left
    tmp.left = parent.right
    parent.right = tmp
    grand_parent.right = parent


def convert_bst_to_vine(grand_parent):
    count = 0
    parent = grand_parent.right
    while parent is not None:
        while parent.left is not None:
            rotate_r(grand_parent, parent)
            parent = grand_parent.right
        grand_parent = parent
        parent = parent.right
        count += 1
    return count


def dsw(root):
    # Node to track the root
    grand_parent = TreeNode()
    grand_parent.right = root

    num_nodes = convert_bst_to_vine(grand_parent)

    # Number of fully filled height
    height = int(math.log2(num_nodes + 1))
    # Number of nodes in fully filled heights
    m = 2**height - 1
    grand_tracker = grand_parent
    parent = grand_tracker.right
    # Left rotate excess nodes on odd nodes
    for _ in range(num_nodes - m):
        rotate_l(grand_tracker, parent)
        grand_tracker = grand_tracker.right
        parent = grand_tracker.right

    while m > 1:
        m //= 2
        grand_tracker = grand_parent
        parent = grand_tracker.right
        # Left rotate on odd nodes
        for _ in range(m):
            rotate_l(grand_tracker, parent)
            grand_tracker = grand_tracker.right
            parent = grand_tracker.right
    return grand_parent.right


if __name__ == "__main__":
    tree_node = TreeNode(1)
    # Dummy node to track the root
    grand = TreeNode()
    grand.right = tree_node
    for i in range(20):
        tree_node.left = TreeNode(2 + i)
        tree_node = tree_node.left

    print_tree(grand)
    print("-")
    grand.right = dsw(grand.right)
    print_tree(grand)
    print("-")
