def digit_distance_nums(n1, n2):
         return sum(map(int,str(abs(n1-n2))))



print(digit_distance_nums(121, 599))
print(digit_distance_nums(23, 56))
print(digit_distance_nums(1, 2))
