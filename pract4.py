#Practical 4 : Student Record Management System using Singly Linked List

class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None  #Address of next node (None for the last node)


class Singly:
    def __init__(self):
        self.head = None

    #1) Add a student (at the end of the list)
    def add(self, roll, name, marks):
        new_node = Node(roll, name, marks)
        if self.head is None:          #List is empty -> new node becomes head
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:  #Traverse to the last node
                temp = temp.next
            temp.next = new_node          #Link last node to new node
        print("Student added successfully")

    #2) Delete a student by roll number
    def delete(self, roll):
        temp = self.head
        prev = None
        while temp is not None:
            if temp.roll == roll:
                if prev is None:           #Node is the first node -> update head
                    self.head = temp.next
                else:
                    prev.next = temp.next  #Adjust link to skip the node
                print("Student record deleted")
                return
            prev = temp
            temp = temp.next
        print("Record Not Found")

    #3) Update a student by roll number
    def update(self, roll):
        temp = self.head
        while temp is not None:
            if temp.roll == roll:
                temp.name = input("Enter new name: ")
                temp.marks = int(input("Enter new marks: "))
                print("Student record updated")
                return
            temp = temp.next
        print("Record Not Found")

    #4) Search a student by roll number
    def search(self, roll):
        temp = self.head
        while temp is not None:
            if temp.roll == roll:
                print("Record Found ->", "Roll No:", temp.roll, "Name:", temp.name, "Marks:", temp.marks)
                return
            temp = temp.next
        print("Record Not Found")

    #5) Sort records (bubble sort, swapping the student data)
    def sort(self, field, order):
        if self.head is None:
            print("The linked list is empty")
            return
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next is not None:
                nxt = temp.next
                #field 1 = Roll No, field 2 = Marks
                if field == 1:
                    a = temp.roll
                    b = nxt.roll
                else:
                    a = temp.marks
                    b = nxt.marks
                #order 1 = ascending, order 2 = descending
                if (order == 1 and a > b) or (order == 2 and a < b):
                    #Swap the student data of the two nodes
                    temp.roll, nxt.roll = nxt.roll, temp.roll
                    temp.name, nxt.name = nxt.name, temp.name
                    temp.marks, nxt.marks = nxt.marks, temp.marks
                    swapped = True
                temp = temp.next
        print("Records sorted successfully")

    #6) Display all records
    def display(self):
        if self.head is None:
            print("The linked list is empty")
            return
        temp = self.head
        print("Roll No\tName\tMarks")
        while temp:
            print(temp.roll, "\t", temp.name, "\t", temp.marks)
            temp = temp.next


x = Singly()  #Creating an object of the linked list

while True:
    print("\n----- Student Record Management System -----")
    print("1. Add a student record")
    print("2. Delete a student record")
    print("3. Update a student record")
    print("4. Search for a student")
    print("5. Sort records")
    print("6. Display records")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        r = int(input("Enter Roll No: "))
        n = input("Enter Name: ")
        m = int(input("Enter Marks: "))
        x.add(r, n, m)
    elif choice == 2:
        r = int(input("Enter Roll No to delete: "))
        x.delete(r)
    elif choice == 3:
        r = int(input("Enter Roll No to update: "))
        x.update(r)
    elif choice == 4:
        r = int(input("Enter Roll No to search: "))
        x.search(r)
    elif choice == 5:
        f = int(input("Sort by 1. Roll No  2. Marks : "))
        o = int(input("Order 1. Ascending  2. Descending : "))
        x.sort(f, o)
        x.display()
    elif choice == 6:
        x.display()
    elif choice == 7:
        print("Thank you")
        break
    else:
        print("Invalid choice")