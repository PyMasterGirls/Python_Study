# Chapter06-1
# 파이썬 클래스 
# OOP (객체 지향 프로그래밍), 인스턴스 메소드, 인스턴스 변수

# 클래스(틀) and 인스턴스 (클래스를 가지고 코드에서 사용하는 어떤 객체/ 틀을 바탕으로 구현한 것) 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간 (딕셔너리 형태로 반환)
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1
class Dog: #object tkdthr
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)  # <class '__main__.Dog'>

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)
c = Dog("mikky", 2)

# 비교
print(a == b, id(a), id(b), id(c))  # 다 다른 id (전혀 다른 객체)

# 네임스페이스
print('dog1', a.__dict__)   # dog1 {'name': 'mikky', 'age': 2} 속성 등이 나옴
print('dog1', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)


# 예제2
# self의 이해
class SelfTest: # 안에 __init__ 없으면 파이썬이 내부적으로 알아서 해줌
    def func1():   # 클래스 메소드
        print('Func1 called')

    def func2(self):  # 클래스로 생성한 인스턴스화 시킨 변수가 이 self로 넘어옴 (인스턴스 메소드)
        print(id(self))
        print('Func2 called')

f = SelfTest()

# print(dir(f))   # 사용할 수 있는 메소드들 출력
print(id(f))
# f.func1() -> 에러 # 예외
f.func2()

SelfTest.func1() # -> 에러 안남. 클래스로 바로 접근
# SelfTest.func2() # -> 에러. 
SelfTest.func2(f) # -> 에러 안남. 


# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0  # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
# Warehouse.stock_num = 50
print(user1.stock_num)
print()
print(user1.name)
print(user2.name)
print()
print(user1.__dict__) # 여기에는 stock_num 안들어있음. 즉, stock_num은 Warehouse에서 알아서 찾아서 가는 것. 어짜피 모두가 공유하는 것이기 때문에 굳이 표시 안함
print(user2.__dict__)
print('before', Warehouse.__dict__)

print()

del user1
print('after', Warehouse.__dict__)
print()

# 예제4
class Dog2: #object tkdthr
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)
    
# 인스턴스 생성
c = Dog2('july', 4)
d = Dog2('Marry', 10)
# 메소드 호출
print(c.info())
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))