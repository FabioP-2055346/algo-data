from utils.Node_class import Node
from utils.tree_build import TreeBuilder


def visit_node(node_label):
    global s
    s += node_label + ' '


def finish():
    global s
    print(s)
    s = ''


def pre_order_recursive(n: Node):
    visit_node(n.label)
    c: Node = n.left_child
    while c is not None:
        pre_order_recursive(c)
        c = c.right_sibling


def pre_order_iterative_no_stack(n: Node):
    visit_node(n.label)
    top: Node = n
    child: Node = n.left_child

    while True:
        if child is not None:
            visit_node(child.label)
            top = child
            child = child.left_child
        else:
            child = top.right_sibling
            top = top.parent
        if top is None:
            break


def pre_order_iterative_with_stack(n: Node):
    stack: list = []
    visit_node(n.label)
    stack.append(n)
    child: Node = n.left_child
    while True:
        if child is not None:
            visit_node(child.label)
            stack.append(child)
            child = child.left_child
        else:
            top_of_stack: Node = stack.pop()
            child = top_of_stack.right_sibling

        if len(stack) == 0:
            break


if __name__ == '__main__':
    s = ''
    root: Node = TreeBuilder().build_me_a_binary_tree()

    print("RECURSIVE")
    pre_order_recursive(root)
    finish()

    print('\nNO-STACK-ITERATIVE')
    pre_order_iterative_no_stack(root)
    finish()

    print('\nWITH-STACK-ITERATIVE')
    pre_order_iterative_with_stack(root)
    finish()
