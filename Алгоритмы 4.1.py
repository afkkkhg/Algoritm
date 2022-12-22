#class Solution:
    def twoCitySchedCost(costs):
		noun = 0
		size = len(costs) // 2
		city1 = 0
		city2 = 0
		costs = sorted(costs, key=lambda x:abs(x[0] - x[1]),reverse = True)

		for i in costs:
			if city2 < size and i[0] >= i[1]:
				noun += i[1]
				city2 += 1
			elif city1 < size and i[1] >= i[0]:
				noun += i[0]
			    city1 += 1
			elif city1 == size:
				noun += i[1]
			elif city2 == size:
				noun +=i [0]


		return noun

