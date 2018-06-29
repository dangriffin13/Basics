

def nested_dictionary(d): 
    for key, value in d.items():
        if isinstance(value, dict):
            print(key,":")
            nested_dictionary(value)
        else:
            print('{0}: {1}'.format(key, value))


def recursive_fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return recursive_fibonacci(number-1) + recursive_fibonacci(number - 2)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node | Data: " + self.data

class LinkedList:
    def __init__(self, head):
        self.head = head


node_data = ['Bill', 'Charlie', 'Dave', 'Evan']

current_node = Node('Adam')
names = LinkedList(current_node)

for node in node_data:
    if node:
        current_node.next = Node(node)
        current_node = current_node.next

def traverse_linked_list(LinkedList):
    
    def _traverse_linked_list(node):
        if node.next:
            return '--> ' + node.data + _traverse_linked_list(node.next)
        else:
            return '--> ' + node.data

    if LinkedList.head.next is None:
        return LinkedList.head.data
    else:
        node = LinkedList.head
        return node.data + _traverse_linked_list(node.next)

    


if __name__ == '__main__':
    print('Recursive functions are available')