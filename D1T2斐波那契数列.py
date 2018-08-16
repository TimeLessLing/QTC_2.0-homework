F = [0, 1, 1]
def Fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n >= 3:
        f = Fibonacci(n-1) + Fibonacci(n-2)
        if f not in F:
            F.append(f)
        return f
n = input("请输入数列的长度n=")
Fibonacci(int(n))
print(sum(F))