L = [1, 2, 3, 5]
ans = []
for a in L:
    for b in L:
        for c in L:
            if a!=b and b!=c and a!=c:
                ans.append(a*100 + b*10 + c)
print(ans)