"""
[문제2] 학급의 평균 점수
for문을 이용하여 A 학급의 평균 점수를 구해 보자.

[문제3]
numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
위 코드를 리스트 내포(list comprehension)를 이용하여 표현하시오.
"""
#문제2
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in A:
    sum += i
print (sum/len(A))

#문제3
numbers = [1, 2, 3, 4, 5]
result =[ n*2 for n in numbers if n%2 ==1]
print (result)