## chapter7. 링크드 리스트(연결리스트)

# 링크드 리스트 기본 구조와 용어
# 노드(Node): 데이터 저장 단위 (데이터값, 포인터)  로 구성
# 포인터(pointer): 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

# 간단한 링크드 리스트 예제
class Node:
    def __init__(self, data, address = None):
        self.data = data
        self.address = address

# Node와 Node 연결하기
node1 = Node(1)
node2 = Node(2)
node1.address = node2
head = node1

def add(data):
    node = head
    while node.address:
        node = node.address
    node.address = Node(data)

# 링크드 리스트로 데이터 추가
for index in range(3, 10):
    add(index)

# 링크드 리스트 데이터 출력하기(검색하기)
node = head
while node.address:
    print(node.data)
    node = node.address
print(node.data)


#  check 1) linked list 데이터 사이에 데이터를 추가
newdata = 1.5
node = head
while node.address:
    if node.data < newdata and node.address.data > newdata:
        newnode = Node(newdata)
        newnode.address = node.address
        node.address = newnode
        break
    else:
        node = node.address

## 문제답안
node3 = Node(1.5)
node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

node_next = node.address
node.address = node3
node3.address = node_next

#출력
node = head
while node.address:
    print(node.data)
    node = node.address
print(node.data)


# 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현
class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.address:
                node = node.address
            node.address = Node(data)

    def desc(self): #순회하는 함수
        node = self.head
        while node:
            print(node.data)
            node = node.address

    def find(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.address
        print("There are not that index node!")

    # delete 함수
    def delete(self, data):
        if self.head == '':
            print("There are not that index node!")
        else :
            node = self.head
            if node.data == data:
                self.head = node.address
                del node
            else:
                while node.address:
                    if node.address.data == data:
                        temp = node.address
                        node.address = node.address.address
                        del temp
                        break
                    else:
                        node = node.address

print("------------------------------1")
linkedlist = NodeMgmt(0)
linkedlist.desc()
print("------------------------------")
for index in range(1,10):
    linkedlist.add(index)
linkedlist.desc()
print("------------------------------")
linkedlist.delete(7)
linkedlist.desc()
print("------------------------------")
linkedlist.delete(1)
linkedlist.desc()
print("------------------------------")
linkedlist.delete(9)
linkedlist.desc()
print("------------------------------")
linkedlist.delete(0)
linkedlist.desc()

findNode = linkedlist.find(5)
print(findNode.data)


# 다양한 링크드 리스트 구조 _ 더블 링크드 리스트(doubly linked list)
# 양방향으로 연결. 양쪽으로 노드탐색 가능

class DoubleNode:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.next = next
        self.prev = prev

class NodeMgmt_double:
    def __init__(self, data):
        self.head = DoubleNode(data)
        self.tail = self.head # 데이터가 하나인 경우 tail은 Head를 가르킨다.

    def insert(self, data):
        if self.head == None:
            self.head = DoubleNode(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = DoubleNode(data)
            node.next.prev = node
            self.tail = node.next

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_from_head(self, data):
        node = self.head
        while node.next:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self, data):
        node = self.tail
        while node.prev:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    def add_in_front(self, data, finddata):
        #올림: math.ceil, 내림 : math.floor  반올림: round
        location = self.search_from_head(finddata)
        if location == False:
            print("finddata is wrong.")
            return False
        else:
            newnode = DoubleNode(data)
            if location.prev == None:
                self.head = newnode
                newnode.prev = None
                newnode.next = location
                location.prev = newnode
            else:
                newnode.prev = location.prev
                newnode.next = location
                location.prev.next = newnode
                location.prev = newnode

    def add_in_back(self, data, finddata):
        location = self.search_from_tail(finddata)
        if location == False:
            print("finddata is wrong.")
            return False
        else:
            newnode = DoubleNode(data)
            if location.next == None:
                self.tail = newnode
                location.next = newnode
                newnode.prev = location
                newnode.next = None
            else:
                newnode.prev = location
                newnode.next = location.next
                location.next.prev = newnode
                location.next = newnode

print("------------------------------")
double_linkedlist = NodeMgmt_double(0)
for index in range(1, 10):
    double_linkedlist.insert(index)
double_linkedlist.desc()

# 연습 : 위 코드에서 노드 데이터가 특정 숫자인 노드 앞에 데이터를 추가하는 함수를 만들고 테스트하기
# - double_linkedlist의 tail 에서부터 뒤로 이동하며, 특정 숫자인 노드를 찾는 함수를 구현
# - 데이터 값이 2인 노드 앞에 1.5 데이터 값을 가진 노드를 추가
print("------------------------------")
node_3 = double_linkedlist.search_from_tail(3)
print("node_3.data: ",node_3.data)
double_linkedlist.add_in_front(1.5, 2)
print("------------------------------")
double_linkedlist.desc()


# 연습4: 위코드에서노드 데이터가 특정 숫자인 노드 뒤에 데이터를 추가하는 함수를 만들고 테스트하기
print("------------------------------")
double_linkedlist.add_in_back(2.5, 2)
double_linkedlist.desc()

