# 1부터 1000까지의 자연수 중 3의 배수의 합을 구하시오.

n = 1
sum = 0
while (3*n) <= 1000:
    sum += 3*n
    n = n+1
print (sum)