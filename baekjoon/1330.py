num1, num2 = (int(x) for x in input().split())
if num1 > num2:
    print('>')
elif num1 == num2:
    print('==')
else:
    print('<')
