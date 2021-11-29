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
                temp_queue = temp_queue + str(self._storage.node(i).data) # dla ostatniego elementu - brak przecinka
            else:
                temp_queue = temp_queue + str(self._storage.node(i).data) + ", "
        return temp_queue


# # # # # # # # # # # # # # # # # # # # # # # TREENODE  # # # # # # # # # # # # # # # # # # # # # # #


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value=Any):
        self.value = value
        self.children = []

    def __str__(self):
        return str(self.value)

    def is_leaf(self) -> bool:
        if not self.children:  # if its list is empty
            return True
        else:
            return False

    def add(self, children1: 'TreeNode') -> None:
        self.children.append(children1)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:  # visit: []]
        visit(self)
        # after visit function, loop and check on all children
        for i in self.children:
            i.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        queue1 = Queue()
        for i in self.children:
            queue1.enqueue(i)
        while queue1:
            j = queue1.dequeue()
            visit(j)
            for i in j.children:
                queue1.enqueue(i)

    def search(self, value: Any) -> Union['TreeNode', None]:

        searched = []

        def support_search(t_node: 'TreeNode') -> None:
            if t_node.value == value:
                searched.append(t_node)

        self.for_each_deep_first(support_search)
        if searched:
            return searched[0]
        else:
            return None


# # TESTY
# F = TreeNode(5)
# B = TreeNode(6)
# G = TreeNode(7)
# F.add(B)
# F.add(G)
# print("F children:")
# for x in F.children:
#     print(x.value) # or just print(x) - we got str method override
# print("IS F A LEAF ? :")
# print(F.is_leaf())
# print("G value :")
# print(G.value)
# print("G children :")
# print(G.children)
# print("IS G A LEAF ? :")
# print(G.is_leaf())
# print(F.for_each_deep_first)
# print(F.search(3))
# print(F.search(6))


# # # # # # # # # # # # # # # # # # # # # # # TREE  # # # # # # # # # # # # # # # # # # # # # # #

class Tree:
    root: TreeNode

    def __init__(self, value=Any):
        self.root = TreeNode(value)

    def add(self, value: Any, parent_name: Any) -> None:
        TreeNode(value)
        kid = TreeNode(value=value)
        self.root.search(parent_name).add(kid)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit=visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit=visit)

    def show(self):
        for lines, filler, name in RenderTree(self.root):   # filling for multiple line entries
            print("%s%s" % (lines, name))

# second method to display the tree ( using treelib )
    def display(self) -> None:
        display_tree = treelib.Tree()
        display_tree.create_node(tag=self.root.value, identifier=self.root.value)

        def children_nodes(node: 'TreeNode') -> None:
            for x in node.children:
                display_tree.create_node(tag=x.value, identifier=x.value, parent=node.value)

        self.for_each_level_order(children_nodes)
        display_tree.show()


drzewo = Tree("F")
# Adding children to the root
drzewo.root.add(TreeNode("B"))
drzewo.root.add(TreeNode("G"))
# Adding children to other nodes
drzewo.add("A", "B")
drzewo.add("D", "B")
drzewo.add("C", "D")
drzewo.add("E", "D")
drzewo.add("I", "G")
drzewo.add("H", "I")

print("\nMETHOD FROM ANYTREE LIBRARY : ")
drzewo.show()
print("\n\n\nMETHOD FROM TREELIB LIBRARY : ")
drzewo.display()