

def nested_dictionary(d): 
    for key, value in d.items():
        if isinstance(value, dict):
            print(key,":")
            nested_dictionary(value)
        else:
            print('{0}: {1}'.format(key, value))


def recursive_fibonacci(number):
    if number = 0:
        return 0
    elif number = 1:
        return 1
    else:
        return recursive_fibonacci(number-1) + recursive_fibonacci(number - 2)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head


node_data = ['Bill', 'Charlie', 'Dave', 'Evan']

current_node = Node('Adam')
names = LinkedList(current_node)

for node in node_data:
    if node:
        current_node.next = Node(node_data)
        current_node = current_node.next

def traverse_linked_list(head):
    if head.next is None:
        return head.data
    else:
        node = head
        return _traverse_linked_list(node.next)

    def _traverse_linked_list(node):
        if node.next:
            return _traverse_linked_list(node.next)
        else:
            return '--> ' + node.data


if __name__ == '__main__':
    print('Recursive functions are available')