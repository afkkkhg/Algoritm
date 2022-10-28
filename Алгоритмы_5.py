def task_5(self, lo, hi, k):
    """
    :type lo: int
    :type hi: int
    :type k: int
    :rtype: int
    """
    values = []
    powers = []
    if not (1 <= lo <= hi <= 1000) or not (1 <= k <= hi - lo + 1):
        exit()

    for i in range(lo, hi + 1):
        values.append(i)

    for x in values:
        steps = []
        while not x == 1:
            if x % 2 == 0:
                x = x / 2
            else:
                x = 3 * x + 1
            steps.append(x)
        powers.append(len(steps))
    results = {}
    for i in range(len(powers)):
        results[values[i]] = powers[i]
    results = sorted(results, key=results.get)
    return results[k - 1]

