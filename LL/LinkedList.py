from LL import Node

class LinkedList:
    def __init__(self,value):
        node = Node(value)
        self.head=node
        self.tail=node
        self.length = 1

    def append(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head=value
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length +=1
        return True

    def print(self):
        temp =self.head
        while temp is not None:
            print(temp)
            print(temp.value)
            temp= temp.next