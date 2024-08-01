from anytree import Node, RenderTree
from anytree.exporter import DotExporter

def create_structural_scheme():
    # Create nodes
    root = Node("Root")
    branch1 = Node("Branch 1", parent=root)
    branch2 = Node("Branch 2", parent=root)
    leaf1 = Node("Leaf 1", parent=branch1)
    leaf2 = Node("Leaf 2", parent=branch1)
    leaf3 = Node("Leaf 3", parent=branch2)
    leaf4 = Node("Leaf 4", parent=branch2)

    # Print tree structure to console
    for pre, _, node in RenderTree(root):
        print(f"{pre}{node.name}")

    # Export to DOT format
    DotExporter(root).to_dotfile("tree_structure.dot")
    print("DOT file saved as tree_structure.dot")

# Create the structural scheme
create_structural_scheme()