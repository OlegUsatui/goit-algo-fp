import matplotlib.pyplot as plt
import networkx as nx
import uuid

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1, visit_order=[], visit_type='inorder'):
    if node is not None:
        graph.add_node(node.id, label=node.val)
        node_index = visit_order.index(node.val)
        color_value = 255 - node_index * (255 // len(visit_order))
        graph.nodes[node.id]['color'] = f"#{color_value:02x}{color_value:02x}ff"

        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1, visit_order=visit_order, visit_type=visit_type)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1, visit_order=visit_order, visit_type=visit_type)
    return graph

def traverse_tree(node, order=[], method='inorder'):
    if node:
        if method == 'inorder':
            traverse_tree(node.left, order, method)
            order.append(node.val)
            traverse_tree(node.right, order, method)
        elif method == 'preorder':
            order.append(node.val)
            traverse_tree(node.left, order, method)
            traverse_tree(node.right, order, method)
        elif method == 'postorder':
            traverse_tree(node.left, order, method)
            traverse_tree(node.right, order, method)
            order.append(node.val)
        elif method == 'bfs':
            queue = [node]
            while queue:
                current = queue.pop(0)
                order.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
    return order

def draw_tree(tree_root, visit_order):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos, visit_order=visit_order)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Test
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

inorder_visit = traverse_tree(root, method='inorder')
preorder_visit = traverse_tree(root, method='preorder')
postorder_visit = traverse_tree(root, method='postorder')
bfs_visit = traverse_tree(root, method='bfs')

print("Inorder traversal:")
draw_tree(root, inorder_visit)
print("Preorder traversal:")
draw_tree(root, preorder_visit)
print("Postorder traversal:")
draw_tree(root, postorder_visit)
print("BFS traversal:")
draw_tree(root, bfs_visit)

