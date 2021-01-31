
# ** 파이썬 객체지향 문법
# class 란 속성(attribute)와 동작(method)를 갖는 데이터 타입
# object란 선언된 클래스를 기반으로 만들어진 실체(객체 or 인스턴스) _ 하나의 클래스를 기반으로 수많은 객체 생성 가능
# 속성은 변수, 동작은 함수와 유사하다.

#  객체지향 프로그램 작성 방법
#  1. 클래스설계(attribute와 method로 구성)
#  2. 설계한 클래스를 기반으로 클래스를 코드로 작성
#  3. 클래스를 기반으로 필요한 객체 생성
#  4. 해당 객체의 attribute와 method를 조작해 프로그램 수행

# 예제1) 객체 생성 전 class 미리 선언

# class에 attribute와 method를 안넣은 상태임으로 임의로 pass를 넣어 선언 끝났음을 알려줌.
class Quadrangle:
    pass # 아무것도 수행안함. 임시코드시 주로 사용

class SingleWord:
    pass

print(dir(SingleWord))

# 만들어진 클래스로 객체 만들기 가능
square = Quadrangle()
print(type(square)) #<class '__main__.Quadrangle'>

## 예제2) attribute 넣기 (width, height, color)
class Quadrangle:
    width = 0
    heigh = 0
    color = "black"

class Dave:
    data = 0
    name = 'dave'

print(dir(Dave)) # 추가로 attribute가 생긴것을 확인 할 수있다.

square = Quadrangle()
print(square.width)
square.width = 100
print(square.width)


# 초간단 연습 :
# width, heigh, color 속성을 가진 사각형 클래스를 만들고 4개의 객체를 만든다.
# 직사각형 1개 객체 속성 width = 10, height = 5, color = 'red'
# 정사각형 1개 객체 속성 width = 7, height = 7, color = 'blue'
class Nemo:
    width = 0
    height = 0
    color = 'None'

square1 = Nemo()
square2 = Nemo()

square1.width = 10
square1.height = 5
square1.color = 'red'

square2.width = 7
square2.height = 7
square2.color = 'blue'

print(square1.width, square1.height, square1.color) # 10 5 red
print(square2.width, square2.height, square2.color) # 7 7 blue


## 예제3) method 넣기 _ 사각형 넓이 구하기
class Nemo:
    width = 0
    height = 0
    color = 'None'

    def area(self):
        # 파이썬은 항상 첫번째 파라미터로 self를 사용하며, 인자가 없을 경우도 self는 사용
        # 클래스의 attribute는 내부에서 접근시 self.attribute로 접근
        return self.width * self.height

    def set_area(self, width, height):
        self.width = width
        self.height = height

square1 = Nemo()

square1.width = 10
square1.height = 5
square1.color = 'red'

print(square1.area()) #50

# 객체의 mehtod에 접근하기 _ 객체명.method명
square3 = Nemo()
square3.set_area(10, 10)
print(square3.area()) # 100


