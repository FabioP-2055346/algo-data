from utils.Node_class import Node


class TreeBuilder:
    def __init__(self):
        pass

    def build_me_a_binary_tree(self) -> Node:
        nodes: dict = self.__build_nodes()
        minus: Node = nodes.get('-')
        plus: Node = nodes.get('+')
        multiply: Node = nodes.get('*')
        one: Node = nodes.get('1')
        two: Node = nodes.get('2')
        three: Node = nodes.get('3')
        four: Node = nodes.get('4')

        minus.left_child = multiply

        multiply.right_sibling = four
        multiply.left_child = plus

        plus.right_sibling = three
        plus.left_child = one

        one.right_sibling = two

        return minus

    def __build_nodes(self) -> dict:
        return {'-': Node('-'), '*': Node('*'),
                '+': Node('+'), '1': Node('1'), '2': Node('2'),
                '3': Node('3'), '4': Node('4')}
