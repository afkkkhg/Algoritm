def task_1(self, number):
    count = 0
    while number > 0:
        if (number % 2 == 0):
            number = number / 2
            count = count + 1
        elif (number % 2 != 0):
            number = number - 1
            count = count + 1
    return (count)
