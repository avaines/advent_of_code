# Aparently DP is the key to part 2, 
# The sample code from option 3 re-written in python

# Re-purposed the Dynamic programming approach from https://leetcode.com/problems/climbing-stairs/solution/

def climbstairs(n):
  if n == 1:
    return 1

  dp = [n+1]
  dp.insert(1,1)
  dp.insert(2,2)

  i=3
  while i <= n:
    dp.insert(i, dp[i-1] + dp[i-2])

    i+=1

  return dp

print(climbstairs(6))