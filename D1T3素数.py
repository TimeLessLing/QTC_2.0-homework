def Prime(n):
    flag = True
    for i in range(2, int(n/2)+1, 1):
        if n%i == 0:
            flag = False
            break
    return flag

P = []
for x in range(1, 201, 1):
    if Prime(x):
        P.append(x)

# print(P)
ans = []
for y in P:
    a = int(y/100)
    b = int((y-a*100)/10)
    c = int(y-a*100-b*10)
    if (a+b+c)%2 == 0:
        ans.append(y)

print("200以内素数的数量是",len(P))
print("符合条件的素数分别为",ans)