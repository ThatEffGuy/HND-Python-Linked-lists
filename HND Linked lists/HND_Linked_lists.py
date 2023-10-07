#New linked list

class Node:
    def __init__(self,contents=None, next=None):
        self.contents = contents
        self.next = next

    def getContents(self):
        return self.contents

    def __str__(self):
        return str(self.contents)

def print_list(node):
    while node:
        print(node.getContents())
        node = node.next
    print()

node1 = Node("Alex")
node2 = Node("Barry")
node3 = Node("Craig")
node4 = Node("Dom")
node5 = Node("Edward")

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print_list(node1)