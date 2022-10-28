def task_3(self, jewels, stones):
    k = 0
    for i in stones:
        if i in jewels:
            k += 1
    return k