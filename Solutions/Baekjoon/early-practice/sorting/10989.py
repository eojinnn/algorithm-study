"""문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다."""

class LinkedList:
    def __init__(self):
        self.head = None

    # def add(self,data):
    #     node = Node(data)
    #     node.next = self.head
    #     self.head = node

    def sort(self,data):
        node = Node(data)
        if self.head is None:
            node.next = self.head
            self.head = node
            return
        
        prev_node = None
        cur_node = self.head
        while cur_node is not None and cur_node.data < node.data:
            prev_node = cur_node
            cur_node = cur_node.next
        node.next = cur_node
        if prev_node is None:
            self.head = node
        else:
            prev_node.next = node

    # def __repr__(self):
    #     node = self.head
    #     nodes = []
    #     while node is not None:
    #         nodes.append(node.data)
    #         node = node.next
    #     return nodes

    def __repr__(self):
        printlist = ''
        node = self.head
        while True:
            if node is None:
                break
            printlist = str(printlist) + str(node.data)
            if node.next is not None:
                printlist = str(printlist) + '\n'
            node = node.next
        return printlist

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data

N = int(input())
llist = LinkedList()
for i in range(N):
    llist.sort(int(input()))
print(llist)



        

        




        




