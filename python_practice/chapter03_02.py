# Chapter03_2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))    # 문자열 길이

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))
print()

# 이스케이프 문자 사용
# I'm Boy
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
"""

print("I'm Boy")
# print('I'm Boy') -> 에러남. ' 때문. 따라서 이럴 경우 " 사용 혹은 이스케이프 문자 사용 (\)
print('I\'m Boy')
print('I\\m Boy')

print('a \t b')     # tab
print('a \n b')     # 줄바꿈
print('a \"\" b')     # a "" b

escape_str1 = "Do tou have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)


# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()


# Raw String 출력 (경로 쓸 때 사용. r'' 의 형태로)
raw_s1 = r'D:\python\test'

print(raw_s1)
print()


# 멀티라인 입력 (긴 텍스트 줄 바꿈해서 넣어주고 싶을때. \ 사용)
multi_str = \
'''
문자열
멀티라인 입력
테스트
'''

print(multi_str)


# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)   # PythonPythonPython (반복 출력)
print(str_o1 + str_o2) # PythonApple
print('y' in str_o1)   # 해당 문자열 안에 y가 있냐 -> 있기 때문에 True 출력됨
print('n' in str_o1)
print('P' not in str_o2)   # True


# 문자열 형 변환
print(str(66), type(str(66)))   # 문자열
print(str(10.1))
print(str(True))


# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)
print("Capitalize: ", str_o1.capitalize())    # 맨 앞 글자만 대문자로 바꿔줌
print("endswith?: ", str_o2.endswith("s"))    # 끝 글자가 s로 끝나냐? 를 알려주는 함수 여기서는 false
print("replace", str_o1.replace("Nice", 'Good'))
print("replace", str_o1.replace("thon", 'Good'))  # replace PyGood 으로 바뀜
print("soarted: ", sorted(str_o1))      # 리스트 형태로 반환. 어떠한 기준에 맞게 정렬되어 나타남. soarted:  ['P', 'h', 'n', 'o', 't', 'y']
print("split: ", str_o4.split(' '))     # 띄어쓰기에 맞춰 자른 후 각 단어들을 리스트로 넣어줌.

print("join str: ", str_o1.join(["I'm ", "!"]))   # join str:  I'm Python!
print("reversed1: ", reversed(str_o2))  # list 형 반환 reversed1:  <reversed object at 0x104627550>
print("reveresd2: ", list(reversed(str_o2)))  # reveresd2:  ['e', 'l', 'p', 'p', 'A']


# 반복 (시퀀스)
im_str = "Good Boy!"

print(dir(im_str))  # 결과 중에 '__iter__' -> 이게 있다면 반복문 쓸 수 있다는 것.

# 출력
for i in im_str:
    print(i)        # 한 글자가 한줄씩 씌여서 출력됨


# 슬라이싱
str_sl = "Nice Python"

# 슬라이싱 연습
print(str_sl[0:3])  # 0~2까지 n-1
print(str_sl[5:])   # [5:11]
print(str_sl[:len(str_sl)])  # str_sl[:11]
print(str_sl[:len(str_sl)-1])
print(str_sl[1:4:2])    # 1~4를 가져오는데 2칸씩 건너띄어서 가져와라
print(str_sl[-5:])      # 맨뒤가 -1. -5부터 오른쪽으로 끝까지 가져오라
print(str_sl[1:-2])     # ice Pyth
print(str_sl[::2])      # 처음부터 끝까지 2칸씩
print(str_sl[::-1])     # 역으로 출력


# 아스키 코드(또는 유니코드)
a = 'z'
print(ord(a))   # 122
print(chr(122)) # z