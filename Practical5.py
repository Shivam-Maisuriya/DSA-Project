# Practical 5: Write a menu driven program to implement following operations on the singly linked list. 
            # (a) Insert a node at the front of the linked list 
            # (b) Insert a node at the end of the linked list 
            # (c) Insert a node such that linked list is in ascending order 
            # (d) Delete a First node of the linked list 
            # (e) Delete a node before specified position 
            # (f) Delete a node after specified position. 
# Name: Shivam Maisuriya
# Enrollment No: 202203103510303
# Batch:B.Tech CSE

class Node:                         # 1.create node class which stores [data|refrence]
    def __init__(self , data):
        self.data = data
        self.ref = None

class LinkedList:                   # 2.Creating Linked List class 
    def __init__(self) :
        self.head = None
    
    def print_LL(self):             # Traversing in Linked List
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end = " ")      #if we want in single line 10 --> 20 -->
                n = n.ref           #for going to the next node

    # Inserting node 
    def add_begin(self, data):
        new_node = Node(data)       #Create new node
        new_node.ref = self.head    #set new_node refrence = previous head 
        self.head = new_node        #Insert at Begining usign head = New_Node
    
    def add_end(self, data):
        new_node = Node(data)       #Create New Node
        if self.head is None:       #check Linked List is empty or not
            self.head = new_node    #if yes then set new node as first node
        else:                       
            n = self.head               #if not then set n = head of linked list
            while n.ref is not None:    #check until node refrence will be None
                n = n.ref               #for going to next node
            n.ref = new_node            #set last node refrence is new node
    
    def sort(self):
        arr = []
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                arr.append(n.data)     
                n = n.ref 
            self.head = None
            arr.sort()
            for i in range(len(arr)):
                LL1.add_end(arr[i])
            LL1.print_LL()
            
    # Deleting node 
    def delete_begin(self):             # from begining 
        if self.head is None:           #checking LinkedList is empty or not
            print("LinkedList is empty! So We can't delete node. ")
        else:
            self.head = self.head.ref   #set head to next node
            
    def delete_before(self, x):
        if self.head is None:
            print("Empty LinkedList!")
            return
        else:
            n = self.head
            while n is not None:
                if n.ref.ref.ref.data == x:
                    break
            n = n.ref
            if n is None:
                print("Data not found!")
                return
            else: 
                n.ref = n.ref.ref
                
    def delete_after(self,x):
        if self.head is None:
            print("Empty LinkedList!")
            return
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.ref
            if n is None:
                print("data not found!")
            elif n.ref is None:
                print("There is no node after given data!")
            else:
                n.ref = n.ref.ref
                return

            
LL1 = LinkedList()                  # creating Linked list

while True:
    print("\n1.Print LinkedList")
    print("2.Add Node at begining")
    print("3.Add Node at end")
    print("4.Sort LinkedList")
    print("5.Delete at begining")
    print("6.Delete before specific position")
    print("7.Delete after specific position")
    print("Press 'q' to Quit \n")
    num = input("Enter your Choice: ")
    
    if num == 'q' or num == 'Q':
        break
    
    match int(num):
        case 1: 
            LL1.print_LL()
            
        case 2: 
            value = input("Enter the data: ")
            LL1.add_begin(value)
        
        case 3:
            value = input("Enter the data: ")
            LL1.add_end(value)
            
        case 4:
            LL1.sort()
            
        case 5:
            LL1.delete_begin()
            
        case 6:
            value = input("Enter the data: ")
            LL1.delete_before(value)
            
        case 7:
            value = input("Enter the data: ")
            LL1.delete_after(value)
                            
        case _:
            print("Invalid Input!")
