n = int(input())
if n == 0:
  exit(0)
nums = [0 for i in range(2*n + 1)]
nums[1] = 1

for i in range(1, n // 2 + 1):
  nums[2*i] = nums[i]
  nums[2*i+1]= nums[i] + nums[i+1]
nums = nums[:n+1]
print(max(nums))
