class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.right = self.head
            self.head.left = None
            self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while(temp.right != None):
                temp = temp.right
            temp.right = new_node
              
        
    def insert_at_index(self, old_data, new_data):
        temp = self.head
        while temp.data != old_data:
            temp = temp.right
            
        if temp.data != old_data and temp.right == None:
            print("No Data Found")
        else:
            temp.data = new_data
    def delete_from_start(self):
        if self.head == None:
            print("No Data found")
            return
        else:
            self.head = self.head.right 
            
    def delete_from_end(self):
        
        if self.head is None:
            print("No Data Found")
        else:
            temp = self.head
            while(temp.right.right != None):
                temp = temp.right
            temp.right = None
    def delete_data_from_value(self, data):
        pass    
    def traverse(self):
        temp = self.head
        while temp.right:
            print(temp.data, end  = "->")
            temp = temp.right
        print(temp.data)


Linked_List = DoublyLinkedList()
Linked_List.insert_at_beginning(10)
Linked_List.insert_at_beginning(5)
Linked_List.insert_at_end(12)
Linked_List.insert_at_end(15)

Linked_List.traverse()
Linked_List.insert_at_index(12, 18)

Linked_List.traverse()


Linked_List.delete_from_start()
Linked_List.traverse()
Linked_List.delete_from_end()
Linked_List.traverse()