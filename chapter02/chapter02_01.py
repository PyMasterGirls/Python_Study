# Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# Ctrl + F5로 실행

# 기본 출력
print('Python start!')
print("Python start!")
print('''Python start!''')
print("""Python start!""")

print()

# Separator 옵션 (원하는 형식으로 출력하고 싶을 때)
# 분리해서 출력
print('P','Y','T','H','O','N')

# 분리된 값에 sep 을 붙여 출력
print('P','Y','T','H','O','N', sep=',')
print('010', '1234', '5678', sep='-')

# end 옵션
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')


# file 옵션
import sys

# 콘솔에 출력
print('Learn Python', file=sys.stdout)

# format 사용 (d, s, f)
print('%s %s' % ('one', 'two'))

# 암묵적으로 index는 0부터 출발하니까 {0} = one / {1} = 2
print('{} {}' .format('one', '2'))
# 순서 지정도 가능 {1} = two / {0} = one
print('{1} {0}' .format('one', 'two'))


# %s
# 양수 or >(왼쪽): 총 열자리를 확보하고 왼쪽부터 공백으로 채우면서 문자열 출력
print('%10s' % ('nice'))
print('{:>10}' .format('nice'))

# 음수 or <(오른쪽 = 생략 가능): 총 열자리를 확보하고 문자열 출력 후 오른쪽을 공백으로 채움
print('%-10s' % ('nice'))
print('{:10}' .format('nice'))

# 공백을 _로 채움
print('{:_>10}' .format('nice'))

# ^: 중앙 정렬 (열자리 중 중앙에 위치)
print('{:^10}' .format('nice'))

# 내가 원하는 자리수만 왼쪽부터 출력하고 slicing
print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))

# 총 열개의 자리수를 차지하되 왼쪽부터 5개만 출력
print('{:10.5}' .format('pythonstudy'))


# %d
print('%d %d' % (1, 2))
print('{} {}' .format(1, 2))

# 있는 값이 그대로 출력
print('%4d' % (42))
# 주어진 값의 길이가 할당된 길이보다 길다면 전체를 출력
print('%5s' % ('sdfkljapfjaidsjfaisjdfio;asjdfi'))
print('%4d' % (42316516165))

# 문자열인 경우엔 s를 안붙여도 괜찮 / 정수는 d를 붙여야함
# 정수는 부등호 생략하면 왼쪽부터 공백을 채움
# 문자열은 부등호 생략하면 < 의미 -> 오른쪽을 공백으로 채움)
# 문자열은 기본적으로 왼쪽 정렬 숫자는 오른쪽 정렬 (나머지는 빈칸으로 채움)
print('{:4d}' .format(42))
print('{:4s}' .format('nices'))


# %f
# 소숫점 아래 6자리까지 출력
print('%f' % (3.140312133131301))
print('{:f}' .format(3.16484651487))

# 정수부는 한자리 소수부는 8자리까지 출력
print('%1.8f' % (3.146464646446514654))
# 소수부가 18자리보다 적은 경우 의미없는 수로 채움
print('%1.18f' % (3.146464646446514654))

# 총 여섯자리를 출력하되(소수점 포함) 
# 소숫점 아래 두자리까지 출력 (나머지는 0으로 채움)
print('%06.2f' % (3.141592653589723))
print('{:06.2f}' .format(3.141592653589723))