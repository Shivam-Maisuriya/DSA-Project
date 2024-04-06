# Practical 3: Implement a program for stack that performs following operations using array.
# (a) PUSH (b) POP (c) PEEP (d) CHANGE (e) DISPLAY
#  Name: Shivam Maisuriya
#  Enrollment No: 202203103510303
# Batch:B.Tech CSE


arr = []

while True:
    print("\n1. PUSH\n2. POP \n3. PEEP \n4. CHANGE \n5. DISPLAY\n6. To Quit\n")
    OperationNumber = int(input("Enter Operation Number : "))
    if OperationNumber == 6:
        break

    match OperationNumber:
        case 1:
            # Push : To insert an item into the stack
            num = input("Enter the value : ")
            arr.append(num)
            print("<-------- Push Successfull -------->")

        case 2:
            # POP : To remove an item from a stack.
            arr.pop(-1)
            print("Successfully poped out")
            print("<-------- Push Successfull -------->")

        case 3:
            # Peep :  To find ith element from stack.
            element = int(input("Enter the ith index:"))
            print("\n<-------- Peep Successfull -------->\n")
            print(arr[element])

        case 4:
            # CHANGE : To change ith element from stack.
            Index = int(input("Enter index :"))
            Value = int(input("Enter Value :"))
            arr.insert(Index , Value)
            print("\n<-------- Change Successfull -------->\n")
            print("Change successfully at {} index and {} value".format(Index , Value))

        case 5:
            #Display : to display 
            print("<-------- Displaying Stack -------->")
            print(arr)






