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
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length +=1
        return True

    def print(self):
        temp =self.head
        while temp is not None:
            print(temp.value)
            temp= temp.next

    def popFirst(self):
        if self.length==0:
            return None
        temp = self.head
        self.head=temp.next
        temp.next =None
        self.length -=1
        if self.length == 0:
            self.tail=None
        return temp

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = temp
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
        else :
            new_node.next=self.head
            self.head =new_node
            self.length +=1
        return True

    def getValue(self,index):
        if index<0 or index >=self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp =temp.next
        return temp

    def set(self,index,value):
        temp  = self.getValue(index)
        if temp:
            temp.value=value
            return True
        return False

    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index ==self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.getValue(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True

    def remove(self,index):
        if index < 0 or index > self.length:
            return False
        if index ==0:
            temp = self.popFirst()
        if index ==self.length-1:
            temp = self.pop()
        prev = self.getValue(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next =None
        self.length-=1
        return temp

    def reverse(self):
        temp = self.head
        self.head=self.tail
        self.tail =temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next =before
            before = temp
            temp = after