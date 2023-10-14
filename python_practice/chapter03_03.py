# Chapter03_3
# 파이썬 리스트
# 자료구조에서 중요
# 배열이 즉, 리스트
# 리스트 자료형 (순서o, 중복o, 수정o, 삭제o)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']    # 서로 다른 자료형이 담길 수 있음.
e = [1000, 10000, ['Ace', 'Base', 'Captine']]  # 리스트 안에 리스트 넣을 수 있음
f = [21.42, 'footbar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])     # 10000
print('d - ', d[0] + d[1] + d[1])   # 저절로 int로 계산
print('d - ', d[-1])    # Captine
print('e - ', e[-1][1]) # Base
print('e - ', list(e[-1][1])) # ['B', 'a', 's', 'e'] ** ['Base']를 원하면 새로 배열 만들고 .append()
print('e - ', list(e[-1][1:3])) # e -  ['Base', 'Captine']


# 슬라이싱
print(">>>>>")
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])


# 리스트 연산
print('>>>>>>')
print('c + d', c + d)      # 두 리스트 합쳐짐. c 뒤에 d
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))   # 타입 에러남. 따라서 c[0]를 str로 변환


# 값 비교
print(">>>>>>")
print(c == c[:3] + c[3:]) # True [70, 75, 80, 85]
print()

# Identity (id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))    # 둘이 같은 id 값을 가짐. 같은 객체를 가르킴


# 리스트 수정, 삭제
print(">>>>>")
c[0] = 4
print('c - ', c)

c[1:2] = ['a', 'b', 'c']
print('c - ', c)    # c -  [4, 'a', 'b', 'c', 80, 85]

c[1:2] = [['a', 'b', 'c']]
print('c - ', c)    # c -  [4, ['a', 'b', 'c'], 80, 85]

c[1] = ['a', 'b', 'c']
print('c - ', c)    # c -  [4, ['a', 'b', 'c'], 80, 85] (하나의 원소로 들어감)

c[1:3] = []
print('c - ', c)    # 인덱스 1,2부분 삭제됨 
# 삭제
del c[2]    # index 번호를 알아야 가능
print('c - ', c)
print()


# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a - ', a)

# a[5] = 10 -> 삽입 안됨. a[4] = 10 -> 수정됨. => 직접적인 삽입은 수정할 때만!

a.append(10)    # 끝부분에 데이터 삽입.
print('a - ', a)

a.sort()        # 오름차순 정렬로 바꿈
print('a - ', a)

a.reverse()     # 내림차순 정렬로 바꿈
print('a - ', a)
# sort, reverse -> 데이터가 많을 수록 상당히 오래걸리는 작업.

print('a - ', a.index(3), a[3])

a.insert(2, 7)   # insert(원하는 위치, 삽입할 값) 인덱스2에 7이 추가되고 나머지들은 뒤로 다 밀림
print('a - ', a)  

a.remove(10)    # 리스트 중 10의 값을 삭제
print('a - ', a)

print('a - ', a.pop())  # 마지막 원소를 꺼내서 삭제
print('a - ', a)

print('a - ', a.count(4))   # 4의 개수가 몇개인지 구함

ex = [8, 9]
a.extend(ex)
print('a - ', a)    # a 뒤에 , 8, 9] 이렇게 들어감


# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)