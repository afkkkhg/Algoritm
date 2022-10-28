def task_2(self, n):
    k = 0
    while n != 1:
        if n % 2 == 0:
            k += n / 2
            n = n / 2
        elif n % 2 != 0:
            k += (n - 1) / 2
            n = (n - 1) / 2 + 1
    return k