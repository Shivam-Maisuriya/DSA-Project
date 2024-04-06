# Practical 4: Queue operations 1.Insert 2.Delete 3.Display. 
# Name: Shivam Maisuriya
# Enrollment No: 202203103510303
# Batch:B.Tech CSE

queue = []
arr = []
count = 0
rear = 0
 
size = int(input("Enter the size of Queue: "))

for i in range(size):
    queue.insert(i , '')
    
for i in range(size):
    arr.insert(i , '')

while True:
    print("\nQueue Operations")
    print("1. Insert an element in the Queue")
    print("2. Delete an element from the Queue")
    print("3. Display the Queue")
    print("4. Exit")
    i = int(input("Enter number : "))

    # insert 
    if i == 1:
        if count == size:
            for j in range(len(queue)):
                if queue[j] == '':
                    count = j
                    element = input("Enter the element: ")
                    queue.pop(count)
                    queue.insert(count , element)
                    count += 1
                    # print("Queue is full")
                    break
                else:
                    print("Queue is Full")
        else:
            element = input("Enter the element: ")
            queue.pop(count)
            queue.insert(count , element)
            # queue.append(element)
            count += 1
            
    # delete 
    if i == 2: 
        if queue == arr :
            print("Queue is empty")
        else: 
            if rear < size :
                queue.pop(rear)
                queue.insert(rear, '')
                rear += 1
            else:
                rear = 0
    # display
    if i == 3:
        print(queue)
    # Exit
    if i == 4: 
        break