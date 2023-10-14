# Chapter02-1-ex1
# 파이썬 완전 기초
# Print 사용법
# 파이썬 3가지 Print Formatting
# 자주 나오는 질문 참고

"""
참고: Escapte 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000: 널 문자
"""

### 3 가지 Format Practices
x = 50
y = 100
text = 308213565
n = 'Lee'

# 출력1
ex1 = 'n = %s, s = %s, sum = %d' % (n, text, (x+y))
print(ex1)

# 출력2
ex2 = 'n = {n}, s = {s}, sum = {sum}' .format(n=n, s=text, sum=x+y)
print(ex2)

# 출력3 (f스트링 방식 = f'')
ex3 = f'n = {n}, s = {text}, sum = {x+y}'
print(ex3)



# 구분기호
m = 1000000000

# 천 단위를 기준으로 , 붙여 출력
print(f'm: {m:,}')
print()



# 정렬
# ^ : 가운데(중앙) / < : 왼쪽 / > : 오른쪽 
t = 20

# 열자리 확보하고 왼쪽은 공백으로 채움
print(f't: {t:10}')
print(f't center: {t:^10}')
# 왼쪽 정렬 (오른쪽에 공백으로 채움)
print(f't: {t:<10}')
# 오른쪽 정렬 (왼쪽에 공백으로 채움)
print(f't: {t:>10}')
# 공백을 -로 채움
print(f't center: {t:-^10}')