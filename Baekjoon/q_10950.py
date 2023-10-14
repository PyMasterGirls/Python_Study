T = int(input())

a = []

while T > 0:
    A, B = map(int, input().split())
    a.append(A+B)
    T -= 1

for i in a:
    print(i)