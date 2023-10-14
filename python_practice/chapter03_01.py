# Chapter03_01
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
str2 = 'Anaconda'
float_v = 10.0    # 10 != 10.0 (타입이 다름)
int_v = 7
list = [str1, str2]
dict = {
    "name" : "Machine Learning",
    "version" : 2.0
}  # key : value

tuple = (7, 8, 9)   # 괄호 없이 , 로 나열해도 인식힘
set = {3, 5, 7}

print(type(str1))
print(type(bool))
print(type(str2))
print(type(str1))
print(type(float_v))
print(type(int_v))
print(type(dict))

print(list)

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) : x의 y 제곱 == x ** y
"""

# 정수 선언
i = 77
i2 = -14
big_int = 8890898908098908908989089898908098000000098888888  # 큰 수도 그냥 할당 가능

# 정수 출력
print(i)
print(i2)
print(big_int)
print()

# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)
print()


# 연산 실습
i1 = 39
i2 = 939
big_int1 = 877897897878978978979070979089078969869623242355
big_int2 = 926746278364286489289032583450938590290859082903
f1 = 1.234
f2 = 3.939

# +
print(">>>>+")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)
print()

a = 3 + 1.0     # 4.0 -> 자동으로 실수형으로 변환됨

# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7    ## b 빼고 다 실수

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b))     # 6.0
print(int(c))       # 0
print(int(d))       # 12
print(int(True))    # 1
print(float(False)) # 0.0
print(complex(3))   # 복소수 (3+0j)
print(complex('3')) # 위와 같음. 문자형 -> 숫자형으로 바꾼 후에 실행됨.
print(complex(False)) # 0j
print()


# 수치 연산 합수
print(abs(-7))      # 절대값

x, y = divmod(100, 8)   # 100을 8로 나눈 후 몫을 x에 나머지를 y에
print(x, y)

print(pow(5,3), 5 ** 3)


# 외부 모듈 (패키지)
import math

print(math.ceil(5.1))     # x 이상의 수 중에서 가장 작은 정수 -> 6
print(math.pi)     # 원주율 나옴