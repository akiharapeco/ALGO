MAX_ARRAY_SIZE = 10**6

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.prev = None
        self.next = None
    def getData(self):
        return self.data
    def getPrev(self):
        return self.prev
    def getNext(self):
        return self.next
    def setData(self, new_data):
        self.data = new_data
    def setPrev(self, new_prev):
        self.prev = new_prev
    def setNext(self, new_next):
        self.next = new_next

class DoublyLinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None
    def insert(self, x):
        if self.first_node == None:
            self.first_node = Node(x)
        else:
            self.first_node.setPrev(Node(x))
            node = self.first_node
            self.first_node = node.getPrev()
            self.first_node.setNext(node)
            self.first_node.setPrev(None)
            self.first_node.setData(x)
        if self.last_node == None:
            self.last_node = self.first_node
    def delete(self, x):
        node = self.first_node
        while node != None:
            if node.getData() == x:
                if node == self.last_node:
                    self.deleteLast()
                elif node == self.first_node:
                    self.deleteFirst()
                else:
                    node.getPrev().setNext(node.getNext())
                    node.getNext().setPrev(node.getPrev())
                    del node
            else:
                node = node.getNext()
    def deleteFirst(self):
        node = self.first_node.getNext()
        del self.first_node
        node.setPrev(None)
        self.first_node = node
    def deleteLast(self):
        node = self.last_node.getPrev()
        node.setNext(None)
        if self.last_node == self.first_node:
            self.first_node = node
        del self.last_node
        self.last_node = node

double_list = DoublyLinkedList()

N = int(input())
for i in range(N):
    command = input().strip().split()
    if command[0] == 'deleteFirst':
        double_list.deleteFirst()
    elif command[0] == 'deleteLast':
        double_list.deleteLast()
   elif command[0] == 'delete':
        double_list.delete(command[1])
    elif command[0] == 'insert':
        double_list.insert(command[1])
