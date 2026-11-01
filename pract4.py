#Inserting an element in the linked list

#Inserting node at the beginning (at the head)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Singly:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("the linked list is empty")
        temp = self.head
        while temp:
            print(temp.data, "-->",end= " ")
            temp = temp.next
    def insertBeg(self,new_node):
        new_node.next = self.head #Points the next node to current head
        self.head = new_node #Updating the current linked list node
    def insertEn(self,last_node):
        last_node.next = None #As it is an last node so no address of next node is there
        temp = self.head #Creating temporary variable for traversing 
        while temp.next is not None:
            temp = temp.next #traversing until the last node of the current linked list
        temp.next = last_node #Store adress of last node
    def insert(self, insert_node,pos):
        temp = self.head #Traversing the linked list
        for i in range(pos-1): #pos = position at which the element is to be inseted
            temp = temp.next

        insert_node.next = temp.next #copying the adress of next node to inserted node
        temp.next = n5 # Adding address of inserted node to previous node
    def deletePos(self,pos):
        temp = self.head.next #Pointing at the node to be deleted
        prev = self.head #
        for i in range(1,pos-1):
            temp = temp.next #Pointing towards next node
            prev = prev.next
        prev = prev.next
        temp.next = None #disconnets the list 
    def searchUnso(self,ele):
        temp = self.head
        while temp is not None:
            if( temp.data == ele):
                print("Found")
            temp = temp.next
            print("No Record Exist")
    def Sort(self,data):
        temp = self.head
        sorting = []
        while temp:
            sorting.append(temp)
        temp = temp.next
            
        
        

        
n = Node(10) #Creating an object
x = Singly() #Creating an object
x.head = n #Assigning head to the first element of the node 

n1 = Node(20) #Creating a 2nd node
x.head.next = n1

n2 = Node(30) #Creating a 3rd node
n1.next = n2

n3 = Node(0) #Creating a node which is inserted at the beginning 
x.insertBeg(n3)

n4 = Node(50) #Creating a node which is indserted at the specific position
x.insertEn(n4)

n5 = Node(40)
x.insert(n5,4)

x.deletePos(5)
x.searchUnso(50)
x.display()
        
