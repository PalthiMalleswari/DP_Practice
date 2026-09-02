#Problem - https://leetcode.com/problems/house-robber-iii/

#==================== BF ==============


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        memo = {}
#======================== BF + Memorization ==========
        def dfs(node):

            if not node:
                return 0
            if node in memo:
                return memo[node]
            
            left,right = 0,0
            if node.left:
                left = dfs(node.left.left)+dfs(node.left.right)
            if node.right:
                right = dfs(node.right.left)+dfs(node.right.right)

            rob = left+right+node.val
            dont = dfs(node.left)+dfs(node.right)
            memo[node] = max(rob,dont) 
            return memo[node]

      Time Complexity - O(N) N - No.of Nodes
      Space Complexity - O(N)+O(N) - Hashmap+Recusive Stack Space

      #======================== Space Optimization ==============
        def dfs(node):
            if not node:
                return (0,0)
            # print(node.val)
            
            left = dfs(node.left)
            right = dfs(node.right)

            # Rob current node
            rob = node.val+left[1]+right[1]
            #Skip current node
            skip = max(left[0],left[1])+max(right[0],right[1])
            return (rob,skip)
        
        rob,skip = dfs(root)
        return max(rob,skip)

Time Complexity - O(N)
Space Complexity - O(N- Recursive Stack Space)
