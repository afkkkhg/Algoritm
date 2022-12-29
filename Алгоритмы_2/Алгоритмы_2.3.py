class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = '*' # В исходной матрице заменяем все единицы на звёздочки для удобства вычеслений.
        if obstacleGrid[0][0] == '*':
            return 0 # Если в самом начале матрицы стоит камень вернуть 0
        else:
            for i in range(len(obstacleGrid)):
                for j in range(len(obstacleGrid[0])):
                    if i == 0 and j == 0:
                        obstacleGrid[i][j] = 1 # Если нет камня на самомо первом элементе матрицы поставить 1
                    else:
                        if obstacleGrid[i][j] != '*': 
                            if obstacleGrid[i-1][j] != '*' and obstacleGrid[i][j-1] != '*': 
                                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1] # Если сверху и слева не нашлось камня, то элемент матрицы будет равен сумме верхнего и левого элемента матрицы.
                            elif obstacleGrid[i - 1][j] == '*':
                                obstacleGrid[i][j] = obstacleGrid[i][j - 1] #Если только сверху камень, то элемент будет равен левому элементу
                            elif obstacleGrid[i][j - 1] == '*':
                                obstacleGrid[i][j] = obstacleGrid[i - 1][j] # Если только слева камень, то элемент будет равен верхнему элементу. 
        if obstacleGrid[-1][-1] == '*':
            return 0  #Если последний элемент матрицы - камень - вернуть 0
        else:
            return obstacleGrid[-1][-1] # Вернуть последний элемент матрицы
# Для нахождения всех возможных вариантов нам нужно пройтись по матрице и прибавлять верхний и левый элемент матрицы относительно текущего элемента взависимости от положения камня(-ей). Количество всех возможных вариантов будет характеризовано значением последнего элемента матрицы.
