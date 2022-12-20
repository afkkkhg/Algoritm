def task_4(self, n, k):
    a = ''
    while n > 0:
        a += str(n % k)
        n = n // k
    b = 0
    for i in a:
        b += int(i)
    return b