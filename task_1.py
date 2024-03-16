class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def merge_sorted_lists(self, list1, list2):
        dummy = Node()
        tail = dummy

        while list1 and list2:
            if list1.value < list2.value:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next

    def sort(self):
        if not self.head or not self.head.next:
            return self.head

        middle = self.get_middle(self.head)
        next_to_middle = middle.next
        middle.next = None

        left = self.sort(self.head)
        right = self.sort(next_to_middle)

        sorted_list = self.merge_sorted_lists(left, right)
        return sorted_list

    def get_middle(self, head):
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# Test
ll = LinkedList()
ll.append(10)
ll.append(5)
ll.append(15)
ll.append(2)
ll.print_list()
ll.reverse()
ll.print_list()
