import streamlit as st

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertBeginning(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insertEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insertIndex(self, new_data, index):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        if index == 0:
            self.insertBeginning(new_data)
        else:
            current = self.head
            for i in range(index - 1):
                if current is None:
                    raise IndexError("Index out of bounds")
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def deleteStart(self):
        if self.head is None:
            return
        self.head = self.head.next

    def deleteEnd(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def Traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


# Streamlit app
st.title("Linked List Operations")

# Initialize the linked list
if "linked_list" not in st.session_state:
    st.session_state.linked_list = LinkedList()

linked_list = st.session_state.linked_list

# Display the linked list
st.subheader("Current Linked List")
elements = linked_list.Traverse()
st.write(" -> ".join(map(str, elements)) + " -> None")

# Insert operations
st.subheader("Insert Operations")
insert_choice = st.selectbox("Choose an insert operation", ["Insert at Beginning", "Insert at End", "Insert at Index"])
new_data = st.number_input("Enter the value to insert", value=0, step=1)

if insert_choice == "Insert at Beginning":
    if st.button("Insert at Beginning"):
        linked_list.insertBeginning(new_data)
elif insert_choice == "Insert at End":
    if st.button("Insert at End"):
        linked_list.insertEnd(new_data)
elif insert_choice == "Insert at Index":
    index = st.number_input("Enter the index", value=0, step=1)
    if st.button("Insert at Index"):
        try:
            linked_list.insertIndex(new_data, index)
        except IndexError:
            st.error("Index out of bounds")

# Delete operations
st.subheader("Delete Operations")
delete_choice = st.selectbox("Choose a delete operation", ["Delete from Start", "Delete from End"])

if delete_choice == "Delete from Start":
    if st.button("Delete from Start"):
        linked_list.deleteStart()
elif delete_choice == "Delete from End":
    if st.button("Delete from End"):
        linked_list.deleteEnd()

# Search operation
st.subheader("Search Operation")
search_key = st.number_input("Enter the value to search", value=0, step=1)
if st.button("Search"):
    found = linked_list.search(search_key)
    if found:
        st.success(f"Value {search_key} found in the linked list.")
    else:
        st.error(f"Value {search_key} not found in the linked list.")

# Reverse operation
st.subheader("Reverse Linked List")
if st.button("Reverse"):
    linked_list.reverse()
    st.success("Linked list reversed successfully!")