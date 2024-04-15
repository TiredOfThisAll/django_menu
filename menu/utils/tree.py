import menu.utils.functors as functors
import menu.utils.tree_traverse as tree_traverse


class Node:
    def __init__(self, value, parent, children, depth, tree) -> None:
        self.value = value
        self.parent = parent
        self.children = children
        self.depth = depth
        self.tree = tree
    
    def __str__(self):
        return f"value: {self.value}, parent: {self.parent}, children: {self.children}, depth:{self.depth}"


class Tree:
    def __init__(self, items) -> None:
        Tree.build_lookup_tables(self, items)
        Tree.build_relations(self)
        Tree.remove_fallen_leaves(self)
        Tree.remove_loops(self)
    
    def build_lookup_tables(self, items):
        self.ids_dict = {}
        self.parent_ids_dict = {}

        self.root = Node(None, None, [], 0, self)
        self.ids_dict[None] = self.root

        for item in items:
            node = Node(item, None, [], None, self)
            self.ids_dict[item.id] = node
            parent_id = item.get_parent_id()
            if parent_id not in self.parent_ids_dict:
                self.parent_ids_dict[parent_id] = [node]
            else:
                self.parent_ids_dict[parent_id].append(node)

    def build_relations(self):
        parent_ids_to_check = [None]

        while parent_ids_to_check:
            parent_id = parent_ids_to_check.pop()
            if parent_id not in self.ids_dict:
                continue
            parent = self.ids_dict[parent_id]
            if parent_id not in self.parent_ids_dict:
                continue
            children = self.parent_ids_dict[parent_id]
            child_depth = parent.depth + 1
            for child in children:
                if not child:
                    continue
                parent_ids_to_check.append(child.value.id)
                child.parent = parent
                parent.children.append(child)
                child.depth = child_depth

    def remove_fallen_leaves(self):
        ids_to_pop = set([])
        parent_ids_to_pop = set([])
        for parent_id, nodes in self.parent_ids_dict.items():
            if parent_id in self.ids_dict:
                continue
            for node in nodes:
                if not node:
                    continue
                ids_to_pop.add(node.value.id)
            parent_ids_to_pop.add(parent_id)
        
        for id in ids_to_pop:
            self.ids_dict.pop(id)
        for parent_id in parent_ids_to_pop:
            self.parent_ids_dict.pop(parent_id)

    def remove_loops(self):
        ids_to_pop = set([])
        for id, node in self.ids_dict.items():
            if not node:
                continue
            if node.depth is not None:
                continue
            ids_to_pop.add(id)
        for id in ids_to_pop:
            self.ids_dict.pop(id)
            self.parent_ids_dict.pop(id)

    def get_visible_nodes(self, selected_node):
        visible_nodes = set(selected_node.children)
        visible_nodes.add(selected_node)
        return visible_nodes


def find_root(node):
    if not node:
        return None
    while node.parent:
        node = node.parent
    return node


def tree_string(node, visitor=None, tabs=1):
    if not visitor:
        visitor = functors.NodeStringBuilder(tabs)
    tree_traverse.down(node, visitor)
    return visitor.result()


def tree_string_reverse(node, visitor=None, tabs=1):
    if not visitor:
        visitor = functors.NodeStringBuilder(tabs)
    tree_traverse.up(node, visitor)
    return visitor.result()


def tree_string_visible_from_root(tree, node, visitor=None, tabs=1, expand_above=False):
    if not visitor:
        visitor = functors.HTMLBuilder()
    visible_set = tree_visible_set(tree, node)
    if expand_above:
        visible_set.update(tree_above_set(tree, node))
    tree_traverse.all(tree.root, visitor, visible_set)
    return visitor.result()


def tree_visible_set(tree, node, visitor=None):
    visitor = functors.NodeChildrenSetBuilder()
    tree_traverse.up(node, visitor)
    visible_set = visitor.result()
    visible_set.add(tree.root)
    return visible_set


def tree_above_set(tree, node, visitor=None):
    if node.tree != tree:
        return set([])
    if not visitor:
        visitor = functors.NodeAboveSetBuilder(node)
    tree_traverse.all(tree.root, visitor)
    return visitor.result()
