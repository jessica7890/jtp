# 50점 이상의 총합

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

sum = 0

i = 0

while i < 10:
    if A[i] > 50:
        sum += A[i]
        i = i + 1
    else:
        i = i + 1

print ( "1st method. the answer is %d " %sum )

#2번째 방법. 답지처럼 해보기
sum = 0
while A:
    mark = A.pop()
    if mark >= 50:
        sum += mark
print ("the second method. the answer is %d" %sum)

"""
왜인지는 몰라도 mark 로 정의한느 대신에 A.pop() 을 바로 넣으니 오류는 아니라도 오답 나옴
A.pop()을 변수대용으로 쓰면 안될거같은 느낌..
답지:
result = 0
while A:  # A 리스트에 값이 있는 동안
    mark = A.pop()  # A리스트의 가장 마지막 항목을 하나씩 뽑아냄
    if mark >= 50:  # 50점 이상의 점수만 더함
        result += mark
"""