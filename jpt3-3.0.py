#for  연습

#1.
# 3. for문의 응용 문제 (44%)

"""
"총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여주시오."
for 이용하자
"""

#방법 1 : for 문을 리스트 안에서
marks = [90, 25, 67, 45, 80]
i = 1
for x in marks:
    if x >=60: print(" %d 번째 학생은 합격입니다" %i)
    else: print ("%d 번째 학생은 불합격입니다" %i)
    i += 1
#방법2 : for 문을 ranage 안에서 if다음에 리스트에서 marks[k] 한거 봐두길..k 는 for 문 돌리는 숫자인데 쓰임.

for k in range(len(marks)):
    if marks [k] >=60: print(" %d 번째 학생 축하합니다. 합격입니다" %(k+1))
    else: continue


#2. 구구단 만들기 for 에 있는 num 이나 i 같은  항목으로도 일반 변수처럼 계산됨.  end=" " 과 print(" ")으로 한칸 띄움.

"""
end = " "는 print함수 때문에 한칸 아래로 내려가는거 방지. 
print (" ")는 한칸아래로 줄바꿈. 

"""

for num in range (2,10):
    for i in range(9):
        print (num*(i+1), end=" " )
    print (" ")

#3. 리스트 내포 list comprehension 연습
# [1, 2, ,3, 4] 중에서 짝수인 2와 4에만 3을 곱하여 담고 싶다
a = [1,2,3,4]
result = [ num*3 for num in a if num%2 == 0] # 이 부분 중요! 숙지하자
print(result)

# 리스트변수이름 = [표현식 for 항목 in 반복가능객체 if 조건문]

#4. 리스트 내포로 구구단 만들기
result = [num*i for num in range(2,10)
          for i in range (1,10)]
print (result)