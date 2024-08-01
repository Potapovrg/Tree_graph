from anytree import Node, RenderTree
from anytree.exporter import DotExporter

def create_structural_scheme():
    # Create nodes with quantities
    root = Node(("Root", 1))
    branch1 = Node(("Branch 1", 2), parent=root)
    branch2 = Node(("Branch 2", 3), parent=root)
    leaf1 = Node(("Leaf 1", 4), parent=branch1)
    leaf2 = Node(("Leaf 2", 5), parent=branch1)
    leaf3 = Node(("Leaf 3", 6), parent=branch2)
    leaf4 = Node(("Leaf 4", 7), parent=branch2)
    leaf4 = Node(("Leaf 4", 7), parent=branch1)

    # Print tree structure to console
    for pre, _, node in RenderTree(root):
        print(f"{pre}{node.name[0]} (Quantity: {node.name[1]})")

    # Custom node naming for DOT export
    def nodenamefunc(node):
        return f'"{node.name[0]}\\nQuantity: {node.name[1]}"'

    # Export to DOT format with custom node naming
    DotExporter(root, nodenamefunc=nodenamefunc).to_dotfile("tree_structure.dot")
    print("DOT file saved as tree_structure.dot")

# Create the structural scheme
create_structural_scheme()