# # Chapter03-6
# # 파이썬 집합
# # 집합 자료형 (순서X, 중복X, 수정O, 삭제O)

# # 선언 
# a = set()
# b = set([1,2,3,4])
# c = set([1,4,5,6])
# d = set([1,2,'Pen', 'Vap'])
# e = {'fuo', 'bar', 'o', 'love'} # key 없이 value만 나열 = set
# f = {42, 'fuo', (1,2,3,4), 3.141592}

# # 출력
# print(type(a), a)
# print(type(b), b)
# print(type(c), c)
# print(type(d), d)
# print(type(e), e)
# print(type(f), f)

# # 튜플 변환 (set -> tuple)
# t = tuple(b)
# print(type(t), t)

# # 튜플 = 순서O, 중복O -> 인덱싱/슬라이싱 가능
# print(t[0], t[1:3])

# # 리스트 변환 (set -> list)
# l = list(c)
# l2 = list(e)
# print(l, l2)

# # 길이
# print(len(a))
# print(len(b))
# print(len(c))
# print(len(d))
# print(len(e))
# print(len(f))

# # 집합 자료형 활용
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])

# # 교집합 : 집합 & 집합 / intersection()
# print(s1 & s2)
# print(s1.intersection(s2))

# # 합집합 : 집합 | 집합 / union()
# print(s1 | s2)
# print(s1.union(s2))

# # 차집합 : 집합 - 집합 / difference()
# print(s1-s2)
# print(s1.difference(s2))

# # isdisjoint() : 중복 원소 확인
# # True : 교집합 X / False : 교집합 O
# print(s1.isdisjoint(s2))

# # issubset() : 부분 집합 확인
# print(s1.issubset(s2))  # s1이 s2의 부분집합인가

# # issuperset() : issubset() 반대
# print(s1.issuperset(s2)) # s2가 s1의 부분집합인가

# # 추가 & 삭제
# s1 = set([1,2,3,4])

# # add() : 집합에 원소 추가
# s1.add(5)
# print(s1)

# # remove() : 집합에 원소 삭제
# s1.remove(4)
# print(s1)

# # discard() : 집합에 원소 삭제
# # 존재하지 않는 원소 삭제하려고 해도 에러 X
# s1.remove(5)
# print(s1)

# # clear() : 집합에 원소 전체 삭제 (리스트에서도 사용 가능)
# s1.clear()
# print(s1)

a, b = 36, 2
a //= b
print(a)