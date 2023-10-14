# Chapter03_5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형 (순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name' : 'Kim', 'phone' : '01044447777', 'birth' : '020115'}   
b = {0 : 'Hello Python'}
c = {'arr' : [1, 2, 3, 4]}
d = {
    'Name' : 'Niceman',
    'City' : "Seoul",
    'Age' : 33,
    'Grade' : 'A',
    'Status' : True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', "Seoul"),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()


# 출력
print('a - ', a['name'])    # 존재 x -> 에러 발생
print('a - ', a.get('name'))   # 존재 x -> None 처리
# 둘이 같은 결과 나옴.
# 위에꺼는 만약 name1로 쓰면 해당 키 값이 없으니 에러남. but, 아래는 에러 안나고 None으로 출력됨 (좀 더 안정적이라 get을 더 많이 씀)

print('b - ', b[0])
print('b - ', b.get(0))

print('f - ', f.get('City'))
print('f - ', f.get('Age'))


# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)

a['name'] = 'Yoo'   # 수정됨
print('a - ', a)

a['rank'] = [1,2,3]
print('a - ', a)

print('a - ', len(a)) 


# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능

print('a - ', a.keys())    # key값들만 가져옴 
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', list(a.keys())) 
print('b - ', list(b.keys()))

print()

print('a - ', a.values())    # values값들만 가져옴 
print('b - ', b.values())
print('c - ', c.values())

print('a - ', list(a.values())) 
print('b - ', list(b.values()))

print()

print('a - ', a.items())    # key, values 전체 가져옴 
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items())) 
print('b - ', list(b.items()))

print()

print('a - ', a.pop('name'))
print('a - ', a)

print()

print('f - ', f.popitem())  # 아무거나 하나를 꺼내서 뺌
print('f - ', f)

print()


print('a - ', 'birth' in a)   # birth 라는 키가 있으면 true
print('a - ', 'City' in d)


# 수정
a['test'] = 'test_dict'

print('a - ', a)    # 추가 됨

a['address'] = 'dj'
print('a - ', a)

a.update(birth = '000000') 
print('a - ', a)

temp = {'address' : 'Busan'}
a.update(temp)
print('a - ', a)