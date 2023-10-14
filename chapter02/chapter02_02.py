# Chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n))



# 동시 선언
x = y = z = 700
print(x, y, z)



# 선언
var = 75

# 재선언
var = "Change Value"

# 출력
print(var)
print(type(var))


# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777
n = 777
print(n, type(n))

# m -> 777 <- n
m = n
print(m, type(m))

m = 400
print(m, n)

# id(identity) 확인 :  객체의 고유값 확인
m = 800
n = 655

# id값 출력
print(id(m))
print(id(n))

print(id(m) == id(n))

# 같은 오브젝트 참조
# m과 n이 같은 값을 가리킨다면 같은 인스터스 (id값이 같음)
# 이들을 하나의 오브젝트로 생성함
m = 800
n = 800

print(id(m))
print(id(n))

print(id(m) == id(n))


# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : number_of_college_graduates -> Variable

# 예약어는 변수명으로 불가능
# ex) as, for, import
