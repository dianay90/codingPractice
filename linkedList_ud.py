class Node: 
    def __init__(self, data, next = None): 
        self.data = data
        self.next = next 

class LinkedList: 
    def __init__(self): 
        self.head = None

    def insert_first(self,data):
        self.head = Node(data,self.head) 

    def print_list(self):
        temp = self.head
        if temp == None: 
            print("List is empty")
        while(temp):
            print(temp.data)
            temp = temp.next

    def size(self): 
        current = self.head
        count = 0 
        while(current):
            count +=1
            current = current.next
        print("Size is " + str(count))
        return count

    def get_first(self):
        return self.head

    def get_last(self):
        current = self.head 

        while(current):
            if current.next == None: 
                return current
            else: 
                current = current.next

    def clear_list(self): 
        self.head = None 

    def remove_first(self):
        if self.head == None:
            return
        
        self.head = self.head.next 

    def remove_last(self):
        if self.head == None:
            return
        
        if self.head.next == None: 
            return 

        previous = self.head
        current = self.head.next

        while(current):
            if current.next == None: 
                previous.next = None 
            else: 
                previous = previous.next

            current = current.next

    def insert_last(self, data):
        if self.head == None: 
            self.head = Node(data)
        else: 
            node = Node(data)
            current = self.get_last()
            current.next = node
    '''

    def get_at(self,index):
        counter = 0 
        current = self.head
        while (counter != index):
        
            counter += 1 
            current= current.next
            
        return current.data
    '''

    def get_at2(self, index):
        counter =0 
        current = self.head

        while(current):
            if counter == index: 
                return current.data
            counter +=1
            current = current.next

        return None 
    def linked_list_midpoint(self, list): 
        slow = list.head 
        fast = list.head

        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        
        return slow 
node_one = Node(5)

list =  LinkedList()
list.head = node_one
print("first list print")
list.print_list()

list.insert_first(15)
list.insert_first(15)
list.insert_first(1)
list.insert_first(8)

list.insert_first(9)
list.insert_first(1)
list.insert_first(6)
list.insert_first(0)
list.insert_first(4)
list.insert_first(10)


print("second list print")

list.print_list()
list.size()

head= list.get_first()
print("Get first head " + str(head.data))

last = list.get_last()
print("Get last  " + str(last.data))

'''
print("clear list")
list.clear_list()
list.print_list()
'''

list.remove_first()
list.print_list()

print("Removing last")
list.remove_last()
list.print_list()

print("Insert last")
list.insert_last(17)
list.print_list()

print("Get at")
index = 0
retrieved_data = list.get_at2(index)
print("Retrieved data at index " + str(index) + ": " + str(retrieved_data))
print(retrieved_data)


index = 4
retrieved_data = list.get_at2(index)
print("Retrieved data at index " + str(index) + ": " + str(retrieved_data))
print(retrieved_data)

index = 1
retrieved_data = list.get_at2(index)
print("Retrieved data at index " + str(index) + ": " + str(retrieved_data))
print(retrieved_data)

index = 10
retrieved_data = list.get_at2(index)
print("Retrieved data at index " + str(index) + ": " + str(retrieved_data))
print(retrieved_data)

print("Linked list midpoint")
midpoint = list.linked_list_midpoint(list)
print("midpoint is " + str(midpoint.data))