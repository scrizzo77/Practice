class Node:
    data = None
    next = None

head = None

def get_last_node(node):
    if node == None:
      return None
    while node.next != None:
        node = node.next
        return node
  
def append_to_list(node, data):
    global head
    if node == None:
        node = Node()
        node.data = data
        node.next = None
        head = node
    elif node.next == None:
        node.next = Node()
        node.next.data = data
        node.next.next = None
    else:
        append_to_list(node.next, data)


def print_list(node):
    if node == None:
        print("[EMPTY LIST]")
        return
    print(node.data, end='')
    if node.next != None:
        print(" -> ", end='')
        print_list(node.next)
    else:
        print("")

def is_item_in_list(node, item):
    if node.data == item:
        return True
    elif node.next != None:
        return is_item_in_list(node.next,item)
    else:
        return False

def get_list_length(node):
    node_count = 1
    while node.next != None:
        node = node.next
        node_count += 1
    return node_count

def get_item_from_list(node,index):
    nodeNum = 0
    while node != None:
        if nodeNum == index:
            return node.data
        nodeNum += 1
        node = node.next
    return -1
  

'''
item_in_list = is_item_in_list(head, "D")
print(item_in_list)

numNodes = get_list_length(head)
print(numNodes)

index = int(input("Enter index: "))
node_count = get_list_length(head)
while index < 0 or index > (node_count - 1):
  index = int(input("Enter index: "))
print(get_item_from_list(head,index))
'''
def displayMenu():
    menu = "Select one of the following options:\n1. Add node \n2. Delete node \n3. Find index \n4. Insert node (at certain index) \n5.Insert node before certain node \n6. Reverse list \n7. Quit"
    print(menu)

def add_node():
    new_data = input("Enter data to be added: ")
    append_to_list(head,new_data)
    print_list(head)

def delete_node():
    global head
    data = input("Enter data to be deleted: ")
    actual_node = head
    if actual_node == None:
        print("Linked list is empty")
        return
    prev_node = None
    while actual_node != None:
        if actual_node.data == data:
            break
        else:
            prev_node = actual_node
            actual_node = actual_node.next
    if actual_node == None:
        print("Data not found in the linked list")
        return
    if prev_node == None:
        head = actual_node.next
    else:
        prev_node.next = actual_node.next

def find_index():
    data = input("Enter data to be found: ")
    actual_node = head
    if actual_node == None:
        print("Linked list is empty")
        return
    index = 0
    while actual_node != None:
        if actual_node.data == data:
            break
        else:
            index += 1
            actual_node = actual_node.next
    print(f"Index of entered data is: {index}")

def insert_node():
    global head
    node = head
    prevNode = None
    nodeNum = 0
    data = input("Enter data to be inserted: ")
    index = int(input("Enter index for this data to be added at: "))
    if index < 0:
        print("Negative index entered")
        return
    while nodeNum < index and node != None:
        prevNode = node
        node = node.next
        nodeNum += 1
    if nodeNum < index:
        print("Index entered out of range")
        return
    newNode = Node()
    newNode.data = data
    newNode.next = node
    if prevNode != None:
        prevNode.next = newNode
    else:
        head = newNode

def placeBeforeNode():
    global head
    node = head
    prevNode = None
    successor = input("Enter successor node: ")
    data = input("Enter data to be inserted before successor: ")
    while node != None:
        if node.data == successor:
            break
        prevNode = node
        node = node.next
    if node == None:
        print("Successor not found")
        return
    newNode = Node()
    newNode.data = data
    newNode.next = node
    if prevNode == None:
        head = newNode
    else:
        prevNode.next = newNode

    
    

option = 0
while (option < 1 or option > 6) or (option != 7):
    displayMenu()
    option = int(input())
    if option == 1:
        add_node()
    elif option == 2:
        delete_node()
        print_list(head)
    elif option == 3:
        find_index()
    elif option == 4:
        insert_node()
        print_list(head)
    elif option == 5:
        placeBeforeNode()
        print_list(head)
    elif option == 6:
        print("NOT YET SUPPORTED")
  

