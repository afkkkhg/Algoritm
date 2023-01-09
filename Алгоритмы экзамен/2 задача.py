def strangeCalc(n):
    a = [0] * (n + 1)
    a[1] = 1
    for i in range(2, n + 1):
        a[i] = a[i] + a[i - 1] + a[i - 2]
        if i % 3 == 0:
            a[i] = a[i] + a[i // 3]

    return a[-1]


print(strangeCalc(9))