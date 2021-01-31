# ## 대표적인 데이터 구조6: 해쉬 테이블 (Hash Table)
#
# ### 1. 해쉬 구조
# * Hash Table: 키(Key)에 데이터(Value)를 저장하는 데이터 구조
#   - Key를 통해 바로 데이터를 받아올 수 있으므로, 속도가 획기적으로 빨라짐
#   - 파이썬 딕셔너리(Dictionary) 타입이 해쉬 테이블의 예: Key를 가지고 바로 데이터(Value)를 꺼냄
#   - 보통 배열로 미리 Hash Table 사이즈만큼 생성 후에 사용 (공간과 탐색 시간을 맞바꾸는 기법)
#   - <font color='#BF360C'>단, 파이썬에서는 해쉬를 별도 구현할 이유가 없음 - 딕셔너리 타입을 사용하면 됨</font>

#  python _ dictionary
#  연관 배열(Associative array) 또는 해시(Hash)

# 딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻는다.
# 다음은 기본 딕셔너리의 모습이다.
#
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}
# Key와 Value의 쌍 여러 개가 { }로 둘러싸여 있다. 각각의 요소는 Key : Value 형태로 이루어져 있고 쉼표(,)로 구분되어 있다.
#
# ※ Key에는 변하지 않는 값을 사용하고, Value에는 변하는 값과 변하지 않는 값 모두 사용할 수 있다.

# >>> a = {1: 'a'}
# >>> a[2] = 'b'
# >>> a
# {1: 'a', 2: 'b'}

# >>> a['name'] = 'pey'
# >>> a
# {1: 'a', 2: 'b', 'name': 'pey'}

# case 1_ 해시 테이블 만들기

# list comprehension
#  [출현표현식 for 요소 in 입력sequence [if 조건식]]
#  예) dataset = [4, true, 'dave', 2.1, 3]
#  종류가 다른 데이터에서 정수 리스트만 가져오기
#  int_data = [num for num in dataset if type(num) == int]

hash_table = list([0 for index in range(10)])
print(hash_table)  #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

hash_table = list([index for index in range(10)])
print(hash_table)  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# case 2 : 간단한 해쉬 함수
def hash_func(key):
    return key%5

data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'
print(ord(data1[0]),ord(data2[0]),ord(data3[0]))  # ord : 문자의 ASCII 코드 리턴
print(ord(data1[0]), hash_func(ord(data1[0])))

# 3.3.2. 해쉬 테이블에 값 저장 예
# data:value 와 같이 data 와 value를 넣으면, 해당 data에 대한 key를 찾아서, 해당 key에 대응하는 해쉬주소에 value를 저장하는 예
def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

storage_data('Andy', '01055553333')
storage_data('Dave', '01044443333')
storage_data('Trump', '01022223333')

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print('Andy :', get_data('Andy'))