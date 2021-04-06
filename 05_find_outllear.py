def outlier(integers):
       evens =[]
       odds =[]
       for i in integers:
         if i % 2 > 0:
            odds.append(i)
         if i % 2 == 0:
            evens.append(i)
       print("evens",evens)
       print("odds",odds)
       if len(evens)>len(odds):
           return odds[0]
       else:
         return evens[0]
print(outlier([1,2,3,4,7,11]))
