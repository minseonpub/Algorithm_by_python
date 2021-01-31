
## chapter6. 스택
# * 데이터를 제한적으로 접근할 수 있는 구조(한쪽 끝에서만 자료를 넣거나 뺄 수 있는 구조)
# 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조
#   - 큐: FIFO 정책
#   - 스택: LIFO 정책

# 스택은 LIFO(Last In, Fisrt Out) 또는 FILO(First In, Last Out) 데이터 관리 방식을 따름
# push(): 데이터를 스택에 넣기
# pop(): 데이터를 스택에서 꺼내기

# 스택은 컴퓨터 프로세스 실행구조의 가장 기본이며, 함수 호출시의 구조와 유사하다.
# 파이썬 재귀함수는 1000번까지만 호출 가능
def recursive(data):
    if data <0:
        print("ended")
    else:
        print(data)
        recursive(data-1)
        print("returned", data)

recursive(4)
# 4
# 3
# 2
# 1
# 0
# ended
# returned 0
# returned 1
# returned 2
# returned 3
# returned 4

# 파이썬 리스트 기능에서 제공하는 메서드로 스택 사용
data_stack = list()
data_stack.append(1)
data_stack.append(2)

print(data_stack) #[1, 2]
print(data_stack.pop()) # 2

# 연습1: 리스트 변수로 스택을 다루는 pop, push 기능 구현해보기 (pop, push 함수 사용하지 않고 직접 구현해보기)
data_stacklist = list()
def push(data):
    data_stacklist.append(data)

def pop():
    data = data_stacklist[-1]  # 리스트의 크기와 상관 없이 맨 끝 index는 -1
    del data_stacklist[-1]
    return data

for index in range(10):
    push(index)
print(data_stacklist) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(pop()) #9

