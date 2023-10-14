# 파이썬 완전 기초
# Print 사용법 (2023년 추가)
# 파이썬 3가지 Print Formatting
# 자주 나오는 질문 참고

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자

"""

### 3가지 Format Practices

x = 50
y = 100
text = 308276567
n = 'Lee'

## 주로 2,3번 사용
# 출력1
ex1 = 'n = %s, s = %s, sum = %d' % (n, text, (x + y))
print(ex1)

# 출력2
ex2 = 'n = {n}, s = {s}, num = {sum}'.format(n=n, s=text, sum=x+y)
print(ex2)

# 출력3
ex3 = f'n = {n}, s = {text}, sum = {x + y}'     ## f'~~~'
print(ex3)


# 구분 기호
m = 100000000

print(f'm : {m:,}')     ## 알아서 구분 기호로 표시남 m : 100,000,000

print()
print()

# 정렬
# ^ : 가운데 정렬, < : 왼쪽 정렬, > : 오른쪽 정렬 ## 숫자 -> 오른쪽 정렬이 기본, 문자 -> 왼쪽 정렬이 기본

t = 20

print(f"t : {t:10}")   ## 자리수 10칸
print(f"t center : {t:^10}")
print(f"t center : {t:<10}")
print(f"t center : {t:>10}")


print()
print()

print(f"t center : {t:-^10}")  ## 빈칸을 - 기호로 채워줌 => t center : ----20----
print(f"t center : {t:#<10}")