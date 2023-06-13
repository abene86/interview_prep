from typing import TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data:T)->None:
        self.data = data
        self.node = None

class Linkedlist(Generic[T]):

    def __init__(self)->None:
        self.head = None
        self.tail =None

    def append(self, data:T)->None:
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.node = new_node
            self.tail = new_node

    def delete(self, data:T)->T:
        head = self.head
        prev = None
       # print(head is self.head)
        while head != None:
            if head.data == data:
                break
            prev = head
            head = head.node
        if head == None:
            return None
        data = head.data
        prev.node = head.node
        return data

    def print_linklist(self):
        head = self.head
        while head!=None:
            print(head.data, end=" ")
            head = head.node


def main()->None:
    linklist_1 = Linkedlist[str]()
    word = "Abenezer is a lovely person and deserves to be reconginzed by people all around the world"
    for cha in word:
        linklist_1.append(cha)
    linklist_1.print_linklist()
    word = "person and people"
    for cha in word:
        print(linklist_1.delete(cha))
    linklist_1.print_linklist()
main()

