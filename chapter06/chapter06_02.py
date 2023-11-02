# Chapter06-2
# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
    return x+y

def minus(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

def power(x, y):
    return x**y

# __name__ 사용 : main에서만 동작
# 외부에서 import해서 사용되는 모듈인 경우 출력 X
if __name__ == '__main__':
    print('-' * 15)
    print('called! __main__')
    print(add(5, 5))
    print(minus(15, 5))
    print(multiply(2, 3))
    print(divide(10, 2))
    print(power(2, 2))
    print('-' * 15)

