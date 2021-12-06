from typing import Any, List, Callable, Union
from anytree import Node, RenderTree
import treelib


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# # # # # # # # # # # # # # # # # # # # # # # LINKED LIST  # # # # # # # # # # # # # # # # # # # # # # #


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node

    def node(self, at: int) -> Node:
        temp = self.head
        if temp is None:
            return None
        for i in range(at):
            temp = temp.next
        return temp

    def insert(self, data: Any, after: Node) -> None:
        if after is None:
            print("There is no such node in this linkedList")
            return None
        new_node = Node(data)
        if after == self.tail:
            after.next = new_node
            self.tail = new_node
        new_node.next = after.next
        after.next = new_node

    def pop(self) -> Any:
        if self.head == 0:
            return 0
        removed = self.head
        removed.data = self.head.data
        self.head = self.head.next
        return removed.data

    def remove_last(self) -> Any:
        if self.head == 0:
            return 0
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        self.tail = temp
        temp.next = None  # ustawienie nastepnika na 0, koniec listy
        return temp.data

    def remove(self, after: Node) -> None:
        if after is None:
            print("There is no such node in this linkedList")
            return None
        else:
            self.tail = after
            after.next = None

    def __str__(self) -> str:  # OVERRIDE - przesloniecie(nadpisanie) metody domyslnej
        temp = self.head
        temp_list = ""
        if temp is None:
            print("List is empty")
        while temp is not None:
            if temp.next is not None:
                temp_list = temp_list + str(temp.data) + ' -> '  # do ogona dodaje strzalke
            else:
                temp_list = temp_list + str(temp.data)  # dla ogona nie dodaje strzalki
            temp = temp.next
        return temp_list

    def __len__(self) -> int:
        current = self.head
        sum_len = 0
        if current is None:
            return 0
        while current is not None:
            sum_len = sum_len + 1
            current = current.next
        return sum_len


# # # # # # # # # # # # # # # # # # # # # # # QUEUE  # # # # # # # # # # # # # # # # # # # # # # #


class Queue:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def peek(self) -> Any:
        if self._storage == 0:
            return 0
        return self._storage.head.data

    def enqueue(self, element: Any) -> None:
        return self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()

    def __len__(self) -> int:
        return len(self._storage)

    def __str__(self) -> str:
        temp_queue = ""
        if self._storage is None:
            print("Queue is empty")
        for i in range(len(self._storage)):
            if i == len(self._storage) - 1:
                temp_queue = temp_queue + str(self._storage.node(i).data)  # dla ostatniego elementu - brak przecinka
            else:
                temp_queue = temp_queue + str(self._storage.node(i).data) + ", "
        return temp_queue


# # # # # # # # # # # # # # # # # # # # # # # BinaryNode  # # # # # # # # # # # # # # # # # # # # # # #


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value=Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.value)

    def is_leaf(self):
        if self.right_child is None and self.left_child is None:
            return True
        else:
            return False

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)


# # # # # # # # # # # # # # # # # # # # # # # BinaryTree  # # # # # # # # # # # # # # # # # # # # # # #


class BinaryTree:
    root: BinaryNode

    def __init__(self, value=Any) -> None:
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def show(self) -> None:

        display_tree = treelib.Tree()
        display_tree.create_node(tag=self.root.value, identifier=self.root.value)

        def left_right_children(node: 'BinaryNode') -> None:

            if node.left_child:
                display_tree.create_node(tag=node.left_child.value,
                                         identifier=node.left_child.value, parent=node.value)

            if node.right_child:
                display_tree.create_node(tag=node.right_child.value,
                                         identifier=node.right_child.value, parent=node.value)

        self.traverse_pre_order(left_right_children)  # only can be done with pre_order, other doesnt work
        display_tree.show()


def closest_parent(tree: BinaryTree, first_node: BinaryNode, second_node: BinaryNode) -> BinaryNode:

    if tree is None:
        return None
    elif tree is first_node or tree is second_node:
        return tree

    right_subtree = closest_parent(tree.right_child, first_node, second_node)

    left_subtree = closest_parent(tree.left_child, first_node, second_node)

    if right_subtree is not None and left_subtree is not None:
        return tree
    elif left_subtree is not None:
        return left_subtree
    else:
        return right_subtree


tree2 = BinaryTree(1)
tree2.root.add_left_child(2)
tree2.root.add_right_child(3)
tree2.root.left_child.add_left_child(4)
tree2.root.left_child.add_right_child(5)
tree2.root.right_child.add_right_child(7)
tree2.root.left_child.left_child.add_left_child(8)
tree2.root.left_child.left_child.add_right_child(9)

print("\n\nTREE 2 : \n")
tree2.show()

# 1 SAMPLE
cp1 = closest_parent(tree2.root, tree2.root.left_child.right_child, tree2.root.left_child.left_child.left_child)
print("Closest parent to 8 and 5 is : " + str(cp1))
# 2 SAMPLE                                                                      # cp=closest parent
cp2 = closest_parent(tree2.root, tree2.root.left_child.left_child.right_child, tree2.root.right_child.right_child)
print("Closest parent to 9 and 7 is : " + str(cp2))
# 3 SAMPLE
cp3 = closest_parent(tree2.root, tree2.root.left_child.left_child.left_child, tree2.root.right_child.right_child)
print("Closest parent to 8 and 7 is : " + str(cp3))
# 4 SAMPLE
cp4 = closest_parent(tree2.root, tree2.root.left_child.left_child, tree2.root.left_child.right_child)
print("Closest parent to 4 and 5 is : " + str(cp4))
# 5 SAMPLE
cp5 = closest_parent(tree2.root, tree2.root.left_child.right_child, tree2.root.right_child.right_child)
print("Closest parent to 5 and 7 is : " + str(cp5))
# 6 SAMPLE
cp6 = closest_parent(tree2.root, tree2.root, tree2.root.left_child)
print("Closest parent to 1 and 2 is : " + str(cp6))
# 7 SAMPLE
cp7 = closest_parent(tree2.root, tree2.root, tree2.root)
print("Closest parent to 1 and 1 is : " + str(cp7))