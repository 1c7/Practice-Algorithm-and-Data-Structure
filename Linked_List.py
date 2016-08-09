
# http://openbookproject.net/thinkcs/python/english3e/linked_lists.html

# Sturcture
class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

# New 3 Node
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# point Node to other
node1.next = node2
node2.next = node3

# print them
def print_list(node):
    while node is not None:
        print(node, end=" ")
        node = node.next
    print()

print_list(node1)




