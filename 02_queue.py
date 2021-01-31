# chapter5. 큐
import queue    # 일반적인 FiFO를 따르는 Queue 뿐만 아니라 다양한 Queue지원
data_queue = queue.Queue() #일반적 FIFO Queue
# data_queue.put() # queue 넣기
data_queue.put("funcoding")
data_queue.put('a')

# data_queue.qsize() : qsize: 큐의 크기
print(data_queue.qsize())  # 2

# data_queue.get() # queue 빼기
print(data_queue.get()) # funcoding
print(data_queue.qsize()) #1

#LIFO (LIFOQueue)
import queue
data_lifoqueue = queue.LifoQueue()
data_lifoqueue.put("funcoding")
data_lifoqueue.put('a')

print(data_lifoqueue.get()) # a가 출력


#PriorityQueue() : 우선순위를 부여해서 데이터 추출 순서를 선택(중요)
import queue
data_priorityqueue = queue.PriorityQueue()
data_priorityqueue.put((10,"korea"))   #((priority, data)) : 순으로 작성 (튜플형식이라 괄호 2개)
data_priorityqueue.put((5,1))
data_priorityqueue.put((15,"china"))

print(data_priorityqueue.qsize())
print(data_priorityqueue.get()) #(5, 1)
print(data_priorityqueue.get()) #(10, 'korea')


# 연습1: 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기
queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
#   FIFO
    data = queue_list[0]
    del queue_list[0]   # del : 삭제
    return data

for index in range(10):
    enqueue(index)

print(len(queue_list)) #10
print(dequeue()) #0
