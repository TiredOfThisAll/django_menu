def down(node, visitor=None, allowed_nodes=None):
    if not visitor:
        return
    def helper(node, visitor, allowed_nodes):
        if not node:
            return
        if allowed_nodes is not None and node not in allowed_nodes:
            return
        visitor(node)

        for child in node.children:
            helper(child, visitor, allowed_nodes)
    helper(node, visitor, allowed_nodes)


def up(node, visitor=None, allowed_nodes=None):
    if not visitor:
        return
    def helper(node, visitor, allowed_nodes):
        if not node:
            return
        if allowed_nodes is not None and node not in allowed_nodes:
            return
        visitor(node)
        helper(node.parent, visitor, allowed_nodes)
    helper(node, visitor, allowed_nodes)


def all(node, visitor=None, allowed_nodes=None):
    if not visitor:
        return
    if allowed_nodes is None:
        allowed_nodes = set(node.tree.ids_dict.values())
    def helper(node, visitor, allowed_nodes):
        if not node:
            return
        
        if allowed_nodes is not None:
            if node not in allowed_nodes:
                return
            allowed_nodes.remove(node)

        visitor(node)        
        for child in node.children:
            helper(child, visitor, allowed_nodes)
        helper(node.parent, visitor, allowed_nodes)
    helper(node, visitor, allowed_nodes.copy() if allowed_nodes else None)
