# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # res = []

        # q = collections.deque()
        # q.append(root)

        # while q:
        #     qLen = len(q)
        #     level = []

        #     for _ in range(qLen):
        #         node = q.popleft()

        #         if node:
        #             level.append(node.val)
        #             q.append(node.left)
        #             q.append(node.right)
            
        #     if level:
        #         res.append(level)

        
        # return res

        #if the tree is empty
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                # If the node has a left child, enqueue it to be processed in the next level.
                if node.left:
                    queue.append(node.left)
                
                # If the node has a right child, enqueue it as well.
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result
