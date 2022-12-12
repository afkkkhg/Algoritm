# class Solution(object):
def getDecimalValue(self, head): # создаем функцию
    noun = head # вводим переменную
    num = ''
    while noun!= None: # проверяем пока значение не достигнет "никокого значения"
        num = num + str(noun.val)
        noun = noun.next # перезаписываем текущее значение на следущий элемент

    count = 0
    for i in range(len(num)):  # перевод в другую систему исчисления
        count += int(num[len(num) - 1 - i]) * 2 ** i

    return count