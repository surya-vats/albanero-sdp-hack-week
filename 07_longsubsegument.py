def longestsubsegment(a,n, k):
        count = 0
        l = 0
        length =0
        for i in range(0,n):
          if a[i]==0:
           count += 1

          while(count>k):
            if a[l] == 0:
               count -= 1
               l += 1
          length = max(length , i-l+1)
          return length


a=[1,0,0,0,1,1,1,0,1,1,0]
n=len(a)
k=2
print(longestsubsegment(a,n,k))
           













