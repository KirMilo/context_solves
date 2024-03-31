from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


# left root right
def get_result(node: Optional["TreeNode"]):
    if not node.left:
        result.append(node.val)
    else:
        get_result(node.left)
        result.append(node.val)

    if node.right:
        get_result(node.right)


n = int(input().split()[0])
changes = map(int, input().split())

# Заполнение дерева
root = TreeNode(1)
root_root = TreeNode(val=0, left=root)
nodes = {0: root_root, 1: root}
parents = {1: 0}
key_node = 1

for i in range(2, n + 1):
    tree_node = TreeNode(val=i)
    nodes[i] = tree_node
    parents[i] = key_node

    if root.left:
        root.right = tree_node
        key_node += 1
        root = nodes[key_node]
    else:
        root.left = tree_node


# Изменения дерева
for node_val in changes:
    if not parents[node_val]:
        continue

    child = nodes.get(node_val)
    parent = nodes.get(parents.get(child.val))
    parent_parent = nodes.get(parents.get(parent.val))

    if parent_parent.left is parent:
        parent_parent.left = child
    else:
        parent_parent.right = child

    if parent.left is child:
        child.left, parent.left = parent, child.left
        if child.left.left:
            parents[child.left.left.val] = parent.val
    else:
        child.right, parent.right = parent, child.right
        if child.right.right:
            parents[child.right.right.val] = parent.val

    parents[child.val] = parent_parent.val
    parents[parent.val] = child.val


result = []
get_result(nodes[0].left)
print(*result)
