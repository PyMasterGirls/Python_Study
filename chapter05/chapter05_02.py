# Chapter05-02
# 파이썬 사용자 입력
# Input 사용법
# 기본 타입(str)

# 예제1
# name = input("Enter your name: ")
# grade = input("Enter your grade: ")
# company = input("Enter your company: ")

# print(name, grade, company)

# # 예제2
# number = input("Enter number: ")
# name = input("Enter name: ")

# print("type of number", type(number), number)
# print("type of name", type(name), name)

# 예제3
first = int(input("Ener number1: "))
second = int(input("Enter number2: "))
print(first + second)

# 예제4
print("FirstName - {0}, LastName - {1}".format(input("Enter first name: "), input("Enter second name: ")))

# 예제5 -> 예외처리
try:
    n = int(input("Enter a number: "))
    print('OK, Your number is : ', n)
except ValueError:
    print('This is not a number')

# 예제6 -> 올바른 값 입력 완료까지 지속
while True:
    try:
        n = int(input('Enter a number: '))
        break
    except ValueError:
        print('This is not a number')

print('OK, Your number is : ', n)