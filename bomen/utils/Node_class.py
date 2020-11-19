class Node:
    @property
    def label(self):
        return self.__label

    @property
    def left_child(self):
        return self.__left_child

    @left_child.setter
    def left_child(self, n):
        self.__left_child = n
        self.__left_child.parent = self

    @property
    def right_sibling(self):
        return self.__right_sibling

    @right_sibling.setter
    def right_sibling(self, n):
        self.__right_sibling = n
        self.__right_sibling.parent = self.parent

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, n):
        self.__parent = n

    def __init__(self, label):
        self.__label = label
        self.__left_child: Node = None
        self.__right_sibling: Node = None
        self.__parent: Node = None

    def add_child(self, n):
        if self.__left_child is None:
            self.__left_child = n
