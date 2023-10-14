# 파이썬 완전 기초
# Print 사용법

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자

"""

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print() # 줄바꿈

# separator 옵션 (구분자)
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')
print()

# file 옵션
import sys

print('Learn Python', file=sys.stdout)
print()

# format 사용(d, s, f) d-> 정수 s-> 문자열 f-> 실수
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))  # 위와 같음. 가독성 더 좋고 유연
print('{} {}'.format('one', 2))
print('{1} {0}'.format('one', 'two'))   # two one

print()

# %s
print('%10s' % ('nice'))    # 10개의 자리 (왼쪽부터 공백처리) ______nice (_부분이 공백)
print('{:>10}'.format('nice'))   # 위와 같음

print('%-10s' % ('nice'))    # 10개의 자리 (왼쪽부터 공백처리) nice______ (_부분이 공백)
print('{:10}'.format('nice'))   # 위와 같음

print('{:$>10}'.format('nice'))   # 공백부분을 원하는 기호로 넣을 수 있음 $$$$$$nice
print('{:^10}'.format('nice'))    # 중앙 정렬 nice를 10자리 중 가운데로 정렬해줌

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))   # pytho 만 출력됨. 즉 5자리의 공간에 맞게 문자열 자름 (.없으면 문자열 전체 걍 다 들어옴)
print('{:10.5}'.format('pythonstudy'))  # 10글자 자리 중 5개만 출력 pytho 출력됨

print()

# %d
print('%d %d' % (1,2))     # 1 2 출력됨
print('{} {}'.format(1,2)) # 위와 같음

print('%4d' % (42))     # __42 (_는 공백)
print('%4d' % (43243432)) # 그대로 다 출력됨
print('{:4d}'.format(42)) # 정수일때는 d 넣어줘야함

print()

# %f
print('%f' % (3.141343434334))     # 소수점 6자리 정도까지 출력됨
print('%1.8f' % (3.141343434334))  # 정수부 1자리, 소수부는 8자리까지 나와라
print('%06.8f' % (3.141343434334)) #..?
print('{:f}'.format(3.141343434334))

print('%06.2f' % (3.1241592653589793))   # 정수부 6자리 소수부2자리...? 결과는 003.14로 나옴.
# 총 6자리. 정수부 1자리밖에 없으니 앞에 나머지 0으로 채워주고(6앞에 0이 있어서 0으로 채워줌. 없으면 공백) 소수부 2자리 와 .을 합쳐서 총 6자리
print('{:06.2f}'.format(3.1241592653589793))


