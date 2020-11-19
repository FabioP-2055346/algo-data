from utils.Node_class import Node
from utils.tree_build import TreeBuilder


def visit_node(node_label):
    global s
    s += node_label + ' '


def finish():
    global s
    print(s)
    s = ''


def in_order_recursive(n: Node):
    child: Node = n.left_child
    while child is not None:
        in_order_recursive(child)
        visit_node(child.label)
        child = child.right_sibling


def in_order_iterative_no_stack(n: Node):
    top: Node = n
    child: Node = n.left_child
    while True:
        if child is not None:
        else:
            child = top.right_sibling
            break


def in_order_iterative_with_stack(n: Node):
    pass


if __name__ == '__main__':
    s = ''
    root: Node = TreeBuilder().build_me_a_binary_tree()

    print("RECURSIVE")
    in_order_recursive(root)
    finish()

    print('\nNO-STACK-ITERATIVE')
    in_order_iterative_no_stack(root)
    finish()

    print('\nWITH-STACK-ITERATIVE')
    in_order_iterative_with_stack(root)
    finish()
