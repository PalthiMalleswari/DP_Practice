# Question - https://takeuforward.org/plus/dsa/problems/rod-cutting-problem


def calculate_max_price(ind,cur_len):

    if ind == 0:
        return cur_len*price[1]
      
    if cur_len == 0:
        return price[ind]

    # not take
    not_take = calculate_max_price(ind-1,cur_len)

    rod_length = ind + 1
  
  # take
    take = float('-inf')
      
    if rod_length <= cur_len:
          take = calculate_max_price(ind,cur_len-rod_length) + price[ind]
  
    return max(take,not_take)

n = len(price)
calculate_max_price(N,n-1)
# Time Complexity (Exponential) -  O(n^N)
# Space Complexity(Stack Space) -  O(N)

#  Memorization


def calculate_max_price(ind,cur_len):

    if ind == 0:
        dp[ind][cur_len] = cur_len*price[1]
        return dp[ind][cur_len]
      
    if cur_len == 0:
        dp[ind][cur_len] = price[ind]
        return dp[ind][cur_len]
    
    if dp[ind][cur_len] != -1:
      return dp[ind][cur_len]
      
    # not take
    not_take = calculate_max_price(ind-1,cur_len)

    rod_length = ind + 1
  
  # take
    take = float('-inf')
      
    if rod_length <= cur_len:
          take = calculate_max_price(ind,cur_len-rod_length) + price[ind]
  
    dp[ind][cur_len] = max(take,not_take)

    return dp[ind][cur_len]

n = len(price)
dp  = [[ -1 for _ in range(N+1)] for _ in range(n)]
calculate_max_price(N,n-1)
return dp[n-1][N]

# Time Complexity (Exponential) -  O(n*N)
# Space Complexity(Dp Array + Stack Space) -  O(n*N)



    
      
      
