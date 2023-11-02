# 모듈 사용 실습

import sys

print(sys.path)
print(type(sys.path))

# 파이썬 path에 등록해야 import해서 영구적으로 사용 가능
# 테스트용이면 append해서 사용 가능
# sys.path.append('C:/math')
# print(sys.path)

# import test_module

# # 모듈 사용
# print(test_module.power(10, 3))