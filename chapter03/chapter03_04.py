# Chapter03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형 (순서O, 중복O, 수정X, 삭제X) -> 연산은 가능
# 불변

# 선언 : 소괄호 사용
a = ()
# 원소가 하나일 땐 (1,)로 
# (1)은 int형
b = (1,)
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine')) # 튜플 안의 튜플도 가능

# 출력
print('>>>>>>>>>>>>>>')
print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)

# 인덱싱
print('>>>>>>>>>>>>>>')
print(d[1])
print(d[0] + d[1])
print(d[-1])
print(e[-1])
print(e[-1][1])
print(list(e[-1][1]))   # 불변 속성 사라짐

# 수정 X
# 튜플은 수정 안된다는 타입 에러 발생
# d[0] = 1500

# 슬라이싱
print('>>>>>>>>>>>>>>')
print(d[0:3])
print(d[2:])
print(e[2][1:3])

# 튜플 연산
print('>>>>>>>>>>>>>>')
print(c + d)
print(c * 6)

# 튜플 함수
print('>>>>>>>>>>>>>>')
a = (5, 1, 2, 3, 4)
print(a.index(3))
print(a.count(2))

# 팩킹 & 언팩킹 (Packing and Unpacking)
print('>>>>>>>>>>>>>>')

# 팩킹 (하나로 묶다)
t = ('foo', 'bar', 'o', 'love')

# 언팩킹1 (묶여있던걸 풀어서 하나씩 할당)
(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹 & 언팩킹
t2 = 1, 2, 3    # 소괄호 없어도 튜플 (괄호 생략 가능)
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6
print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)