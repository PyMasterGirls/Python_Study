# Chapter03-2
# 파이썬 문자형

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = '''How are you'''

print(type(str1), type(str2), type(str3))
# len() : 문자열 길이 구하는 함수
print(len(str1), len(str2), len(str3))

# 빈 문자열
str_t1 = ''
str_t2 = str()

# 이스케이프 문자 사용
'''
\t : 탭
\n : 줄바꿈
\\ : 문자
\000 : 널 문자
'''
# I'm Boy
print("I'm Boy")
print('I\'m Boy')

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"
print(t_s1)
print(t_s2)

# Raw String (이스케이프 무시) : r''
raw_s1 = r'D:\tPython\test'
print(raw_s1)

# 멀티라인 입력 (여러줄을 한줄로) : \ 쓰고 문자열 이어 쓰기
multi_str = \
'''
문자열
멀티라인 입력
테스트
'''

multi_str1 = \
'Test'\
'Python'\
'MultiLine'
print(multi_str1)

# 문자열 연산
str_o1 = 'Python'
str_o2 = 'Apple'
str_o3 = 'Test'
str_o4 = 'Seoul Busan Jinju'

print(str_o1*3)
print(str_o1 + str_o2)
print('y' in str_o3)    # 'y'가 str_o3에 포함되어 있는지를 묻고 -> True / False로 대답
print('P' not in str_o2)

# 문자열 형 변환
print(str(66))
print(type(str(66)))
print(str(True), type(str(True)))

# 문자열 함수
# upper, isalnum, startswith, count, endswith, isalpha

# capitalize() : 첫 번째 글자만 대문자로 바꿔줌
print("Capitalize: ", str_o1.capitalize())

# endswith(x) : 마지막 문자가 x인지 확인
print("endswith?: ", str_o2.endswith('s'))

# replace(x, y) : x를 y로 대체
print("replace ", str_o1.replace("thon", "God"))

# sorted(x) : 문자열 x를 정렬하여 하나씩 리스트로 만듬
print("sorted: ", sorted(str_o1))

# split(x) : x를 기준으로 문자열을 뷴리하여 리스트로 만듬
print("split: ", str_o4.split(' '))

# 반복 (시퀀스)
im_str = "Good Boy!"
print(dir(im_str))  # __iter__ 가 있다면 반복문 사용 가능

for i in im_str:
    print(i)
print()

# 슬라이싱 연습
str_s1 = "Nice Python"

print(len(str_s1))
print(str_s1[0:3]) # 0 1 2 [x:y] = 인덱스 x~(y-1)
print(str_s1[5:11]) # print(str_s1[5:]) 와 동일
print(str_s1[:len(str_s1)]) # str[0:11]와 동일
print(str_s1[1:4:2])    # 1~3까지 2칸씩 건너뛰기 (단위)

print(str_s1[-5:])  # 문자열 오른쪽에서 왼쪽으로는 -1, -2, -3 ...
print(str_s1[1:-2])
print(str_s1[::2])  # 0~11까지 2칸씩 건너뛰기
print(str_s1[::-1]) # 0~11까지 역순으로 출력

# 아스키 코드
# ord() 아스키코드값 구하는 함수
a = 'Z'
print(ord(a))
print(chr(122))