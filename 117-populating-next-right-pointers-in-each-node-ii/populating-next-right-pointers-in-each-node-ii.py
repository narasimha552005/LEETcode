from collections import deque

class Solution:
    def connect(self, root):
        if not root:
            return root

        queue = deque([root])

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                # Connect to the next node at this level
                if i < size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root