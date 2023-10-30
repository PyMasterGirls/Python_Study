# 모듈 사용 실습

import sys

print(sys.path) # 출력되는 경로 안에 모듈들이 존재

print(type(sys.path))   # list

# 모듈 경로 삽입
# sys.path.append('/Users/seungyeon/python_practice/math')

print(sys.path)

# import test_module

# # 모듈 사용
# print(test_module.power(10, 3))

import chapter06_02
