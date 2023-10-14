# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n))  ## <class 'int'>

print()

# 동시 선언
x = y = z = 700
print(x, y, z)

print()

# 선언
var = 75

# 재선언
var = "Change Value"

# 출력
print(var)
print(type(var))    ## str

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))    # 요게 내부적으로 자동으로 일어나는게 위에 있는 식!

print()

# 예2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n
# m -> 777 <- n

print(m, n)
print(type(m), type(n))
print()

m = 400
print(m, n)
print(type(m), type(n))
print()

n = 400
print(m, n)
print(type(m), type(n))
print()

# id(identity) 확인 : 객채의 고유값 확인

m = 800
n = 655

print(id(m))    ## 4377138832
print(id(n))    ## 4377138928   즉, 둘이 서로 다름
print(id(m) == id(n))
print()


# 같은 오브젝트 참조
m = 800
n = 800

print(id(m))    ## 4312962704
print(id(n))    ## 4312962704   즉, 둘이 서로 같음 
print(id(m) == id(n))
print()

## 같은 값일때 같은 id. but, 값이 달라지게 된다면 id값 달라짐! 효율성, 생산성, 속도 때문!!


## 다양한 변수 선언
# Camel case : numberOfCollegeGraduates -> 메소드 선언할때
# Pascal case : NumberOfCollegeGraduates -> class 선언할때 사용
# Snake case : number_of_college_graduates -> 파이썬에서 주로 변수 선언할때 많이 사용

# 허용하는 변수 선언 법 (밑줄, 대소문자로 시작. 숫자로 시작 안됨)
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8


# 예약어는 변수명으로 불가능
# for, as, class...