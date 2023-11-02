# Chapter06-3
# 파이썬 패키지
# 패키지 작성 및 사용법
# __init__.py : Python3.3 부터 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성

# 예제1
import sub.sub1.module1
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# alias 사용 
# import * 가능
from sub.sub1 import module1
from sub.sub2 import module2 as m2

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

