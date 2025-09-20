import collections
from ds_v1.BinaryTree.BinaryTree import TreeNode

def compute_heights(root):
    heights = {}
    depths = {}
    level_nodes = collections.defaultdict(list)

    def dfs(node, depth):
        if not node:
            return -1  
        depths[node.data] = depth
        left_h = dfs(node.left, depth + 1)
        right_h = dfs(node.right, depth + 1)
        h = 1 + max(left_h, right_h)
        heights[node.data] = h
        level_nodes[depth].append((h, node.data))
        return h

    dfs(root, 0)
    return heights, depths, level_nodes


def heights_after_queries(root, queries):
    heights, depths, level_nodes = compute_heights(root)
    best_two = {}
    for depth, arr in level_nodes.items():
        arr.sort(reverse=True)  
        best_two[depth] = arr[:2]  

    results = []
    for q in queries:
        depth = depths[q]
        if best_two[depth][0][1] != q:
            max_other = best_two[depth][0][0]
        elif len(best_two[depth]) > 1:
            max_other = best_two[depth][1][0]
        else:
            max_other = -1 
        results.append(depth + max_other)

    return results
