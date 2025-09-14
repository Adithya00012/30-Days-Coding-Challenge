def validate_bst(root):
    
    def is_valid(node, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.data < max_val):
            return False
        return (is_valid(node.left, min_val, node.data) and
                is_valid(node.right, node.data, max_val))
    return is_valid(root, float('-inf'), float('inf'))
