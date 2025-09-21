from ds_v1.BinaryTree.BinaryTree import TreeNode

def diameter_of_binaryTree(root):
    max_diameter = 0

    def get_height(node):
        nonlocal max_diameter
        if not node:
            return -1

        left_height = get_height(node.left)
        right_height = get_height(node.right)
        
        current_diameter = left_height + right_height + 2
        max_diameter = max(max_diameter, current_diameter)
        
        return max(left_height, right_height) + 1

    get_height(root)
    return max_diameter
