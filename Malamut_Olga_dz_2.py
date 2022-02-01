num = []
sum1 = 0
sum2 = 0
for i in range(1, 1001):
        if i % 2 != 0:
            num.append(i**3)
for idx in range(len(num)):
        num_sum = 0
        j = num[idx]
while j:
            num_sum += j % 10
            j = j // 10
if num_sum % 7 == 0:
                sum1 += num[idx]
                num[idx]+=17
                num_sum = 0
                j = num[idx]
while j:
        num_sum += j % 10
        j = j // 10
        if num_sum % 7 == 0:
            sum2 += num[idx]
print (sum1)
print (sum1)

