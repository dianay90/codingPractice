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


node_one = Node(5)
list =  LinkedList()
list.head = node_one
print("first list print")
list.print_list()

list.insert_first(15)

print("second list print")

list.print_list()
list.size()

head= list.get_first()
print("Get first head " + str(head.data))
