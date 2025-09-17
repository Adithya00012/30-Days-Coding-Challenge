def is_symmetric(root):
    def is_mirror(node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        
        return (node1.data == node2.data and
                is_mirror(node1.left, node2.right) and
                is_mirror(node1.right, node2.left))

    return is_mirror(root, root)
