# Chapter04_02
# 파이썬 반복문
# FOR 실습

# for in <collection>
#       <Loop body>

# 0 ~ 9  
for v in range(10):
    print('v is', v)
print()

# 1 ~ 10
for v in range(1, 11):
    print('v is', v)
print()

for v in range(1, 11, 2):
    print('v is', v)
print()

# 1 ~ 1000까지 합
sum1 = 0
for v in range(1, 1001):
    sum1+=v;
print('1~1000의 sum:', sum1)
print('1~1000까지의 Sum:', sum(range(1, 1001)))
print('1~1000까지 4의 배수의 합 Sum:', sum(range(4, 1001, 4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', "Jung", 'Lee']
for n in names:
    print('You are', n)

# 예제2
lotto_numbers = [11,22,33,44,55,66]
for n in lotto_numbers:
    print('Current number', n)

# 예제3
word = 'Beautiful'
for s in word:
    print('word : ', s)

# 예제4
my_info = {
    "name": "Lee",
    "age": 22
}
for k in my_info:
    print('key: ', k)   # value는 가져오지 않음 (key만 가져옴)
    print(k, '의 value', my_info[k])

for v in my_info.values():
    print('value: ', v)

# 예제5
name = 'FineApplE'
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.isupper())

# break
number = [14,3,4,5,6,7,5,1,12,3,4,8,1,1,24,34, 38, 52]
for n in number:
    if n == 34:
        print('Found 34')
        break
    else:
        print('Not Found')

# continue
lt = ["1", 2, 3.4, True, complex(4)]
for v in lt:
    if type(v) is bool:
        continue
    print('Current type', v, type(v))
    print(True*3)   # True = 1

# for - else
for num in number:
    if num == 241:
        print('Found 241')
        break
else:
    print('Not Found 241')


# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end='')
    print()

# 변환 예제
name2 = 'Aceman'
print('Reversed', reversed(name2))
print('List', list(reversed(name2)))

