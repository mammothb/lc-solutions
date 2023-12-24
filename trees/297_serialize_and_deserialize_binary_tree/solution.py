import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = ""
        stack = [root]
        while stack:
            root = stack.pop()
            if root is None:
                result += ",#"
            else:
                result += f",{root.val}"
                stack.append(root.right)
                stack.append(root.left)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def build(values):
            self.idx += 1
            if values[self.idx] == "#":
                return None
            root = TreeNode(int(values[self.idx]))
            root.left = build(values)
            root.right = build(values)
            return root

        self.idx = 0
        return build(data.split(","))

    def deserialize2(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        stack = []
        n = len(data)
        root = None
        value = ""
        for i in range(1, n):
            if data[i] == ",":
                if value == "#":
                    node = None
                else:
                    node = TreeNode(int(value))
                if stack:
                    if stack[-1] is None:
                        stack.pop()
                        stack[-1].right = node
                        stack.pop()
                    else:
                        stack[-1].left = node
                # This will only be reached once because even after we start
                # building the right sub tree, the root.right node will be in
                # the stack
                else:
                    root = node
                stack.append(node)
                value = ""
            else:
                value += data[i]
        return root

    def serialize_bfs(self, root):
        result = ""
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                result += ",#"
            else:
                result += f",{node.val}"
                queue.append(node.left)
                queue.append(node.right)
        return result

    def deserialize_bfs(self, data):
        if data == "":
            return None

        values = data.split(",")
        if values[1] == "#":
            return None

        root = TreeNode(int(values[1]))
        queue = collections.deque([root])

        n = len(values)
        idx = 2
        while queue:
            node = queue.popleft()
            if values[idx] != "#":
                node.left = TreeNode(int(values[idx]))
                queue.append(node.left)
            if values[idx + 1] != "#":
                node.right = TreeNode(int(values[idx + 1]))
                queue.append(node.right)
            idx += 2
        return root


class CodecRecursive:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def solve(node, result):
            if node is None:
                result.append("#")
                return
            result.append(f"{node.val}")
            solve(node.left, result)
            solve(node.right, result)

        result = []
        solve(root, result)

        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def solve(data, n):
            if self.index == n:
                return
            if data[self.index] == "#":
                self.index += 1
                return None
            root = TreeNode(int(data[self.index]))
            self.index += 1
            root.left = solve(data, n)
            root.right = solve(data, n)
            return root

        data = data.split(",")
        self.index = 0
        return solve(data, len(data))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
