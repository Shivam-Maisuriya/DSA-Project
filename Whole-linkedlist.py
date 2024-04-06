# 1.create node class which stores [data|refrence]
class Node:
    def __init__(self , data):
        self.data = data
        self.ref = None
        
# node1 = Node(10) 
# print(node1) # it will return -> <__main__.Node object at 0x0000018E7E80B100>  

# 2.Creating Linked List class 
class LinkedList:
    def __init__(self) :
        self.head = None
    
    # Traversing in Linked List
    def print_LL(self):   
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                # print(n.data)       #for accesing and print data 
                print(n.data, "--->", end = " ")      #if we want in single line 10 --> 20 -->
                n = n.ref           #for going to the next node

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
    
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in LinkedList!")
        else: 
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
    def add_before(self, data, x):
        if self.head is None:
            print("LinkedList is empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head 
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
    # Deleting node 
    def delete_begin(self):             # from begining 
        if self.head is None:           #checking LinkedList is empty or not
            print("LinkedList is empty! So We can't delete node. ")
        else:
            self.head = self.head.ref   #set head to next node
        
    def delete_end(self):
        if self.head is None:
            print("LinkedList is empty! So We can't delete node. ")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
            
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
                
# creating Linked list
LL1 = LinkedList()

def call():
    while True:
        print("\n1.Print LinkedList")
        print("2.Add Node at begining")
        print("3.Add Node at end")
        print("4.Add Node after")
        print("5.Add Node before")
        print("6.Delete at begining")
        print("7.Delete at end")
        print("8.Delete before")
        print("9.Delete after")
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
                value = input("Enter the data: ")
                after = input("Which number after: ")
                LL1.add_after(value, after)
                
            case 5:
                value = input("Enter the data: ")
                after = input("Which number after: ")
                LL1.add_before(value, after)
                                            
            case 6:
                LL1.delete_begin()
                
            case 7:
                LL1.delete_end()
                              
            case 8:
                value = input("Enter data before: ")
                LL1.delete_before(value)
                
            case 9:
                value = input("Enter data after: ")
                LL1.delete_after(value)
                                            
            case _:
                print("Invalid Input!")

call()



