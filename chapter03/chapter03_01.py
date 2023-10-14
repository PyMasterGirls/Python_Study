# Chapter03-1
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열 (시퀀스)
list : 리스트 (시퀀스)
tuple : 튜플 (시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = "Anaconda"
float_v = 10.0    # 10 != 10.0 
int_v = 7
list = [str1, str2]
print(list)

dict = {
    "name" : "Machine Learning",
    "version" : 2.0
}
print(dict)

# 리스트와 유사하나 소괄호를 사용 (리스트는 대괄호)
tuple = (7, 8, 9) # 괄호 없이도 사용 가능

# 리스트와 유사하나 중괄호 사용 (리스트는 대괄호)
set = {7, 8, 9}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs : 절댓값
pow(x, y) : x**y (x의 y 제곱)
"""

# 정수 선언
i = 77
i2 = -14
big_int = 11111111111111111111111111111111111111111111

# 정수 출력
print(i)
print(i2)
print(big_int)

f = 0.9999
f2 = 3.141592
f3 = -3.9

print(f)
print(f2)
print(f3)

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 1111111111111111111111111111
big_int2 = 12222222222222222222222222222

# 서로 다른 타입끼리 계산할 때 자동으로 형변환 이루어짐
print("i1 + i2 : ", i1 + i2)

# 형 변환 실습
a = 3.  # 3.0 의미 (0은 생략 가능)
b = 6
c = .7  # 0.7 의미
d = 12.7

# 형 변환
print(float(b))
print(int(c))
print(int(c))
print(int(True))
print(float(False))
print(complex(3))
print(complex('3'))
print(complex(False))

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)   # divmod() : 몫과 나머지를 구하는 함수
print(x, y)
print(pow(5,3)) # print(5**3)과 동일

# 외부 모듈
import math

# x 이상 수 중에서 가장 작은 정수 
print(math.ceil(5.1))

# 원주율 출력
print(math.pi)