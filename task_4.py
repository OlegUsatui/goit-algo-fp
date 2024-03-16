import uuid
import networkx as nx
import matplotlib.pyplot as plt

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key, color="skyblue"):
        self.heap.append(Node(key, color))

    def heapify(self, idx=0):
        left = 2 * idx + 1
        right = 2 * idx + 2
        largest = idx

        if left < len(self.heap) and self.heap[left].val > self.heap[largest].val:
            largest = left

        if right < len(self.heap) and self.heap[right].val > self.heap[largest].val:
            largest = right

        if largest != idx:
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            self.heapify(largest)

    def build_heap(self):
        for i in range(len(self.heap)//2 - 1, -1, -1):
            self.heapify(i)

    def draw_heap(self):
        tree = nx.DiGraph()
        pos = {}
        for i, node in enumerate(self.heap):
            tree.add_node(node.id, color=node.color, label=node.val)
            if i != 0:  # Not the root node
                parent_idx = (i - 1) // 2
                tree.add_edge(self.heap[parent_idx].id, node.id)
            pos[node.id] = (i, -1 * int(i / 2))

        self._draw_tree(tree, pos)

    def _draw_tree(self, tree, pos):
        colors = [node[1]['color'] for node in tree.nodes(data=True)]
        labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

        plt.figure(figsize=(8, 5))
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
        plt.show()

class Node:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

# Test
heap = BinaryHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)
heap.insert(15)

heap.build_heap()
heap.draw_heap()
