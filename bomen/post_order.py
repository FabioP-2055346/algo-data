from utils.Node_class import Node
from utils.tree_build import TreeBuilder


def visit_node(node_label):
    global s
    s += node_label + ' '


def finish():
    global s
    print(s)
    s = ''


def post_order_recursive(n: Node):
    child: Node = n.left_child
    while child is not None:
        post_order_recursive(child)
        child = child.right_sibling  # als bereikt wordt --> geen child meer over
    # als bereikt wordt --> geen children meer over, zowel links als rechts van de huidige knoop 'n' !
    visit_node(n.label)  # dus we gaan deze huidige knoop nooit meer passeren, dus visit het label van de knoop!


def post_order_iterative_no_stack(n: Node):
    top: Node = n
    child: Node = n.left_child
    while True:
        if child is not None:
            top = child
            child = child.left_child
        else:
            child = top.right_sibling
            visit_node(top.label)
            top = top.parent
        if top is None:
            break


def post_order_iterative_with_stack(n: Node):
    stack: list = []
    child: Node = n.left_child
    stack.append(n)

    while len(stack) > 0:
        if child is not None:
            stack.append(child)
            child = child.left_child
        else:
            top: Node = stack.pop()
            visit_node(top.label)
            child = top.right_sibling


if __name__ == '__main__':
    s = ''
    root: Node = TreeBuilder().build_me_a_binary_tree()

    print("RECURSIVE")
    post_order_recursive(root)
    finish()

    print('\nNO-STACK-ITERATIVE')
    post_order_iterative_no_stack(root)
    finish()

    print('\nWITH-STACK-ITERATIVE')
    post_order_iterative_with_stack(root)
    finish()
