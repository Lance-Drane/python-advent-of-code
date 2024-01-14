import re
import sys
from collections import Counter


class Node:
    def __init__(self, weight: int):
        self.weight = weight
        self.subnode_names: list[str] = []
        self.subnode_sums: list[int] = []
        self.total_weight = weight

    def are_subnodes_balanced(self) -> bool:
        return all(x == self.subnode_sums[0] for x in self.subnode_sums)


graph: dict[str, Node] = {}


# generic DFS function
def update_total_weight(node_key: str):
    node = graph[node_key]
    for idx, subnode_key in enumerate(node.subnode_names):
        update_total_weight(subnode_key)
        node.subnode_sums[idx] = graph[subnode_key].total_weight
    node.total_weight = node.weight + sum(node.subnode_sums)


# short-circuiting function which traverses one path up the tree until it finds a match
def find_unbalanced(node_key: str, change: int) -> int:
    node = graph[node_key]
    if node.are_subnodes_balanced():
        return node.weight + change
    commons = [c[0] for c in Counter(node.subnode_sums).most_common()]
    uncommon_idx = node.subnode_sums.index(commons[1])
    return find_unbalanced(node.subnode_names[uncommon_idx], commons[0] - commons[1])


seen_base = set()
seen_supported = set()

# initialize graph with node and subnode names
for line in sys.stdin.readlines():
    parts = re.findall(r'[\w]+', line)
    seen_base.add(parts[0])
    new_node = Node(int(parts[1]))
    if len(parts) > 2:
        for item in parts[2:]:
            seen_supported.add(item)
            new_node.subnode_names.append(item)
    graph[parts[0]] = new_node

# update graph nodes with subnode sums
for node in graph.values():
    node.subnode_sums = [graph[name].weight for name in node.subnode_names]

root_node_key = next(iter(seen_base - seen_supported))

# compute total weight for all nodes
update_total_weight(root_node_key)

# find the unusual weight
print(find_unbalanced(root_node_key, 0))