# 초간단 연습 2
# 위에서 작성한 클래스를 기반으로 직사각형 1개 객체, 정사각형 1개 객체를 만들고, 각 사각형 너비 출력하기
class Quadrangle:
    width = 0
    height = 0
    color = 'None'

    def area(self):
        # 파이썬은 항상 첫번째 파라미터로 self를 사용하며, 인자가 없을 경우도 self는 사용
        # 클래스의 attribute는 내부에서 접근시 self.attribute로 접근
        return self.width * self.height

    def set_area(self, width, height):
        self.width = width
        self.height = height

    def set_areaPlue(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

square01 = Quadrangle()
square02 = Quadrangle()

square01.set_areaPlue(10, 5, 'red')
square02.set_areaPlue(7,7,'blue')

print("직사각형 너비: ", square01.area())
print("정사각형 너비: ", square02.area())


# 한발짝 더~(심화문제)
# 위에서 작성한 클래스를 기반으로 직사각형 1개, 정사각형 1개를 만들되, 너비, 높이, 색상을 한번에 설정할 수 있는 메소드 만들고
# 각 객체의 속성값을 변경 후, 너ㅂ와 색상도 함께 출력하기.
print("직사각형 너비: ", square01.area(), " 색상 : ", square01.color)
print("정사각형 너비: ", square02.area(), " 색상 : ", square02.color)


# 생성자와 소멸자
# 생성자는 객체 생성시 자동 호출, 소멸자는 객체 소멸시 자동 호출
# 생성자(__init__(self))
class Quadrangle_init:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def __del__(self):
        print("Quadrangle object is deleted")

square = Quadrangle_init(5,5,'red')
del square # 객체 삭제


# 초간단 연습
# 정삼각형 클래스를 만들고, 정삼각형 이름하기
# attribute : 정삼각형 한변의 길이, 정삼각형 이름
# method : 정삼각형 이름 리턴, 너비 리턴
# 생성자에서 attribute 값 설정
# 소멸자 작성 후, 객체 소멸시 object is deleted 출력
import math

class Triangle:
    def __init__(self, length, name):
        self.length = length
        self.name = name

    def __del__(self):
        print("object is deleted")

    def call_name(self ):
        return self.name

    def get_area(self):
        return math.sqrt(3)/2* math.pow(self.length,2)
#       return math.sqrt(3)/2*self.length**2

tri = Triangle(10, "triangle")
print("정삼각형 너비 : ", tri.get_area())
print("정삼각형 이름 : ", tri.call_name())


# # 예제로 이해하는 객체지향 문법(public, private, protected)
# private -> protected-> public
# class 의 attribute, method에 접근을 제어할 수 있는 기능
# private : 해당 클래스에서만 접근 가능
# protected : 해당 클래스 혹은 상속 클래스에서만 접근 가능
# public : 어떤 클래스라도 사용 가능

# 파이썬에서는 모든 attribute, method는 public(외부에서 접근 가능)

#2) protected
class Quadrangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def __del__(self):
        print("Quadrangle object is deleted")

    def _set_area(self):        # _(single underscore)를 붙여 표시, 실제 제약은 않고 경고표시
        return self.width * self.height

#3) private
class Quadrangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def __del__(self):
        print("Quadrangle object is deleted")

    def __set_area(self):  # __(double underscore)를 붙여 표시
        # 실제로 해당이름이 classname으로 변경되어 접근 허용 안됨.
        return self.width * self.height


# 심화문제
# 원 클래스 만들기
# attribute : 원 반지름, 원 이름
# method :
# 1. 원 이름 리턴 메소드
# 2. 원 넓이 리턴 메소드
# 3. 원 길이 리턴 메소드(생성자에서만 attribute 설정가능(private))

class Circle:
    def __init__(self, round, circle_name):
        self.__round = round
        self.__circle_name = circle_name
    def __del__(self):
        print("object is ended")
    def get_named(self):
        return self.__circle_name
    def get_area(self):
        return math.pi*(self.__round**2)
    def get_length(self):
        return 2*math.pi*self.__round

mini_circle = Circle(3, 'dave')
print("원 이름: ", mini_circle.get_named(), "\n원 너비: ", mini_circle.get_area(), "\n원 길이: ",mini_circle.get_length() )

#assign 01
# 1. 과제관리 class 작성하기
#     - attribute : 계좌 초기 금액을 속성으로 하나 설정
#     - 생성자에서 초기금액은 0으로 설정
#     - 속성은 private로 설정
#     - method: 인출, 저축, 잔액 확인 3가지 method 구현, 각각 현재 계좌 금액 리턴
#     - 각 method도 private로 설정

class Assign:
    def __init__(self):
        self.__mymoney = 0  ## 현재 잔고

    def __del__(self):
        print("Thank you for using our bank!")

    def __withdraw(self, money):
        self.__mymoney -= money
        return self.__mymoney

    def __insert(self, money):
        self.__mymoney += money
        return self.__mymoney

    def __checkmycount(self):
        return self.__mymoney

