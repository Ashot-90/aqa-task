class ListNode:
    def __init__(self, data, next=None):
        self.val = data
        self.next = next


def convert_to_list_node(elements):
    head = ListNode(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(element)
    return head


class Heap:
    def __init__(self):
        self.data = []

    def get_val(self, i):
        return self.data[i].val
    
    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    def insert(self, value):
        self.data.append(value)
        n = len(self.data) - 1
        i = n
        while i != 0 and self.data[i].val < self.data[self.parent(i)].val:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        smallest = i
        n = len(self.data)
        if left < n and self.get_val(left) < self.get_val(smallest):
            smallest = left
        if right < n and self.get_val(right) < self.get_val(smallest):
            smallest = right
        if smallest != i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.heapify(smallest)

    def extract_min(self):
        n = len(self.data)
        if n == 0:
            return '#'
        if n == 1:
            temp = self.data[0]
            self.data.pop()
            return temp
        root = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self.heapify(0)
        return root


def merge(*iterables):
    list_of_node_lists = []
    for sub in iterables:
        if sub:
            list_of_node_lists.append(convert_to_list_node(sub))
    heap = Heap()
    for i in list_of_node_lists:
        heap.insert(i)
    res = None
    res_next = None
    while True:
        temp = heap.extract_min()
        if temp == "#":
            return res
        if not res:
            res = temp
            res_next = temp
            temp = temp.next
            if temp:
                heap.insert(temp)
            res.next = None
        else:
            res_next.next = temp
            temp = temp.next
            res_next = res_next.next
            if temp:
                heap.insert(temp)
            res_next.next = None
