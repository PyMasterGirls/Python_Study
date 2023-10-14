# Chapter03_4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x)   # 불변

# 선언
a = ()
b = (1, 2)
# 주의!!! 원소가 하나일때 b = (1) -> int 형으로 인식함. 따라서 b = (1,) 꼭 콤마를 찍어야함!
# 괄호 없이 1, 2, 3 이렇게 선언해도 튜플!!

c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))


# 인덱싱
print('>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])   # 100 + 1000 + 1000 = 2100
print('d - ', d[-1])
print('e - ', e[-1])    # ('Ace', 'Base', 'Captine')
print('e - ', e[-1][1]) # Base
print('e - ', list(e[-1][1]))   # 리스트로 형 변환됨!!


# 수정 x
# d[0] = 1500
# -> 에러남.


# 슬라이싱
print('>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])


# 튜플 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)


# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)

print('a - ', a.index(3))   # 숫자 3이 들어간 위치
print('a - ', a.count(2))   # 숫자 2의 개수


# 팩킹 & 언팩킹(Packing, and Unpaking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')    # 4개의 원소를 하나로 묶음 -> 팩킹

# 언팩킹1
(x1, x2, x3, x4) = t

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)   
# 묶여있던 4개의 원소가 각각 변수로 할당됨. -> 언팩킹
# foo bar baz qux


# 팩킹
t2 = 1, 2, 3
t3 = 4,

# 언팩킹
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)