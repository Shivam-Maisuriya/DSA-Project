# Practical 1: Implementation of Array operations - Insert, Delete, Search, Update, and Display. 
#  Name: Shivam Maisuriya
#  Enrollment No: 202203103510303
# Batch:B.Tech CSE

arr = []

while True:
    print("\n1. Insert Element\n2. Update Element\n3. Search Element Index\n4. Delete Element\n5. Display Arrray\n6. To Quit\n")
    OperationNumber = int(input("Enter Operation Number : "))
    # print(" ")
    if OperationNumber == 6:
        break

    match OperationNumber:
        case 1:
            # Insert 
            i = int(input("Enter the number of elements you want to enter :"))
            j = 0
            
            while j != i:
                num = input("Enter the value : ")
                arr.append(num)
                j += 1
            print("<---------- Insert Successfull ------------> ")

        case 2: 
            # Update index
            Index = input("Enter index :")
            Value = input("Enter Value :")

            arr.insert(int(Index) , int(Value))
            print("<---------- Update Successfull ------------> ")

        case 3:
            # Search 
            element = input("Enter value: ")
            print("Element found at index -",arr.index(element))

        case 4:
            # delete 
            delNumber = input("Enter the value which you want to delete :")
            arr.remove(delNumber)
            print("<---------- Delete Successfull ------------> ")

        case 5:
            # Display 
            print("<---------- Displaying Array ------------> \n" ,arr)

