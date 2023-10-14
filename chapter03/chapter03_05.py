# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형 (순서X, 키 중복X, 수정O, 삭제O)

# 선언 (키는 어떤 자료형이든 가능)
a = {'name' : 'Kim', 'phone' : '01021346578', 'birth' : '010809'}
b = {0 : 'Hello Python'}
c = {'arr' : [1, 2, 3, 4]} 
d = {
    'Name' : 'Kim',
    'City' : 'Seoul',
    'Age' : 22,
    'Grade' : 'A',
    'Status' : True
}
# dict([(a:b)])
e = dict([
    ('Name', 'Kim'),
    ('City', 'Seoul')
])

# dict(a=b)
f = dict(
    Name='Kim',
    City='Seoul'
)

# 출력
print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)
print(type(f), f)

print(a['name'])    # 존재X -> 에러 발생
print(a.get('name')) # 존재X -> None 처리
print(b[0])
print(b.get(0))
print(f.get('City'))
print(f.get('Age'))

# 딕셔너리 추가
a['address'] = 'seoul'
print(a)
a['rank'] = [1, 2, 3]

# 딕셔너리 수정
a['address'] = 'busan'
print(a)
print(len(a))   # 키의 개수를 셈

a.update(birth='910904')

temp = {'address' : 'goyang'}
a.update(temp)

# 딕셔너리 함수
# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능

# keys() : 딕셔너리 키값들만 가져옴
print(a.keys())
print(list(a.keys()))

# values() : 딕셔너리 값들만 가져옴
print(a.values())
print(list(a.values()))

# items() : 딕셔너리 키와 값을 동시에 가져옴
# 리스트로 둘러쌓인 튜플들로 출력
print(a.items())
print(list(a.items()))
print()

# pop(x) : 속성이 x인 key의 value 꺼내 출력 후 제거
print(a)
print(a.pop('name'))
print(a)
print()

# popitem() : 딕셔너리 마지막 item 제거
print(f.popitem())
print(f)

# in : key를 포함하고 있는지 조회
print('birth' in a) # a에 birth라는 key가 있는지 조회