# Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형 (순서O, 중복O, 수정O, 삭제O)

# 리스트 선언
a = []
print(type(a))
b = list()
c = [1, 2, 3, 4, 5]
print(len(c))
d = [1000, 100000, 'Ace', 'Base', 'Captine']    # 서로 다른 자료형 담을 수 있음
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>>>>>>>>>>>>')
print(d)
print(d[0] + d[1])
print(d[-1])
print(e[-1][1])
print(list(e[-1][1]))   # 리스트로 형 변환

# 슬라이싱
print('>>>>>>>>>>>>>>>>')
print(d[0:3])
print(d[2:])
print(e[-1][1:3])

# 리스트 연산
print('>>>>>>>>>>>>>>>>')
print(c+d)
print(c*3)
print('Test + c[0]', 'Test' + str(c[0]))

# 값 비교
print('>>>>>>>>>>>>>>>>')
print(c == c[:3] + c[3:])

# Identity(id)
print('>>>>>>>>>>>>>>>>')
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정
print('>>>>>>>>>>>>>>>>')
c[0] = 4
print(c)

# 리스트와의 연산은 리스트로 해야함
# c[1]에 리스트가 들어가는게 아님
c[1:2] = ['a', 'b', 'c']
print(c)

# 이땐 리스트로 들어감
c[1:2] = [['a', 'b', 'c']]
print(c)

# 슬라이싱은 원소가 들어가지만 정확한 인덱스에는 리스트가 들어감
c[1] = ['a', 'b', 'c']
print(c)

# 리스트 삭제
print('>>>>>>>>>>>>>>>>')
c[1:3] = []
print(c)

del c[2]
print(c)

# 리스트 함수
print('>>>>>>>>>>>>>>>>')
a = [5, 2, 3, 1, 4]
print(a)

# append() : 리스트 뒤에 원소 추가
a.append(10)
print(a)

# sort() : 오름차순 정렬
a.sort()
print(a)

# reverse() : 내림차순 정렬
a.reverse()
print(a)

# index(x) : x번째 원소 가져옴
print(a.index(1))

# insert(x, y) : x번째 자리에 y 삽입 + (x+1) 자리부터 한칸씩 뒤로 밀기
print(a)
a.insert(2, 7)
print(a)

a.reverse()
print(a)

# remove(x) : 리스트에서 제일 처음으로 나온 x 삭제
a.append(5)
a.append(10)
a.remove(10)
print(a)

# pop() : 기존 리스트 마지막 원소 출력 후 제거
print(a.pop())
print(a)

# count(x) : 리스트에서 x의 값이 몇 개 있는지
print(a.count(4))

# extend(list) : 리스트 마지막에 리스트 원소 추가
ex = [8, 9]
a.extend(ex)
print(a)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)