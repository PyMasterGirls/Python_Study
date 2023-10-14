num = int(input())
list = []
for i in range(0, num):
    a, b = (int(n) for n in input().split())
    list.append(a+b)

for i in range(len(list)):
    print(list[i])
