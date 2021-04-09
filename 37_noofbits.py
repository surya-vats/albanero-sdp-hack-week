def numberof1s(self, num: int) -> List[int]:
        dp = [0]*(num+1)
        for i in range(0, num+1):
            if i%2==1:
                dp[i] = dp[floor(i/2)] + 1
            else:
                dp[i]= dp[floor(i/2)]
        return dp
        