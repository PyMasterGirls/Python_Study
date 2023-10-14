# Chapter04-03
# 파이썬 반복문
# While 실습

# while <expr>:
#       <statement(s)>

# 예제1
n = 5
while n>0:
    n = n - 1
    print(n)

# 예제2
a = ['Fuo', 'bar', 'o']
while a:
    print(a.pop())

# 예제3
# break, continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended')

m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended')

# if 중첩
# 예제5
i = 1
while i<=10:
    print('i:', i)
    if i==6:
        break
    i+=1

# while - else
# 예제6
n = 10
while n>0:
    n -=1
    print(n)
    if n==5:
        break
else:   # while문에서 break으로 빠져나가지 못하면 else문 수행
    print('else out.')

# 예제7
a = ['foo', 'bar', 'o', 'qux']
s = 'qux'

i = 0
while i < len(a):
    if a[i] == s:
        break
    i+=1
else:
    print(s, 'not found in list.')

# 무한반복
# while True:

# 예제8
while True:
    if not a:
        break
    print(a.pop())